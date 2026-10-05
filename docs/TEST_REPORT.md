# v1.0.0 本地驗證記錄 — SpeAds Skill Lite

核對日期：2026-10-05。環境：Linux / Python 3.13.5。

| Gate | Result |
|---|---|
| Python unittest | 94 tests, PASS |
| JSON Schema (independent jsonschema Draft202012) | PASS: template brief, synthetic brief, synthetic report |
| Deterministic example replay / JSON+CSV parity | PASS, included in tests |
| No network calls under patched socket / no-overwrite / local installer | PASS, included in tests |
| Relative Markdown links | PASS: 43 links |
| SHA-256 release manifest | PASS after intentional documentation update; checked again before packaging |
| Codex / Claude Code actual discovery and model output | NOT_RUN |
| Native marketplace-export mapping / real seller dataset | NOT_RUN |
| Live account eligibility / ad publishing / performance | NOT_RUN, outside Lite |

完整本地測試輸出：[local-test-output.txt](local-test-output.txt)。以上為原始建置環境記錄；GitHub 端以該 commit 的實際 Actions 結果為準，不以這份文件代替 CI。工作流程會測 Python 3.10 / 3.13；未執行前不宣稱通過。

共用測試在各獨立套件內各自執行；六包的總數包含重複共用情境，不代表 564 種不同廣告能力。平台專屬模式及歸因／收費防護另有測試。靜態掃描及少量動態測試並非完整安全稽核、平台審核或多語自然語言品質驗證。

測試資料均為合成範例。此次沒有使用你的真實賣家報表、商品毛利或廣告憑證。
