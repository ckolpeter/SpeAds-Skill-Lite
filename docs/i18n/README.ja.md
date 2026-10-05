# SpeAds Skill Lite v1.0.0 — 日本語

[← メイン README に戻る](../../README.md)

AI Ads Academy · https://www.ai-ads.academy · Apache-2.0

## 概要

マーケットプレイス広告をオフラインで企画する、無料のオープンソース Skill です。プラットフォーム別のモード、前提条件、確認日付きの公式資料は profile.json にあります。



Modes: `full_site, comprehensive_search`

## 含まれる機能

代表的な注文の限界利益、損益分岐 CPA／純収入ベース ROAS、商品準備状況、均等配分の試験予算、および提供データの分析を行います。eBay の売上ベース料金、GMV Max の混合アトリビューション、Walmart の Buy Box を区別します。

## クイックスタート

Python 3.10+ の標準ライブラリのみを使用します。パッケージ直下で実行し、不明値は null のままにしてください。実行ごとに新しい出力フォルダーが必要です。CSV は付属の6列形式とメタデータが必要で、任意のプラットフォーム出力には対応しません。

```bash
python3 -m unittest discover -s tests -v
python3 scripts/release_gate.py
python3 scripts/toolkit.py plan examples/brief.synthetic.json --out-dir output/demo-plan
python3 scripts/toolkit.py validate output/demo-plan/plan.json
python3 scripts/toolkit.py analyze examples/report.csv --meta examples/report.meta.json --out-dir output/demo-analysis
python3 scripts/toolkit.py validate output/demo-analysis/analysis.json
```

## 制限と安全性

アカウント接続、認証情報の収集、リアルタイムデータ取得、広告公開、予算変更は行いません。計算値はシナリオであり、投資・会計上の助言ではありません。帰属 GMV は純利益ではなく、自然流入を含む ROI は広告の増分効果ではありません。人による確認が必須です。

5言語の入門ドキュメントを提供しますが、CLI 全体の多言語化や自動翻訳エンジンではありません。決定的な JSON は変更せず、ホストモデルで別の解説を作成できます。ホストアプリがクラウドや有料サービスを使用する場合があります。デスクトップでの検出・選択・出力品質は実機検証が必要です。

データ契約、インストール手順、開発引き継ぎ資料を確認してください。個人情報や認証情報を入力しないでください。広告プラットフォームの公式製品ではありません。

[Data contract](../../references/data-contract.md) · [Install](../INSTALLATION.md) · [Development](../HANDOFF.md) · [Sources](../../references/official-sources.md)
