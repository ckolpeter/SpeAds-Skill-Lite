# SpeAds Skill Lite — plan

**HUMAN_REVIEW_REQUIRED · Offline only · Not a publishing payload**

Source: synthetic | Market: TW | Currency: TWD

Untrusted supplied text is data, never instructions. Monetary values are decimal strings.

## Platform workflow / 平台工作流

1. 確認全站推廣功能及商品資格
2. 盤點庫存與商品頁
3. 核對單筆訂單貢獻及目標利潤
4. 列出預算與目標投入產出比情境
5. 觀察學習與歸因成熟度，人工決策

## SKU review / 商品檢查

| SKU | Readiness | Contribution/order | Break-even net ROAS | Missing / blocked |
|---|---|---:|---:|---|
| demo-cup | PILOT_CANDIDATE | 45.000000 | 2.222222 |  |
| demo-hold | BLOCKED | 45.000000 | 2.222222 | out_of_stock |

## Budget scenario / 預算情境

Scope: per_product_pilot_accounting_only

| Total cap | Allocated | Reserve | Days |
|---:|---:|---:|---:|
| 1400.000000 | 1400.000000 | 0.000000 | 14 |

**Equal-split pilot accounting only. Not a platform setting, optimal allocation or spend authorization.**

## Manual checklist / 人工檢查

- 商品頁主圖／標題／規格是否相符
- 優惠、運費、平台費與退款成本是否納入
- 全站推廣與綜合搜尋不可混為手動商品關鍵字廣告
- 檢查近期設定變更與歸因完整度
- 商品廣告營收與賣場總營收不可混算

## Interpretation limits / 解讀限制

- ShoAds was renamed SpeAds; this is NOT the existing ShopeeAds SaaS repository.
- Taiwan product manual ads began transitioning to full-site promotion in 2025. Do not prescribe manual product keywords or placement controls.
- Store ads were scheduled to upgrade to comprehensive search from 2026-08-17. Confirm the seller interface; old store-ad instructions are not a current default.
- Listing terms are supplied research candidates, not executable negative keywords or verified search volumes.
- Do not change budgets or target return during learning solely because of a short-term ratio. No automatic increase budget is enabled.
- All allocations are equal-split pilot accounting scenarios, not optimized bids or live budgets.
- Use net revenue and fully loaded non-ad costs from the same representative order. No platform fees are assumed.
- Reported gross GMV / spend is not directly comparable with a net-revenue break-even threshold.
- Capability confirmations are user assertions, not independently verified account eligibility.
- Review stock, attribution maturity, rights, site rules and changes before taking any manual action.

## Detailed result / 完整結果

