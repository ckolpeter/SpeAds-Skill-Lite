"""Shopee Taiwan input scope and daily delivery regressions."""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import toolkit as t


class SpendDiagnosticsTests(unittest.TestCase):
    def setUp(self):
        self.data = t.read_json(ROOT / 'examples/report.delivery.synthetic.json')
        self.diagnostics = self.data['spend_diagnostics']

    def results(self):
        return t.build(self.data, 'report')['result']['spend_diagnostics']['rows']

    def test_rejects_wrong_site_and_currency_for_all_input_paths(self):
        examples = ROOT / 'examples'
        for field, value in [('market', 'SG'), ('currency', 'USD')]:
            for kind, data in [
                ('brief', t.read_json(examples / 'brief.synthetic.json')),
                ('report', t.read_json(examples / 'report.synthetic.json')),
                ('report', t.read_csv(examples / 'report.csv', t.read_json(examples / 'report.meta.json'))),
            ]:
                with self.subTest(field=field, kind=kind), self.assertRaisesRegex(t.InputError, field):
                    t.build(dict(data, **{field: value}), kind)

    def test_three_synthetic_cases_and_replay(self):
        zero, low, down = self.results()
        self.assertEqual(zero['signals'], ['NO_AD_IMPRESSIONS'])
        self.assertEqual(low['signals'], ['LOW_BUDGET_UTILIZATION'])
        self.assertEqual(low['after']['budget_utilization'], '0.100000')
        self.assertEqual(down['signals'], ['ORGANIC_AND_AD_TRAFFIC_DOWN'])
        self.assertEqual(down['change_after_minus_before'], {
            'organic_visits': '-135.000000',
            'ad_impressions': '-950.000000',
            'spend': '-80.000000',
            'budget': '0.000000',
            'budget_utilization': '-0.400000',
        })
        self.assertTrue(all(not row['missing'] for row in (zero, low, down)))
        artifact = t.build(self.data, 'report')
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'delivery'
            t.write_output(artifact, path)
            self.assertEqual(t.validate_artifact(t.read_json(path / 'analysis.json')), artifact)
            self.assertIn('LOW_BUDGET_UTILIZATION', (path / 'report.md').read_text(encoding='utf-8'))
        artifact['result']['spend_diagnostics']['rows'][0]['signals'] = []
        with self.assertRaisesRegex(t.InputError, 'replay mismatch'):
            t.validate_artifact(artifact)

    def test_missing_field_and_date_are_not_treated_as_zero(self):
        daily = self.diagnostics['series'][0]['daily']
        daily.pop()
        daily[-1]['organic_visits'] = None
        row = self.results()[0]
        self.assertEqual(row['signals'], [])
        self.assertEqual(row['missing'], ['after.daily: 1 date(s) missing', 'after.organic_visits'])
        self.assertIsNone(row['after']['budget_utilization'])
        self.assertIsNone(row['change_after_minus_before']['ad_impressions'])

    def test_missing_threshold_and_zero_budget(self):
        self.diagnostics.pop('low_utilization_threshold')
        self.assertEqual(self.results()[1]['missing'], ['low_utilization_threshold'])
        for day in self.diagnostics['series'][1]['daily']:
            day['budget'] = 0
        row = self.results()[1]
        self.assertEqual(row['signals'], ['NO_POSITIVE_BUDGET'])
        self.assertIsNone(row['after']['budget_utilization'])

    def test_ignores_change_day_and_extra_unmatched_day(self):
        self.data['end_date'] = '2026-09-06'
        series = self.diagnostics['series'][0]
        for date in ('2026-09-03', '2026-09-06'):
            series['daily'].append(dict(series['daily'][0], date=date))
        row = self.results()[0]
        self.assertEqual(row['signals'], ['NO_AD_IMPRESSIONS'])
        self.assertEqual(row['before']['end_date'], '2026-09-02')
        self.assertEqual(row['after']['end_date'], '2026-09-05')

    def test_missing_series_and_change_date(self):
        series = self.diagnostics['series']
        series[0].pop('change_date')
        series.pop()
        first, _, last = self.results()
        self.assertIn('change_date', first['missing'])
        self.assertIsNotNone(first['report_window'])
        self.assertIsNone(first['before'])
        self.assertEqual(last['missing'], ['daily series'])

    def test_rejects_duplicate_date_unmatched_sku_and_outside_dates(self):
        series = self.diagnostics['series'][0]
        daily = series['daily']
        daily.append(daily[0].copy())
        with self.assertRaisesRegex(t.InputError, 'Duplicate daily'):
            self.results()
        daily[-1]['date'] = '2026-09-06'
        with self.assertRaisesRegex(t.InputError, 'outside report'):
            self.results()
        daily.pop()
        series['sku'] = 'unknown-sku'
        with self.assertRaisesRegex(t.InputError, 'match a report row'):
            self.results()

    def test_csv_metadata_parity(self):
        examples = ROOT / 'examples'
        report = t.read_json(examples / 'report.synthetic.json')
        diagnostics = {'series': [{'sku': report['rows'][0]['sku'], 'daily': []}]}
        report['spend_diagnostics'] = diagnostics
        meta = t.read_json(examples / 'report.meta.json')
        meta['spend_diagnostics'] = diagnostics
        csv_data = t.read_csv(examples / 'report.csv', meta)
        self.assertEqual(t.build(csv_data, 'report'), t.build(report, 'report'))
