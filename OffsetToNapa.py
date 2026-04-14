"""
Hull Form offset TXT → NAPA CUR 변환기

Station      : CUR ST{X}; X {X}  / YZ * (Y Z) ...
Profile(CBM) : CUR CBM; Y 0       / XZ * (X Z) ...  (STERN + STEM PROFILE)
Side Tangent : CUR STM; Y {Y}     / XZ * (X Z) ...  (SIDE TANGENT LINE)
Bot Tangent  : CUR BTM; Z {Z}     / XY * CBM (X Y) ... CBM  (BOTTOM TANGENT LINE)

/- -/ 삽입 규칙
  Station / Side : 연속된 두 점의 Y값이 동일할 경우
  Profile        : 연속된 두 점의 X값이 동일할 경우

Z 보정: 0.001 ~ 0.003 범위는 0.000 으로 치환
"""

import re
import sys
from pathlib import Path


# ── 정규식 ──────────────────────────────────────────────────────────────────
COORD_RE       = re.compile(r'\(\s*(-?\d+\.?\d*)\s*,\s*(-?\d+\.?\d*)\s*,\s*(-?\d+\.?\d*)\s*\)')
X_HEADER_RE    = re.compile(r'\*?\s*X\s*=\s*(-?\d+\.?\d*)\s*m', re.IGNORECASE)
STATION_RE     = re.compile(r'STATION PLAN',   re.IGNORECASE)
STERN_RE       = re.compile(r'STERN PROFILE',  re.IGNORECASE)
STEM_RE        = re.compile(r'STEM PROFILE',   re.IGNORECASE)
SIDE_RE        = re.compile(r'SIDE TANGENT',   re.IGNORECASE)
BOTTOM_RE      = re.compile(r'BOTTOM TANGENT', re.IGNORECASE)
PLAIN_COORD_RE = re.compile(r'^\s*(-?\d+\.?\d+)\s+(-?\d+\.?\d+)\s+(-?\d+\.?\d+)\s*$')

TOL = 0.005   # 동일 좌표 판정 허용 오차 (m)


# ── 공통 유틸 ────────────────────────────────────────────────────────────────
def fix_z(z: float) -> float:
    """Z값이 0.001~0.003 범위이면 0으로 보정."""
    return 0.0 if 0.001 <= z <= 0.003 else z


def fmt(n: float) -> str:
    """숫자를 NAPA 좌표 표기로 변환 (불필요한 소수점 0 제거)."""
    s = f"{n:.3f}".rstrip('0').rstrip('.')
    return s


def dedup(points):
    seen = set()
    result = []
    for p in points:
        key = tuple(round(v, 6) for v in p)
        if key not in seen:
            seen.add(key)
            result.append(p)
    return result


def collapse(points, key_idx: int):
    """
    key_idx 기준값이 연속으로 같은 구간을 첫점·끝점만 남긴다.
    key_idx=0 : X 기준 (Profile)
    key_idx=0 : Y 기준 (Station) — collapse_same_y 와 동일 로직
    정렬은 호출 전에 완료된 상태로 가정.
    """
    if not points:
        return points
    collapsed = []
    i = 0
    while i < len(points):
        ref_val   = points[i][key_idx]
        run_start = points[i]
        run_end   = points[i]
        j = i + 1
        while j < len(points) and abs(points[j][key_idx] - ref_val) < TOL:
            run_end = points[j]
            j += 1
        collapsed.append(run_start)
        if j - i > 1:
            collapsed.append(run_end)
        i = j
    return collapsed


# ── 파싱 ─────────────────────────────────────────────────────────────────────
def _extract_coords(line):
    """한 줄에서 (x, y, z) 추출. 없으면 None."""
    m = COORD_RE.search(line)
    if m:
        return float(m.group(1)), float(m.group(2)), float(m.group(3))
    m = PLAIN_COORD_RE.match(line)
    if m:
        return float(m.group(1)), float(m.group(2)), float(m.group(3))
    return None


