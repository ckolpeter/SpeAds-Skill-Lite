# SpeAds Skill Lite v1.0.0 — 简体中文

[← 返回主 README](../../README.md)

AI Ads Academy · https://www.ai-ads.academy · Apache-2.0

## 定位

免费、开源的站内广告离线规划 Skill。各平台模式、前提和带核查日期的官方资料列在 profile.json。



Modes: `full_site, comprehensive_search`

## 已包含功能

提供代表性订单贡献、盈亏平衡 CPA／净收入 ROAS、商品准备度、均分试投预算情景及用户报表分析。eBay 成交收费、GMV Max 混合归因和 Walmart Buy Box 分开处理。

## 快速开始

仅需 Python 3.10+ 标准库，在套件根目录运行。未知值保留 null；每次使用新的输出目录。CSV 必须先整理为附带的六列格式并提供 metadata，不支持任意原始平台导出文件。

```bash
python3 -m unittest discover -s tests -v
python3 scripts/release_gate.py
python3 scripts/toolkit.py plan examples/brief.synthetic.json --out-dir output/demo-plan
python3 scripts/toolkit.py validate output/demo-plan/plan.json
python3 scripts/toolkit.py analyze examples/report.csv --meta examples/report.meta.json --out-dir output/demo-analysis
python3 scripts/toolkit.py validate output/demo-analysis/analysis.json
```

## 限制与安全

不连接账号、不收集凭证、不抓取实时数据、不发布广告、不调整预算。金额只是情景，不是投放指令或会计意见。归因 GMV 不等于净利润，自然加付费 ROI 不等于付费广告增量。所有结果必须由人审核。

本版提供五种语言的入门说明，不代表完整多语言 CLI 或自动翻译引擎。确定性 JSON 字段保持固定；宿主模型可另写用户语言的解读。模型应用可能使用云服务并产生费用。桌面加载、选择与输出质量仍需实机验收。

请阅读数据契约、安装和开发交接文件。不要输入客户个人信息或真实凭证。本工具不是任何广告平台的官方产品。

[Data contract](../../references/data-contract.md) · [Install](../INSTALLATION.md) · [Development](../HANDOFF.md) · [Sources](../../references/official-sources.md)
