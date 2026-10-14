"""retrofit_data/*.json -> retrofit_data/data.js

Retrofit.html 을 파일로 직접 열 때(file://)는 브라우저가 JSON fetch 를 막기 때문에,
JSON 3개를 <script> 로 읽을 수 있는 data.js 로 묶어 둔다.
JSON 을 수정한 뒤 이 스크립트를 한 번 실행하면 된다:  python retrofit_data/build_data.py
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
FILES = {
    "db": "DB.json",
    "defs": "주요개조.json",
    "area": "항해구역+길이별 요건.json",
}


def load_loose(path: Path):
    # 끝에 붙은 잔재(``` 등)가 있어도 마지막 '}' 까지만 읽는다
    text = path.read_text(encoding="utf-8-sig")
    return json.loads(text[: text.rfind("}") + 1])


def main():
    data = {key: load_loose(HERE / name) for key, name in FILES.items()}
    body = json.dumps(data, ensure_ascii=False, indent=1)
    out = HERE / "data.js"
    out.write_text(
        "// 자동 생성 파일 — 직접 수정하지 말고 JSON 수정 후 build_data.py 를 실행하세요.\n"
        f"window.RETROFIT_DATA = {body};\n",
        encoding="utf-8",
    )
    print(f"{out.name} 생성 완료: " + ", ".join(f"{k}={FILES[k]}" for k in FILES))


if __name__ == "__main__":
    main()