def parse_all(filepath: str):
    """
    반환:
      stations : {x_val: [(y, z), ...]}
      stern    : [(x, z), ...]
      stem     : [(x, z), ...]
    """
    lines = Path(filepath).read_text(encoding='utf-8', errors='ignore').splitlines()

    stations: dict[float, list] = {}
    stern:    list = []
    stem:     list = []
    side:     list = []   # (x, y, z) — y는 STM 헤더에 사용
    bottom:   list = []   # (x, y, z) — z는 BTM 헤더에 사용

    # 현재 섹션 상태
    section = None          # 'station' | 'stern' | 'stem' | None
    current_x = None        # station 전용

    for line in lines:
        # ── 섹션 헤더 감지 ──────────────────────────────────────────────────
        if STATION_RE.search(line):
            section = 'station'
            # 같은 줄에 X= 가 있을 수 있으므로 fall-through
        elif STERN_RE.search(line):
            section = 'stern'
            current_x = None
            continue
        elif STEM_RE.search(line):
            section = 'stem'
            current_x = None
            continue
        elif SIDE_RE.search(line):
            section = 'side'
            current_x = None
            continue
        elif BOTTOM_RE.search(line):
            section = 'bottom'
            current_x = None
            continue

        if section is None:
            continue

        # ── Station X 헤더 ──────────────────────────────────────────────────
        if section == 'station':
            xm = X_HEADER_RE.search(line)
            if xm:
                current_x = float(xm.group(1))
                if current_x not in stations:
                    stations[current_x] = []
                continue
            if current_x is None:
                continue

        # ── 좌표 파싱 ────────────────────────────────────────────────────────
        coords = _extract_coords(line)
        if coords is None:
            continue
        cx, cy, cz = coords

        if section == 'station':
            stations[current_x].append((cy, cz))
        elif section == 'stern':
            stern.append((cx, fix_z(cz)))
        elif section == 'stem':
            stem.append((cx, fix_z(cz)))
        elif section == 'side':
            side.append((cx, cy, fix_z(cz)))   # y값 보존 (STM 헤더에 사용)
        elif section == 'bottom':
            bottom.append((cx, cy, fix_z(cz))) # z값 보존 (BTM 헤더에 사용)

    return stations, stern, stem, side, bottom


# ── NAPA 출력 ────────────────────────────────────────────────────────────────
def _interp_stm_z(x_val: float, side_points) -> tuple[float, float] | None:
    """STM의 X범위 내에 있으면 (Y_stm, Z_stm) 보간값 반환, 범위 밖이면 None."""
    if not side_points:
        return None
    # x 오름차순 정렬
    pts = sorted(side_points, key=lambda p: p[0])
    x_min, x_max = pts[0][0], pts[-1][0]
    if x_val < x_min - TOL or x_val > x_max + TOL:
        return None
    y_stm = pts[0][1]   # Y는 고정값
    # 경계 처리
    if x_val <= pts[0][0]:
        return y_stm, pts[0][2]
    if x_val >= pts[-1][0]:
        return y_stm, pts[-1][2]
    # 선형 보간
    for i in range(len(pts) - 1):
        x0, _, z0 = pts[i]
        x1, _, z1 = pts[i+1]
        if x0 <= x_val <= x1:
            t = (x_val - x0) / (x1 - x0) if abs(x1 - x0) > 1e-9 else 0
            return y_stm, z0 + t * (z1 - z0)
    return None


