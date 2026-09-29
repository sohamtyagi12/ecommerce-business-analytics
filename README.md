# E-Commerce Business Analytics Dashboard

End-to-end business analysis of a synthetic mid-size D2C retailer's FY2025 order data (6,000 orders, 1,380 customers), built to demonstrate business analyst / product analyst skills: data modeling, KPI definition, customer segmentation, and executive-ready reporting.

## What's in here

- `data/orders.csv` — order-level transaction data (order id, date, customer, category, region, segment, price, quantity, revenue)
- `generate_data.py` — reproducible data generation script (synthetic but realistic seasonality and customer-value patterns)
- `Ecommerce_Business_Analytics.xlsx` — the analysis workbook:
  - **Insights & Recommendations** — executive summary of findings
  - **Raw Data** — full transaction log
  - **Monthly Trend** — revenue/order trend with a native line chart
  - **Category Breakdown** — revenue by category with a pie chart
  - **Region Breakdown** — revenue by region with a bar chart
  - **Customer Segmentation** — Pareto/concentration analysis across all 1,380 customers
- `build_workbook.py` — script that builds the workbook from the CSV (all summary tables use live `SUMIFS`/`COUNTIFS` formulas, so the workbook recalculates if the underlying data changes)
- `tableau_powerbi_notes.md` — how the same dataset was modeled as a Tableau/Power BI dashboard (screenshots + `.twbx`/`.pbix` if included)

## Key findings

1. The top 20% of customers (276 of 1,380) generate **50.2%** of total revenue — a clear Pareto pattern.
2. **Electronics** is the top revenue-generating category; **South** is the top-revenue region.
3. **VIP** customers are 15% of the base but drive **23.8%** of revenue.
4. **Q4** (Oct–Dec) accounts for **29.7%** of annual revenue — a strong seasonal spike.

## Recommendations

- Launch a VIP retention program given their outsized revenue contribution.
- Increase inventory/marketing spend ahead of Q4 to capture the seasonal spike.
- Run a win-back/onboarding campaign for the "New" segment to lift long-term value.
- Concentrate marketing spend on the top-performing category and region while testing smaller campaigns elsewhere.

## Tools used

Excel (data modeling, `SUMIFS`/`COUNTIFS`, pivot-style summary tables, native charts), Python/pandas (data generation and validation), and the same model rebuilt in Power BI / Tableau for interactive filtering (see `tableau_powerbi_notes.md`).

## How to reproduce

```bash
python generate_data.py      # regenerates data/orders.csv
python build_workbook.py     # rebuilds the Excel workbook from the CSV
```
