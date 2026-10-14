// 자동 생성 파일 — 직접 수정하지 말고 JSON 수정 후 build_data.py 를 실행하세요.
window.RETROFIT_DATA = {
 "db": {
  "DB": [
   {
    "개조": "Cargo Tank 용량변경, 추가등",
    "조치해야할 도면": "- INTACT STABILITY BOOKLET\n- LOADING MANUAL\n  (INCL. TYPICAL LOADING UNLOADING)\n- DAMAGE STABILITY BOOKLET\n- LOADING INSTRUMENT TEST REPORT (권고)\n- GRAIN STABILITY BOOKLET",
    "비고": "-"
   },
   {
    "개조": "Water Ballast Tank 용도변경",
    "조치해야할 도면": "A. Consumable tank로 변경 \n - INTACT STABILITY BOOKLET\n - LOADING MANUAL\n   (INCL. TYPICAL LOADING UNLOADING)\n - DAMAGE STABILITY BOOKLET\n - LOADING INSTRUMENT TEST REPORT (권고)\n\nB. MISC. tank,VOID로 변경 \n  - [KR NOTE] 부착 // 강도, 용량등 고려 X",
    "비고": "- 하기 Note를 복원성 관련도면에 부착하고 현장검사원 확인 받도록 \"C\" Comment \n\n[KR Note] \nThe No.5 W.B TANK(P) has been changed to dual purpose tank of No.5 W.B TANK(P) / treated sewage storage tank\". Accordingly, the Master is responsible for acknowledging this change and establishing the loading/discharge plan."
   },
   {
    "개조": "Bunker tank (FO, LO, DO, FW)",
    "조치해야할 도면": "A. 다른 용도의 Consumable tank로 변경 시\n   (ex. HFO -> LFHO, FWT -> DWT 등)\n  - [KR NOTE] 부착 // 강도, 용량등 고려 X\n\nB. MISC. tank, VOID로 변경\n  - [KR NOTE] 부착 // 강도, 용량등 고려 X\n\nC. 전혀 다른 탱크로 변경 시 (W.B.T, C.O.T 등)\n - INTACT STABILITY BOOKLET\n - LOADING MANUAL\n   (INCL. TYPICAL LOADING UNLOADING)\n - DAMAGE STABILITY BOOKLET\n - LOADING INSTRUMENT TEST REPORT (권고)",
    "비고": "-"
   },
   {
    "개조": "Draft Increase",
    "조치해야할 도면": "- INTACT STABILITY BOOKLET\n - LOADING MANUAL\n   (INCL. TYPICAL LOADING UNLOADING)\n - DAMAGE STABILITY BOOKLET\n - LOADING INSTRUMENT TEST REPORT\n - GRAIN STABILITY BOOKLET\n - TOTAL RES. CALCULATION",
    "비고": "-"
   },
   {
    "개조": "Draft Decrease",
    "조치해야할 도면": "- EEDI/EEXI Technical file (주요개조)",
    "비고": "- 하기 Note를 복원성 관련도면에 부착하고 현장검사원 확인 받도록 \"C\" Comment \n\n[KR Note]\nThe freeboard was newly assigned as of 10th Oct, 2023 (f=2649 mm, Draft (mould) = 4.674m). Therefore, the master shall keep loading up to a newly assigned freeboard."
   },
   {
    "개조": "LWT Change",
    "조치해야할 도면": "# 누적 개조량이 SC297 / 선박안전법 기준을 초과하는 경우, 개조 완료 및 출항전 최소 Prov. 도면 승인 필요\n\n - RESULT OF I/E & D/M\n - INTACT STABILITY BOOKLET\n - LOADING MANUAL\n   (INCL. TYPICAL LOADING UNLOADING)\n - DAMAGE STABILITY BOOKLET\n - LOADING INSTRUMENT TEST REPORT\n - EEDI/EEXI Technical file",
    "비고": "# SC297\n              경사시험  //  복원성 자료 \n - LWT :            2% //  2% ~ 1% \n - LCG :            1% //  1% ~ 0.5% (Lf 기준)\n - VCG :           1% //  1% ~ 0.5\n\n# 선박안전법 시행규칙 \n             경사시험  //  복원성 자료 \n - LWT :  Max(2%, 2ton) //  2% ~ 1% \n - LCG :        1% //  1% ~ 0.5% (LBP 기준)\n - VCG 大 : LWT 0.5%초과시 복원성 자료 재승인\n - VCG 小 : LWT 1.5%초과시 복원성 자료 재승인\n\n * 개조후 여객선의 VCG 상승 및 화물선 경하상태의 GoM이 0 미만으로 변경되는 개조는 불가하므로 사전에 확인 하도록 안내 할 것"
   },
   {
    "개조": "Ship type change \nFrom Chemical to Oil/Chemical Tanker",
    "조치해야할 도면": "- INTACT STABILITY BOOKLET\n - LOADING MANUAL\n   (INCL. TYPICAL LOADING UNLOADING)\n - DAMAGE STABILITY BOOKLET\n - LOADING INSTRUMENT TEST REPORT (if need)\n - MARPOL I/23",
    "비고": "-"
   },
   {
    "개조": "Ship type change \nFrom Oil to Oil / Chemical Tanker",
    "조치해야할 도면": "- INTACT STABILITY BOOKLET\n - LOADING MANUAL\n   (INCL. TYPICAL LOADING UNLOADING)\n - DAMAGE STABILITY BOOKLET\n - LOADING INSTRUMENT TEST REPORT (if need)\n\n # Reflecting type II, 3,000m3 limit",
    "비고": "-"
   },
   {
    "개조": "On deck Cargo Loading",
    "조치해야할 도면": "- INTACT STABILITY BOOKLET\n - LOADING MANUAL\n   (INCL. TYPICAL LOADING UNLOADING)\n - DAMAGE STABILITY BOOKLET (if need)\n - LOADING INSTRUMENT TEST REPORT \n\n # On-deck allowable uniform loading 반영 (구조기술 1팀 지정)\nICLL Damage 적용선박인 경우, SOLAS Damage 의 GM Curve 반영",
    "비고": "-"
   }
  ]
 },
 "defs": {
  "title": "주요개조 관련 정의 및 내규 정리",
  "sections": [
   {
    "regulation": "SOLAS II-1/1.3 - Circ. 1246",
    "content": "\"주요특성의 개조 및 변경\"이란 표현은, 화물선의 구획 및 복원성과 관련하여, 그 선박의 구획 수준에 영향을 주는 구조에 대한 변경을 말한다. 화물선이 그러한 변경을 하는 경우, 그러한 변경후 그 선박 에 대하여 계산된 A/R율이 변경전 그 선박에 대하여 계산된 A/R율 보다 적지 아니 하여야 한다. 그러나 변경전 그 선박의 A/R율이 1 이상인 경우, 변경후 선박이 변경된 선박에 대하여 계산된 R보다 적지 아니 한 A값을 가져야 할 필요만 있다."
   },
   {
    "regulation": "SOLAS II-1/1.3.4",
    "content": "여객선으로 개조되는 화물선은 그 건조일자와 상관없이 이러한 개조가 시작된 날에 건조된 여객선으로 간주한다."
   },
   {
    "regulation": "MSC. 429(98) Reg 1.3",
    "content": "If a passenger ship that has been in domestic service only and never been issued a SOLAS Passenger Ship Safety Certificate is converted to international service, for purposes of the stability requirements in parts B, B-1, B-2, B-3 and B-4 it should be treated as a passenger ship constructed on the date on which such a conversion commences."
   },
   {
    "regulation": "MARPOL Annex I/1",
    "description": "선박의 주요개조 정의",
    "items": [
     "당해 선박의 치수 또는 운송 용량을 실질적으로 변경하는 것",
     "당해 선박의 종류를 변경하는 것",
     "당해 개조의 목적이 실질적으로 당해 선박의 연한을 연장하는 것이라고 주관청이 인정하는 것",
     "만약 당해 선박이 신선이라면, 현존선에는 적용되지 아니하는 이 협약의 규정을 적용받게 되는 정도로 당해 선박을 개조하는 것"
    ],
    "exceptions": [
     "규칙1.28.3에 규정된 1982년 6월 1일 이전에 인도된 재화중량톤수 20,000톤 이상의 유탱커를 이 부속서 제18규칙의 요건에 적합하게 하기 위한 개조는 이 부속서의 목적상 주요개조로 간주하지 아니한다.",
     "이 부속서 제19 또는 20규칙의 요건을 만족하기 위하여 규칙1.28.5에 규정된 1996년 7월 6일 전에 인도된 유탱커의 개조는 이 부속서의 목적상 주요개조로 간주하지 아니한다."
    ]
   },
   {
    "regulation": "MARPOL Annex V/2.17",
    "description": "제4장과 관련하여 '주요개조'의 정의",
    "items": [
     "당해 선박의 치수, 운송능력 또는 엔진 출력을 실질적으로 변경하는 것",
     "당해 선박의 종류를 변경하는 것",
     "당해 개조의 목적이 실질적으로 당해 선박의 연한을 연장하는 것이라고 주관청이 인정하는 것",
     "만약, 당해 선박이 신선이라면, 현존선에는 적용되지 아니하는 이 협약의 규정을 적용받게 되는 정도로 당해 선박을 개조하는 것",
     "선박의 에너지 효율을 실질적으로 변경하고 이 부속서의 제24규칙에 규정된 해당 “EEDI 허용값” 또는 제25규칙에 규정된 해당 \"EEXI 허용값\"을 선박이 초과할 수 있는 어떠한 변경을 포함하는 것"
    ]
   },
   {
    "regulation": "MEPC.1/Circ.795",
    "content": "For regulation 2.2.17.1, any substantial change in hull dimensions and/or capacity (e.g. change of length between perpendiculars (LPP) or change of assigned freeboard) should be considered a major conversion. Any substantial increase of total engine power for propulsion (e.g. 5% or more) should be considered a major conversion. In any case, it is the Administration's authority to evaluate and decide whether an alteration should be considered a major conversion, consistent with chapter 4.",
    "note": "Notwithstanding paragraph 2.1, assuming no alteration to the ship structure, both decrease of assigned freeboard and temporary increase of assigned freeboard due to the limitation of deadweight or draft at calling port should not be construed as a major conversion. However, an increase of assigned freeboard, except a temporary increase, should be construed as a major conversion."
   },
   {
    "category": "개조와 관련된 적용 예 - 협약검사내규 1편 1.5.6",
    "major_conversions": [
     {
      "type": "주요 개조",
      "modifications": [
       {
        "item": "Modify Hull Dimension (예, Lengthening)",
        "solas_application": "개조부분에만 개조시점의 SOLAS를 적용. (단, 톤수의 변경 또는 선박길이의 변경으로 인한 추가 규정이 발생하였을 경우 그 설비는 개조당시의 규정에 적합할 것. 예를 들어 톤수 변경에 따른 고정식 소화설비)",
        "marpol_application": "개조시점의 MARPOL 규정 적용"
       },
       {
        "item": "Increase The Passenger Carrying Capacity",
        "solas_application": "개조부분에만 개조시점의 SOLAS를 적용. (단, 톤수의 변경 또는 선박길이의 변경으로 인한 추가 규정이 발생하였을 경우 그 설비는 개조당시의 규정에 적합할 것. 예를 들어 톤수 변경에 따른 고정식 소화설비)",
        "marpol_application": "톤수변경이 수반되지 않을 경우 적용제외"
       },
       {
        "item": "Vehicle Deck Converted to Passenger Accommodation",
        "solas_application": "개조부분에만 개조시점의 SOLAS를 적용. (단, 톤수의 변경 또는 선박길이의 변경으로 인한 추가 규정이 발생하였을 경우 그 설비는 개조당시의 규정에 적합할 것. 예를 들어 톤수 변경에 따른 고정식 소화설비)",
        "marpol_application": "톤수변경이 수반되지 않을 경우 적용제외"
       }
      ]
     },
     {
      "type": "변경 (a) 항행구역 변경",
      "modifications": [
       {
        "item": "항행구역 변경",
        "before": "국내항해로 건조된 선박",
        "after": "국제항해",
        "solas_application": "건조시 KEEL LAYING에 따른 SOLAS 요건 적용 (소급적용부분 적용, 소급적용에 대한 현행 규정 만족되어야 함)",
        "marpol_application": "건조시 KEEL LAYING에 따른 MARPOL 요건 적용 (소급적용부분 적용, 소급적용에 대한 현행 규정 만족되어야 함)"
       }
      ]
     },
     {
      "type": "변경 (b) 용도변경",
      "modifications": [
       {
        "before": "OIL",
        "after": "CHEMICAL",
        "solas_application": "건조시 KEEL LAYING에 따른 SOLAS (IBC/BCH CODE) 요건 적용(소급적용부분 적용, 소급적용에 대한 현행 규정 만족되어야 함)",
        "marpol_application": "개조시점의 MARPOL 규정 적용"
       },
       {
        "before": "CHEMICAL",
        "after": "OIL",
        "solas_application": "건조시 KEEL LAYING에 따른 SOLAS 요건 적용 (소급적용부분 적용, 소급적용에 대한 현행 규정 만족되어야 함)",
        "marpol_application": "개조시점의 MARPOL 규정 적용"
       },
       {
        "before": "CARGO SHIP",
        "after": "TANKER",
        "solas_application": "개조시점의 SOLAS 규정 적용",
        "marpol_application": "개조시점의 MARPOL 규정 적용"
       },
       {
        "before": "BULK",
        "after": "CONTAINER CARRIER",
        "solas_application": "톤수변경이 수반되지 않을 경우 추가요건만 개조시점의 규정적용(예, SOLAS Reg.II-2/54)",
        "marpol_application": "톤수변경이 수반되지 않을 경우 적용제외"
       },
       {
        "before": "OIL(FA)",
        "after": "OIL(FB)",
        "solas_application": "SOLAS Chapter II-2에 대한 요건은 개조시점의 규정 적용(특히 화물구역에 대한 요건)",
        "marpol_application": "톤수변경이 수반되지 않을 경우 적용제외"
       }
      ]
     }
    ]
   }
  ]
 },
 "area": {
  "제목": "선박의 항해구역별, 길이별 요건 비교(강선의구조기준, 선박복원성기준)",
  "요건비교": [
   {
    "항목": "1. 선수격벽 위치",
    "관련조항": "강선의구조기준 221조 & 689조",
    "평수": "- 90미터 미만 : 0.05Lf ~ 0.13Lf\n- 90미터 이상 : Min(0.05Lf,10) ~ Max(0.08Lf,0.05Lf+3)",
    "연해": "- 90미터 미만 : 0.05Lf ~ 0.13Lf\n- 90미터 이상 : Min(0.05Lf,10) ~ Max(0.08Lf,0.05Lf+3)",
    "근해": "- 총톤수 500톤 미만 : 0.05Lf ~ 0.13Lf\n- 90미터 미만 : 0.05Lf ~ 0.05Lf+3 m\n- 90미터 이상 : Min(0.05Lf,10) ~ Max(0.08Lf,0.05Lf+3)",
    "국제": "SOLAS II-1/12.1 : Min(0.05Lf,10) ~ Max(0.08Lf,0.05Lf+3)",
    "비고": null
   },
   {
    "항목": "2. 이중저구조",
    "관련조항": "강선의구조기준 92조 & 530조",
    "평수": "항해구역 상관없음\n'- 90미터 미만, 요건 없음\n- 90미터 이상, 설치",
    "연해": "항해구역 상관없음\n'- 90미터 미만, 요건 없음\n- 90미터 이상, 설치",
    "근해": "항해구역 상관없음\n'- 90미터 미만, 요건 없음\n- 90미터 이상, 설치",
    "국제": "- 90미터 미만 : 여객선 또는 500톤 이상 화물선\n- 90미터 이상 : 이중저 설치",
    "비고": null
   },
   {
    "항목": "3. 선루등의 설치",
    "관련조항": "강선의구조기준 284조",
    "평수": "- 60미터 미만 유탱커 면제\n- 유탱커 이외 선박 면제",
    "연해": "- 평수구역으로부터 최고속력 2시간 이내 왕복할 수 있는 구역 한정하여 운항하는 선박은 면제\n- 유탱커 이외 선박 면제",
    "근해": "- 유탱커 이외 선박으로, 길이 60미터 이하 면제",
    "국제": "ICLL 선수높이 만족",
    "비고": null
   },
   {
    "항목": "4. 선루단격벽의 출입구",
    "관련조항": "강선의구조기준 288조",
    "평수": "항해구역 상관없음, 380",
    "연해": "항해구역 상관없음, 380",
    "근해": "항해구역 상관없음, 380",
    "국제": "항해구역 상관없음, 380",
    "비고": null
   },
   {
    "항목": "5. 기관실의 출입구",
    "관련조항": "강선의구조기준 143조 & 331조의20",
    "평수": "항해구역 상관없음, Pos 1 : 600, Pos 2 : 380",
    "연해": "항해구역 상관없음, Pos 1 : 600, Pos 2 : 380",
    "근해": "항해구역 상관없음, Pos 1 : 600, Pos 2 : 380",
    "국제": "항해구역 상관없음, Pos 1 : 600, Pos 2 : 380",
    "비고": null
   },
   {
    "항목": "6. 승강구의 높이",
    "관련조항": "강선의구조기준 333조",
    "평수": "- 90미터 미만, Pos 1 : 150, Pos 2 : 100\n- 90미터 이상, Pos 1 : 300, Pos 2 : 100",
    "연해": "- 30미터 미만, Pos 1 : 300, Pos 2 : 150\n- 30미터 이상, Pos 1 : 450, Pos 2 : 300",
    "근해": "- Pos 1 : 600, Pos 2 : 380",
    "국제": "- Pos 1 : 600, Pos 2 : 380",
    "비고": null
   },
   {
    "항목": "7. 기타개구(갑판실 출입구)",
    "관련조항": "강선의구조기준 (?), ICLL 18(5)(6)",
    "평수": "- 강선의구조기준에는 해당요건 없음.\n- ICLL에 따르면, \n  상부갑판에서 출입 가능한 선교루/선미루 출입구 : 380\n  상부갑판에서 출입 불가능한 선교루/선미루/갑판실 출입구 : 600",
    "연해": "- 강선의구조기준에는 해당요건 없음.\n- ICLL에 따르면, \n  상부갑판에서 출입 가능한 선교루/선미루 출입구 : 380\n  상부갑판에서 출입 불가능한 선교루/선미루/갑판실 출입구 : 600",
    "근해": "- 강선의구조기준에는 해당요건 없음.\n- ICLL에 따르면, \n  상부갑판에서 출입 가능한 선교루/선미루 출입구 : 380\n  상부갑판에서 출입 불가능한 선교루/선미루/갑판실 출입구 : 600",
    "국제": "- 강선의구조기준에는 해당요건 없음.\n- ICLL에 따르면, \n  상부갑판에서 출입 가능한 선교루/선미루 출입구 : 380\n  상부갑판에서 출입 불가능한 선교루/선미루/갑판실 출입구 : 600",
    "비고": "ICLL 18(5)(6)요건에 대응하는 강선의 구조기준 조항 찾지못함. 상부갑판으로부터 출입이 되지 않으면 해당 구획의 갑판상 개구는 승강구가 되며, 333조의 승강구 요건과 같이 항해구역/선박길이별 완화 요건이 있어야 할 것으로 보임.\n강선의구조기준 개정?"
   },
   {
    "항목": "8. 창구코밍의 높이",
    "관련조항": "강선의구조기준 318조",
    "평수": "- 30미터 미만, Pos 1 : 300, Pos 2 : 150\n- 30미터 이상, Pos 1 : 450, Pos 2 : 300",
    "연해": "- 30미터 미만, Pos 1 : 450, Pos 2 : 300\n- 30미터 이상, Pos 1 : 600, Pos 2 : 450",
    "근해": "- Pos 1 : 600, Pos 2 : 450",
    "국제": "- Pos 1 : 600, Pos 2 : 450",
    "비고": null
   },
   {
    "항목": "9. 통풍통의 높이",
    "관련조항": "강선의구조기준 380조",
    "평수": "식에 따라 경감 가능",
    "연해": "- 30미터 미만, Pos 1 : 760, Pos 2 : 450\n- 30미터 이상, Pos 1 : 900, Pos 2 : 760",
    "근해": "- Pos 1 : 900, Pos 2 : 760",
    "국제": "- Pos 1 : 900, Pos 2 : 760",
    "비고": null
   },
   {
    "항목": "10. 공기관의 높이",
    "관련조항": "선박기관기준 120조",
    "평수": "항해구역 상관없음, TUG Boat Pos 1 : 450, Pos 2 :300",
    "연해": "항해구역 상관없음, TUG Boat Pos 1 : 450, Pos 2 :300",
    "근해": "항해구역 상관없음, TUG Boat Pos 1 : 450, Pos 2 :300",
    "국제": "항해구역 상관없음, TUG Boat Pos 1 : 450, Pos 2 :300",
    "비고": null
   },
   {
    "항목": "11. 현창",
    "관련조항": "강선의구조기준 377조",
    "평수": "별표4의 요건 적용",
    "연해": "별표3의 요건 적용",
    "근해": "불명확 함.",
    "국제": "ICLL 동일",
    "비고": "377조 8항의 \"국제항해에 종사하는\"을 삭제하여 길이 24미터 미만 선박을 모두 적용하도록 하고, 9항에 따라 연해, 평수 선박은 별표의 완화적용하도록 강선의구조기준을 개정해야 함."
   },
   {
    "항목": "12. 복원성",
    "관련조항": "선박복원성기준\n(항해구역 확대시, 해당 시점의 기준 적용함)",
    "평수": "- 여객선 : 국제기준과 동일\n  단, Weather Criteria 관련하여, \n      호소,하천,항만내 항해 여객선은 감소된 풍압 적용\n      연해이하 선박 횡요주기(Ts)에 따른 s값 완화\n      상갑판 상방의 현측을 현단으로 인정 가능\n  단, 일반복원성기준 중, GM과 GZ곡선면적 요건만 적용 \n- 화물선 : GM과 GZ곡선면적 요건만 적용\n- 특수선형선박 중 여객선의 경사우력정 계산인자 K : 1.71",
    "연해": "- 여객선 : 국제기준과 동일\n  단, Weather Criteria 관련하여 횡요주기(Ts)에 따른 s값\n      완화\n  단, 한정연해이거나 길이 24미터 미만은 일반복원성 기준 \n      중, GM과 GZ곡선면적 요건만 적용 \n- 화물선 : 평수와 동일\n- 특수선형선박 중 여객선의 경사우력정 계산인자 K 관련,     \n  한정연해 : 1.71, 연해 : 2.74",
    "근해": "- 여객선 : 국제기준과 동일 \n- 화물선 : 연해요건에서 θmax ≥ 25, GZ30 ≥ 20 추가되어\n              국제기준 중 Weather Criteria 만 제외됨.\n- 특수선형선박 중 여객선의 경사우력정 계산인자 K : 5.14",
    "국제": "- 여객선 : 일반복원성기준(GM, GZ곡선면적, θmax, GZ30), \n             Weather Criteria, 여객이동 및 선회시 횡경사 적용\n- 화물선 : 일반복원성기준(GM, GZ곡선면적, θmax, GZ30),\n             Weather Criteria",
    "비고": "국제연해이면, 선박복원성기준에서는 Ts에 따른 s값 완화 되지만, IS Code에서는 이러한 완화규정 없음. \n선박복원성기준 개정요청 ??"
   }
  ]
 }
};