def to_station_curve(x_val: float, raw_points, cbm_max_z: float = None,
                     side_points=None) -> str:
    """Station → CUR ST{X}; X {X} / YZ * (Y Z) ...

    규칙 1: station 첫 Z < cbm_max_z → 같은 Y로 cbm_max_z까지 /- -/ 연장
    규칙 2: Z ≈ 0, Y ≠ 0 → BTM / Z ≈ 0, Y ≈ 0 → CBM / 둘 다 → BTM /- -/ CBM
            Z=0 없으면 마지막에 CBM 추가
    규칙 3: station X가 STM X 범위 내 → Z_stm 이하 좌표만 출력,
            상단을 (Y_stm, cbm_max_z) /- -/ STM 으로 시작
    """
    if not raw_points:
        return ""

    # STM 교차점 계산
    stm_result = _interp_stm_z(x_val, side_points) if side_points else None
    _, z_stm = stm_result if stm_result else (None, None)

    # Z=0 점과 일반 점 분리
    zero_z  = [(y, z) for y, z in raw_points if abs(z) < TOL]
    nonzero = [(y, z) for y, z in raw_points if abs(z) >= TOL]

    has_btm = any(abs(y) >= TOL for y, _ in zero_z)
    has_cbm = any(abs(y) <  TOL for y, _ in zero_z)

    # 규칙 3: STM 범위 내면 Z_stm 이하 좌표만 사용
    if z_stm is not None:
        nonzero = [(y, z) for y, z in nonzero if z <= z_stm + TOL]

    # 일반 점 정렬 & collapse
    pts = sorted(dedup(nonzero), key=lambda p: (p[1], p[0]), reverse=True)
    pts = collapse(pts, key_idx=0)

    x_str = fmt(x_val)
    header = f"CUR ST{x_str}; X {x_str}"

    parts = []

    if z_stm is not None:
        # 규칙 3: STM 으로 시작 (규칙 1 미적용)
        parts.append("STM")
    else:
        # 규칙 1: CBM 최대 Z 연장
        if cbm_max_z is not None and pts:
            first_y, first_z = pts[0]
            if first_z < cbm_max_z - TOL:
                parts.append(f"({fmt(first_y)},{fmt(cbm_max_z)})")
                parts.append("/- -/")

    # 일반 좌표 출력
    for i, (y, z) in enumerate(pts):
        if i > 0 and abs(y - pts[i-1][0]) < TOL:
            parts.append("/- -/")
        parts.append(f"({fmt(y)},{fmt(z)})")

    # 규칙 2: Z=0 처리
    if has_btm and has_cbm:
        parts.append("BTM")
        parts.append("/- -/")
        parts.append("CBM")
    elif has_btm:
        parts.append("BTM")
    elif has_cbm:
        parts.append("CBM")
    else:
        parts.append("CBM")

    return f"{header}\nYZ     * {' '.join(parts)}; OK"


def to_profile_curve(stern_points, stem_points, name: str = "CBM") -> str:
    """STERN + STEM → CUR CBM; Y 0 / XZ * (X Z) ... (텍스트 순서 유지, 한번에 정의)"""
    if not stern_points and not stem_points:
        return ""

    stern_pts = collapse(dedup(stern_points), key_idx=0)
    stem_pts  = collapse(dedup(stem_points),  key_idx=0)

    header = f"CUR   {name}; Y 0"
    parts  = []

    for i, (x, z) in enumerate(stern_pts):
        if i > 0 and abs(x - stern_pts[i-1][0]) < TOL:
            parts.append("/- -/")
        parts.append(f"({fmt(x)},{fmt(z)})")

    for i, (x, z) in enumerate(stem_pts):
        if i == 0 and stern_pts:
            parts.append("/- -/")   # STERN→STEM 연결부 강제 삽입
        elif i > 0 and abs(x - stem_pts[i-1][0]) < TOL:
            parts.append("/- -/")
        parts.append(f"({fmt(x)},{fmt(z)})")

    return f"{header}\nXZ     * {' '.join(parts)}; OK"


