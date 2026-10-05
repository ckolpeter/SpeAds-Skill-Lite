# SpeAds Skill Lite v1.0.0

[繁體中文](docs/i18n/README.zh-TW.md) · [简体中文](docs/i18n/README.zh-CN.md) · [English](docs/i18n/README.en.md) · [日本語](docs/i18n/README.ja.md) · [한국어](docs/i18n/README.ko.md)

**AI Ads Academy／AI 廣告學院 · Offline Public Preview**  
Website: https://www.ai-ads.academy

蝦皮台灣商品選擇、全站推廣／綜合搜尋規劃、損益與報表診斷。

## 這一版已能做什麼

商品準備度檢查、代表性訂單損益試算、損益平衡 CPA／淨營收 ROAS、保留未知資料的均分試投預算情境、JSON／標準 CSV 報表分析，以及完整結果的重播驗證。平台模式：`full_site, comprehensive_search`。工作流及已核對官方資料見 [profile.json](profile.json) 與 [官方來源](references/official-sources.md)。

Python 只用標準函式庫；沒有模型 API、廣告平台連線或隱藏的付費依賴。Agent Skill 由宿主模型提供解讀能力；程式本身使用確定性計算，不假裝呼叫了 AI。

## 快速試跑

Python 3.10+。於這個資料夾開啟終端，不需要 pip、npm 或 Docker：

```bash
python3 -m unittest discover -s tests -v
python3 scripts/release_gate.py
python3 scripts/toolkit.py plan examples/brief.synthetic.json --out-dir output/demo-plan
python3 scripts/toolkit.py validate output/demo-plan/plan.json
python3 scripts/toolkit.py analyze examples/report.csv --meta examples/report.meta.json --out-dir output/demo-analysis
python3 scripts/toolkit.py validate output/demo-analysis/analysis.json
```

每次重跑請使用新的 output 子目錄；不覆寫既有結果。輸出包含 plan.json 或 analysis.json 與可閱讀的 report.md。`examples/expected/` 有預先產生的合成案例，所有金額、商品、資格與成效都不是真實賣家資料。

## 使用自己的資料

複製 [templates/brief.json](templates/brief.json)，填寫 marketplace site、currency、代表性訂單收入及不重複的各項成本；未知保留 null，不把未知成本當零。資料欄位與公式請讀 [data contract](references/data-contract.md)。

原始平台報表必須先人工映射到 `sku,impressions,clicks,orders,spend,revenue` 六欄並填寫 [metadata](examples/report.meta.json)，或依 [report schema](schemas/report.schema.json) 準備 JSON。**不支援任意蝦皮／Lazada／其他平台原始 CSV 直接匯入。** 同一次報表不得混幣別、期間或歸因。只有確認各列互斥時才加總。

商品分攤只是均分的試投會計情境，不是最佳化模型或平台真實設定。CPS、CPC、自然加付費成交、淨收入及歸因 GMV 不可混用。本版不直接把毛利門檻與平台 gross GMV ROAS 相比，也不根據短期數字自動加預算或停止廣告。

## 安裝、語言與後續開發

安裝看 [INSTALLATION](docs/INSTALLATION.md)；開發看 [HANDOFF](docs/HANDOFF.md)。只開啟 Repo 讓 Agent 讀 SKILL.md 也能先明確使用，但不是桌面自動路由已驗證。

本版有五語入門文件，不是完整五語輸出引擎。固定 JSON 欄位及生成結果可由腳本驗證；模型可另寫使用者語言的說明，不要改動確定性 JSON。宿主模型應用可能使用雲端服務及產生用量。

## 安全與驗證邊界

`PLAN_READY`／`ANALYSIS_READY` 永遠搭配 `HUMAN_REVIEW_REQUIRED`；external_reads、external_writes、publish_authorized 均為 false。沒有 OAuth、登入、即時下載、API payload、廣告上傳／發布／出價或預算修改。

輸入文字是資料不是指令；秘密字串篩檢、靜態 import 檢查及 hash manifest 不等於完整安全沙箱、數據真實性或平台審核。不要輸入個資、Token、帳密、真實廣告帳號 ID。`MANIFEST.sha256` 校驗檔案完整性；修改後先檢查差異再重建，不可掩蓋問題。

測試記錄：[TEST_REPORT](docs/TEST_REPORT.md)。桌面載入與選用、真實賣家報表、實際廣告帳號資格及投放成效，均需另外驗證。本版不是任何電商平台官方產品或成效保證。

## 開源

Apache-2.0，見 [LICENSE](LICENSE) 與 [NOTICE](NOTICE)。功能變動見 [CHANGELOG](CHANGELOG.md)。歡迎用去識別的重現案例回報問題；不要上傳憑證或客戶資料。