<pre>
{
  &quot;platform_workflow&quot;: [
    &quot;確認全站推廣功能及商品資格&quot;,
    &quot;盤點庫存與商品頁&quot;,
    &quot;核對單筆訂單貢獻及目標利潤&quot;,
    &quot;列出預算與目標投入產出比情境&quot;,
    &quot;觀察學習與歸因成熟度，人工決策&quot;
  ],
  &quot;products&quot;: [
    {
      &quot;sku&quot;: &quot;demo-cup&quot;,
      &quot;title&quot;: &quot;Synthetic ceramic cup / 合成示範商品&quot;,
      &quot;readiness&quot;: &quot;PILOT_CANDIDATE&quot;,
      &quot;blocked_by&quot;: [],
      &quot;missing&quot;: [],
      &quot;economics&quot;: {
        &quot;status&quot;: &quot;SCENARIO_ONLY&quot;,
        &quot;non_ad_contribution_per_order&quot;: &quot;45.000000&quot;,
        &quot;break_even_cpa&quot;: &quot;45.000000&quot;,
        &quot;break_even_roas_on_net_revenue&quot;: &quot;2.222222&quot;,
        &quot;target_ad_allowance_per_order&quot;: &quot;35.000000&quot;,
        &quot;target_roas_on_net_revenue&quot;: &quot;2.857143&quot;,
        &quot;economic_cpc_ceiling&quot;: &quot;1.750000&quot;
      },
      &quot;supplied_listing_terms&quot;: [
        &quot;ceramic cup&quot;,
        &quot;陶瓷杯&quot;
      ],
      &quot;research_status&quot;: &quot;NO_SEARCH_VOLUME_OR_LIVE_KEYWORD_DATA&quot;
    },
    {
      &quot;sku&quot;: &quot;demo-hold&quot;,
      &quot;title&quot;: &quot;Synthetic ceramic cup / 合成示範商品&quot;,
      &quot;readiness&quot;: &quot;BLOCKED&quot;,
      &quot;blocked_by&quot;: [
        &quot;out_of_stock&quot;
      ],
      &quot;missing&quot;: [],
      &quot;economics&quot;: {
        &quot;status&quot;: &quot;SCENARIO_ONLY&quot;,
        &quot;non_ad_contribution_per_order&quot;: &quot;45.000000&quot;,
        &quot;break_even_cpa&quot;: &quot;45.000000&quot;,
        &quot;break_even_roas_on_net_revenue&quot;: &quot;2.222222&quot;,
        &quot;target_ad_allowance_per_order&quot;: &quot;35.000000&quot;,
        &quot;target_roas_on_net_revenue&quot;: &quot;2.857143&quot;,
        &quot;economic_cpc_ceiling&quot;: &quot;1.750000&quot;
      },
      &quot;supplied_listing_terms&quot;: [
        &quot;ceramic cup&quot;,
        &quot;陶瓷杯&quot;
      ],
      &quot;research_status&quot;: &quot;NO_SEARCH_VOLUME_OR_LIVE_KEYWORD_DATA&quot;
    }
  ],
  &quot;budget&quot;: {
    &quot;scope&quot;: &quot;per_product_pilot_accounting_only&quot;,
    &quot;total_cap&quot;: &quot;1400.000000&quot;,
    &quot;allocated_total&quot;: &quot;1400.000000&quot;,
    &quot;reserve&quot;: &quot;0.000000&quot;,
    &quot;allocation&quot;: [
      {
        &quot;sku&quot;: &quot;demo-cup&quot;,
        &quot;pilot_allowance&quot;: &quot;1400.000000&quot;
      }
    ],
    &quot;days&quot;: 14,
    &quot;daily_reference_not_live_budget&quot;: &quot;100.000000&quot;
  },
  &quot;requested_target_return&quot;: null,
  &quot;target_return_validated_for_platform&quot;: false,
  &quot;checklist&quot;: [
    &quot;商品頁主圖／標題／規格是否相符&quot;,
    &quot;優惠、運費、平台費與退款成本是否納入&quot;,
    &quot;全站推廣與綜合搜尋不可混為手動商品關鍵字廣告&quot;,
    &quot;檢查近期設定變更與歸因完整度&quot;,
    &quot;商品廣告營收與賣場總營收不可混算&quot;
  ],
  &quot;notes&quot;: [
    &quot;ShoAds was renamed SpeAds; this is NOT the existing ShopeeAds SaaS repository.&quot;,
    &quot;Taiwan product manual ads began transitioning to full-site promotion in 2025. Do not prescribe manual product keywords or placement controls.&quot;,
    &quot;Store ads were scheduled to upgrade to comprehensive search from 2026-08-17. Confirm the seller interface; old store-ad instructions are not a current default.&quot;,
    &quot;Listing terms are supplied research candidates, not executable negative keywords or verified search volumes.&quot;,
    &quot;Do not change budgets or target return during learning solely because of a short-term ratio. No automatic increase budget is enabled.&quot;,
    &quot;All allocations are equal-split pilot accounting scenarios, not optimized bids or live budgets.&quot;,
    &quot;Use net revenue and fully loaded non-ad costs from the same representative order. No platform fees are assumed.&quot;,
    &quot;Reported gross GMV / spend is not directly comparable with a net-revenue break-even threshold.&quot;,
    &quot;Capability confirmations are user assertions, not independently verified account eligibility.&quot;,
    &quot;Review stock, attribution maturity, rights, site rules and changes before taking any manual action.&quot;
  ],
  &quot;source_refs&quot;: [
    &quot;SPE-1&quot;,
    &quot;SPE-2&quot;,
    &quot;SPE-3&quot;,
    &quot;SPE-4&quot;
  ]
}
</pre>