def to_side_curve(raw_points) -> str:
    """SIDE TANGENT LINE → CUR STM; Y {Y} / XZ * (X Z) ..."""
    if not raw_points:
        return ""

    # Y값은 첫 점에서 추출 (일정값)
    y_val = raw_points[0][1]

    # (x, z) 로 변환 후 collapse
    xz_points = [(x, z) for x, _, z in raw_points]
    pts = collapse(dedup(xz_points), key_idx=0)

    header = f"CUR   STM; Y {fmt(y_val)}"

    parts = []
    for i, (x, z) in enumerate(pts):
        if i > 0 and abs(x - pts[i-1][0]) < TOL:
            parts.append("/- -/")
        parts.append(f"({fmt(x)},{fmt(z)})")

    return f"{header}\nXZ     * {' '.join(parts)}; OK"


def to_bottom_curve(raw_points) -> str:
    """BOTTOM TANGENT LINE → CUR BTM; Z {Z} / XY * CBM (X Y) ... CBM
    Y ≈ 0 인 점은 좌표 대신 CBM 으로 출력한다."""
    if not raw_points:
        return ""

    z_val = raw_points[0][2]

    xy_points = [(x, y) for x, y, _ in raw_points]
    pts = collapse(dedup(xy_points), key_idx=0)

    header = f"CUR   BTM; Z {fmt(z_val)}"

    parts = []
    prev_x = None
    for (x, y) in pts:
        if abs(y) < TOL:                        # Y ≈ 0 → CBM
            if parts and parts[-1] != "CBM":    # 연속 CBM 중복 방지
                parts.append("CBM")
            elif not parts:
                parts.append("CBM")
        else:
            if prev_x is not None and abs(x - prev_x) < TOL:
                parts.append("/- -/")
            parts.append(f"({fmt(x)},{fmt(y)})")
        prev_x = x

    return f"{header}\nXY     * {' '.join(parts)}; OK"


def _stm_xs_at_z(wl_z: float, side_points) -> list[float]:
    """WL_Z에서 STM 곡선의 모든 X 교차값을 반환 (순서 유지)."""
    if not side_points:
        return []
    pts = [(x, z) for x, _, z in side_points]
    xs = []
    for i in range(len(pts) - 1):
        x0, z0 = pts[i]
        x1, z1 = pts[i + 1]
        if abs(z0 - z1) < TOL:
            # 수평 구간: WL_Z가 이 Z에 해당하면 양 끝점 추가
            if abs(z0 - wl_z) < TOL:
                xs.append(x0)
                xs.append(x1)
            continue
        lo, hi = min(z0, z1), max(z0, z1)
        if lo - TOL <= wl_z <= hi + TOL:
            t = (wl_z - z0) / (z1 - z0)
            xs.append(x0 + t * (x1 - x0))
    # 중복 제거 (순서 유지)
    seen = set()
    result = []
    for x in xs:
        key = round(x, 4)
        if key not in seen:
            seen.add(key)
            result.append(x)
    return result


