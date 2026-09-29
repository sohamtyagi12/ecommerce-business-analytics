# Power BI / Tableau: how to complete this part

I can't run Tableau or Power BI directly (they're desktop apps, not something I can execute here), so I built the full analysis and data model in Excel with `data/orders.csv` as the single source of truth — the same file drops straight into either tool. To finish the CV story truthfully, do this once (15–20 min):

## Power BI (or Tableau) steps

1. Open Power BI Desktop → Get Data → Text/CSV → `data/orders.csv`.
2. Build these visuals (matches the Excel tabs, so the story is consistent):
   - Line chart: `revenue` by `order_date` (month) → Monthly Trend
   - Pie/donut: `revenue` by `category` → Category Breakdown
   - Bar chart: `revenue` by `region` → Region Breakdown
   - Table + scatter: `customer_id` ranked by total revenue, with a cumulative % line → Pareto/Customer Segmentation
   - Slicers: `segment`, `region`, `category`
3. Add 2 KPI cards: total revenue, and "% revenue from top 20% of customers."
4. Save as `.pbix` and export a screenshot (or a published Power BI Service link) for the repo.

## Why this matters for your CV

List Power BI/Tableau only once you've actually clicked through building this — the bullet point should say something you can screen-share and rebuild live in an interview. Once you've built it, add the `.pbix`/`.twbx` file (or a link + screenshot) to this repo and update the README's "Tools used" section to link it.
