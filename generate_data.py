import pandas as pd
import numpy as np

np.random.seed(42)

n = 6000
start = pd.Timestamp("2025-01-01")
end = pd.Timestamp("2025-12-31")
dates = pd.to_datetime(np.random.randint(start.value, end.value, n))

categories = ["Electronics", "Apparel", "Home & Kitchen", "Beauty", "Sports", "Books"]
cat_weights = [0.22, 0.24, 0.18, 0.15, 0.12, 0.09]
regions = ["North", "South", "East", "West"]
segments = ["New", "Returning", "VIP"]
seg_weights = [0.45, 0.40, 0.15]

n_customers = 1400
customer_ids = np.random.choice(range(1, n_customers + 1), n)

df = pd.DataFrame({
    "order_id": range(10001, 10001 + n),
    "order_date": dates,
    "customer_id": customer_ids,
    "category": np.random.choice(categories, n, p=cat_weights),
    "region": np.random.choice(regions, n),
    "segment": np.random.choice(segments, n, p=seg_weights),
})

# price ranges per category
price_map = {
    "Electronics": (1200, 45000),
    "Apparel": (400, 4500),
    "Home & Kitchen": (300, 8000),
    "Beauty": (150, 3000),
    "Sports": (300, 6000),
    "Books": (150, 1200),
}
unit_price = df["category"].map(lambda c: np.random.uniform(*price_map[c]))
df["unit_price"] = unit_price.round(2)
df["quantity"] = np.random.choice([1, 1, 1, 2, 2, 3], n)

# VIP customers spend more, returning less than VIP, new least
seg_multiplier = df["segment"].map({"New": 0.85, "Returning": 1.0, "VIP": 1.6})
df["revenue"] = (df["unit_price"] * df["quantity"] * seg_multiplier).round(2)

# add mild seasonality: boost Oct-Dec (festive/holiday)
month = df["order_date"].dt.month
season_boost = month.isin([10, 11, 12]).map({True: 1.25, False: 1.0})
df["revenue"] = (df["revenue"] * season_boost).round(2)

df = df.sort_values("order_date").reset_index(drop=True)
df.to_csv("/home/claude/ecommerce-business-analytics/data/orders.csv", index=False)
print(df.shape)
print(df.head())