def to_waterlines(stations: dict, side_points, cbm_max_z: float,
                  step: float = 1.0, cbm_first_z_min: float = None) -> list[str]:
    """
    Z = step 단위로 cbm_max_z 까지 WATER LINE 생성.
    각 WL에는 해당 Z가 Station의 Z 범위 내에 있는 Station만 포함.
    STM 범위 내 Station은 STM Z_stm 이하일 때만 포함.
    WL_Z에서 STM 교차점이 있으면 STM/X=# 으로 삽입.
    인접한 두 STM 참조 사이에는 /- -/ 삽입.
    첫 Station X == cbm_first_x 이고 WL_Z >= cbm_first_z_min 이면 CBM /- -/ ST... 로 연결.
    형식: CUR WL{Z}; Z {Z}
          XY * CBM ... STM/X=# ... CBM; OK
    """
    if not cbm_max_z:
        return []

    # WL Z값 목록 생성
    wl_zs = []
    z = step
    while z < cbm_max_z - TOL:
        wl_zs.append(round(z, 6))
        z += step
    wl_zs.append(cbm_max_z)

    # 각 station의 Z 범위 및 STM 교차점 미리 계산
    st_info = {}   # x_val → (z_min, z_max, z_stm_or_None)
    for x_val, pts in stations.items():
        nonzero = [z for _, z in pts if abs(z) >= TOL]
        if not nonzero:
            continue
        has_btm_pt = any(abs(z) < TOL and abs(y) >= TOL for y, z in pts)
        z_min = 0.0 if has_btm_pt else min(nonzero)
        raw_z_max = max(nonzero)
        z_max = cbm_max_z if (cbm_max_z and raw_z_max < cbm_max_z - TOL) else raw_z_max
        stm_result = _interp_stm_z(x_val, side_points) if side_points else None
        z_stm = stm_result[1] if stm_result else None
        st_info[x_val] = (z_min, z_max, z_stm)

    sorted_xs = sorted(st_info.keys())

    curves = []
    for wl_z in wl_zs:
        # 포함 Station 필터링 → (x_val, name) 목록
        items: list[tuple[float, str]] = []
        for x_val in sorted_xs:
            z_min, z_max, z_stm = st_info[x_val]
            if wl_z < z_min - TOL or wl_z > z_max + TOL:
                continue
            if z_stm is not None and wl_z > z_stm + TOL:
                continue
            items.append((x_val, f"ST{fmt(x_val)}"))

        # STM 교차점 추가
        for x_stm in _stm_xs_at_z(wl_z, side_points):
            items.append((x_stm, f"STM/X=#{fmt(x_stm)}"))

        if not items:
            continue

        # X 오름차순 정렬
        items.sort(key=lambda p: p[0])

        # 이름 목록 조합 (인접 STM 사이에 /- -/ 삽입)
        names = []
        # CBM이 cbm_first_x에서 유효한 Z 범위(>= cbm_first_z_min) 내이면 CBM /- -/ ST...
        if cbm_first_z_min is not None and wl_z >= cbm_first_z_min - TOL:
            names.append("/- -/")
        for i, (_, name) in enumerate(items):
            if i > 0 and name.startswith("STM/") and items[i-1][1].startswith("STM/"):
                names.append("/- -/")
            names.append(name)

        z_str = fmt(wl_z)
        header = f"CUR WL{z_str}; Z {z_str}"
        body   = f"XY * CBM {' '.join(names)} CBM; OK"
        curves.append(f"{header}\n{body}")

    return curves


def to_hull(has_cbm: bool, has_stm: bool, has_btm: bool,
            station_xs: list[float], wl_zs: list[float]) -> str:
    """HULL 서페이스 정의 — 생성된 모든 CURVE 이름을 THR 뒤에 나열."""
    names = []
    if has_cbm:
        names.append("CBM")
    if has_stm:
        names.append("STM")
    if has_btm:
        names.append("BTM")
    for x in station_xs:
        names.append(f"ST{fmt(x)}")
    for z in wl_zs:
        names.append(f"WL{fmt(z)}")
    comment = (
        "@@ TRANSOME의 경우 직접 모델링 후 WL에 추가하시오\n"
        "@@ HULL_P 정의에 TRANSOME 을 추가하시오\n"
    )
    return f"{comment}\n@@SUR HULL_P\n@@THR {' '.join(names)}; OK"


