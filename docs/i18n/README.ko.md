# SpeAds Skill Lite v1.0.0 — 한국어

[← 메인 README로 돌아가기](../../README.md)

AI Ads Academy · https://www.ai-ads.academy · Apache-2.0

## 개요

마켓플레이스 광고를 오프라인으로 기획하는 무료 오픈소스 Skill입니다. 플랫폼별 모드, 조건 및 확인 날짜가 있는 공식 자료는 profile.json에 있습니다.



Modes: `full_site, comprehensive_search`

## 포함된 기능

대표 주문의 공헌이익, 손익분기 CPA/순매출 기준 ROAS, 상품 준비 상태, 균등 분배 시험 예산 및 제공된 보고서 분석을 지원합니다. eBay 매출 기반 수수료, GMV Max 혼합 기여도, Walmart Buy Box를 구분합니다.

## 빠른 시작

Python 3.10+ 표준 라이브러리만 필요합니다. 패키지 루트에서 실행하고 알 수 없는 값은 null로 유지하세요. 매번 새 출력 폴더를 사용하세요. CSV는 제공된 6열 형식과 메타데이터가 필요하며 임의의 플랫폼 원본 내보내기는 지원하지 않습니다.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/release_gate.py
python3 scripts/toolkit.py plan examples/brief.synthetic.json --out-dir output/demo-plan
python3 scripts/toolkit.py validate output/demo-plan/plan.json
python3 scripts/toolkit.py analyze examples/report.csv --meta examples/report.meta.json --out-dir output/demo-analysis
python3 scripts/toolkit.py validate output/demo-analysis/analysis.json
```

## 제한 및 안전

계정 연결, 자격 증명 수집, 실시간 데이터 조회, 광고 게시 또는 예산 변경을 하지 않습니다. 계산은 시나리오이며 광고 실행 지시나 회계 조언이 아닙니다. 기여 GMV는 순이익이 아니며 자연 유입을 포함한 ROI는 유료 광고의 증분 효과가 아닙니다. 사람의 검토가 필요합니다.

5개 언어의 입문 문서를 제공하지만 완전한 다국어 CLI나 자동 번역 엔진은 아닙니다. 결정적 JSON은 유지하고 호스트 모델이 별도 해설을 작성할 수 있습니다. 호스트 앱은 클라우드를 사용하거나 요금을 발생시킬 수 있습니다. 데스크톱 검색, 선택 및 출력 품질은 실제 환경에서 검증해야 합니다.

데이터 계약, 설치 안내 및 개발 인수인계 문서를 읽으세요. 개인정보나 실제 자격 증명을 입력하지 마세요. 광고 플랫폼의 공식 제품이 아닙니다.

[Data contract](../../references/data-contract.md) · [Install](../INSTALLATION.md) · [Development](../HANDOFF.md) · [Sources](../../references/official-sources.md)
