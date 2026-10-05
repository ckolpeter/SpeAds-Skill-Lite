# SpeAds Skill Lite v1.0.0 — 繁體中文

[← 回主 README](../../README.md)

AI Ads Academy · https://www.ai-ads.academy · Apache-2.0

## 定位

免費、開源的站內廣告離線規劃 Skill。各平台的模式、前提及具核對日期的官方資料，列在 profile.json。

蝦皮台灣商品選擇、全站推廣／綜合搜尋規劃、損益與報表診斷

Modes: `full_site, comprehensive_search`

## 已包含功能

提供代表性訂單貢獻、損益平衡 CPA／淨營收 ROAS、商品準備度、均分試投預算情境與使用者報表分析。eBay 成交費率、GMV Max 混合歸因、Walmart Buy Box 分開處理。

## 快速開始

只需 Python 3.10+ 標準函式庫，於套件根目錄執行。未知值保持 null；每次使用新輸出目錄。CSV 必須先整理為所附六欄格式並提供 metadata，不是任意平台原始報表都能直接匯入。

```bash
python3 -m unittest discover -s tests -v
python3 scripts/release_gate.py
python3 scripts/toolkit.py plan examples/brief.synthetic.json --out-dir output/demo-plan
python3 scripts/toolkit.py validate output/demo-plan/plan.json
python3 scripts/toolkit.py analyze examples/report.csv --meta examples/report.meta.json --out-dir output/demo-analysis
python3 scripts/toolkit.py validate output/demo-analysis/analysis.json
```

## 限制與安全

不連帳號、不收憑證、不抓即時資料、不發布廣告、不改預算。金額只是情境，不是投放指令或會計意見。歸因 GMV 不等於淨利，自然加付費 ROI 不等於付費廣告增量。所有結果都需人工審查。

本版提供五語入門說明，不代表完整多語 CLI 或自動翻譯引擎。確定性 JSON 保持固定欄位；承載模型可另寫使用者語言的解讀文件。模型應用本身可能上雲及產生費用。桌面載入、正確選用與輸出品質仍需實機驗收。

請閱讀資料契約、安裝與開發交接文件。不輸入客戶個資及真實憑證。本工具非任何廣告平台官方產品。

[Data contract](../../references/data-contract.md) · [Install](../INSTALLATION.md) · [Development](../HANDOFF.md) · [Sources](../../references/official-sources.md)