# ── 변환 진입점 ──────────────────────────────────────────────────────────────
def convert(input_path: str, output_path: str | None = None) -> None:
    stations, stern, stem, side, bottom = parse_all(input_path)

    if output_path is None:
        output_path = Path(input_path).stem + "_napa.txt"

    out_lines = []

    # STERN + STEM → CBM 한번에 정의
    if stern or stem:
        out_lines.append(to_profile_curve(stern, stem, "CBM"))
        out_lines.append("")

    # SIDE TANGENT LINE → STM
    if side:
        out_lines.append(to_side_curve(side))
        out_lines.append("")

    # BOTTOM TANGENT LINE → BTM
    if bottom:
        out_lines.append(to_bottom_curve(bottom))
        out_lines.append("")

    # CBM 최대 Z 계산 (stern + stem 전체에서)
    cbm_max_z = None
    all_profile = [(x, z) for x, z in stern] + [(x, z) for x, z in stem]
    if all_profile:
        cbm_max_z = max(z for _, z in all_profile)

    # STATION PLAN
    for x_val in sorted(stations.keys()):
        curve = to_station_curve(x_val, stations[x_val], cbm_max_z, side)
        if curve:
            out_lines.append(curve)
            out_lines.append("")

    # CBM 시작 X 및 해당 X의 최소 Z 계산 (stern 첫 점, 없으면 stem 첫 점)
    cbm_first_x    = None
    cbm_first_z_min = None
    stern_collapsed = collapse(dedup(stern), key_idx=0) if stern else []
    stem_collapsed  = collapse(dedup(stem),  key_idx=0) if stem  else []
    if stern_collapsed:
        cbm_first_x = stern_collapsed[0][0]
        zs_at_x = [z for x, z in stern if abs(x - cbm_first_x) < TOL]
        if zs_at_x:
            cbm_first_z_min = min(zs_at_x)
    elif stem_collapsed:
        cbm_first_x = stem_collapsed[0][0]
        zs_at_x = [z for x, z in stem if abs(x - cbm_first_x) < TOL]
        if zs_at_x:
            cbm_first_z_min = min(zs_at_x)

    # WATER LINE
    wl_list = []
    if cbm_max_z:
        wl_list = to_waterlines(stations, side, cbm_max_z,
                                cbm_first_z_min=cbm_first_z_min)
        for wl in wl_list:
            out_lines.append(wl)
            out_lines.append("")

    # HULL
    wl_zs = []
    for wl in wl_list:
        # 첫 줄에서 Z값 추출: "CUR WL{z}; Z {z}"
        z_str = wl.split('\n')[0].split('; Z ')[-1]
        try:
            wl_zs.append(float(z_str))
        except ValueError:
            pass
    hull = to_hull(
        has_cbm=bool(stern or stem),
        has_stm=bool(side),
        has_btm=bool(bottom),
        station_xs=sorted(stations.keys()),
        wl_zs=wl_zs,
    )
    out_lines.append(hull)
    out_lines.append("")

    Path(output_path).write_text("\n".join(out_lines), encoding='utf-8')
    print(f"변환 완료: STERN {'O' if stern else 'X'} / STEM {'O' if stem else 'X'} / SIDE {'O' if side else 'X'} / BOTTOM {'O' if bottom else 'X'} / Station {len(stations)}개 → {output_path}")


def preview(input_path: str) -> None:
    stations, stern, stem, side, bottom = parse_all(input_path)

    if stern or stem:
        print("=== CBM (STERN + STEM) ===")
        print(to_profile_curve(stern, stem, "CBM"))
        print()

    if side:
        print("=== STM (SIDE TANGENT LINE) ===")
        print(to_side_curve(side))
        print()

    if bottom:
        print("=== BTM (BOTTOM TANGENT LINE) ===")
        print(to_bottom_curve(bottom))
        print()

    cbm_max_z = None
    all_profile = [(x, z) for x, z in stern] + [(x, z) for x, z in stem]
    if all_profile:
        cbm_max_z = max(z for _, z in all_profile)

    print("=== STATION (처음 3개) ===")
    for x_val in sorted(stations.keys())[:3]:
        print(to_station_curve(x_val, stations[x_val], cbm_max_z, side))
        print()

    if cbm_max_z:
        print("=== WATER LINE (처음 3개) ===")
        for wl in to_waterlines(stations, side, cbm_max_z)[:3]:
            print(wl)
            print()


# ── main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법:")
        print("  python OffsetToNapa.py <input.txt> [output.txt]")
        print("  python OffsetToNapa.py <input.txt> --preview")
        sys.exit(0)

    inp = sys.argv[1]
    if len(sys.argv) >= 3 and sys.argv[2] == "--preview":
        preview(inp)
    else:
        out = sys.argv[2] if len(sys.argv) >= 3 else None
        convert(inp, out)
