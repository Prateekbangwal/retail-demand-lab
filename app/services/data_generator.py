import numpy as np
import pandas as pd


def generate_synthetic_data(n_weeks=52, n_sku=5, n_stores=10, seed=42):
    np.random.seed(seed)
    weeks = pd.date_range(start="2022-01-03", periods=n_weeks, freq="W-MON")
    data = []
    for store in range(1, n_stores + 1):
        for sku in range(1, n_sku + 1):
            base_demand = np.random.randint(50, 200)
            price = np.random.uniform(5, 15)
            for week in weeks:
                promo_flag = np.random.binomial(1, 0.3)
                seasonality = 10 * np.sin(2 * np.pi * week.month / 12)
                noise = np.random.normal(0, 5)
                demand = base_demand + seasonality - 2 * price + promo_flag * 15 + noise
                data.append(
                    [week, store, sku, round(price, 2), promo_flag, max(0, round(demand, 2))]
                )

    df = pd.DataFrame(data, columns=["week", "store_id", "sku_id", "price", "promo_flag", "demand"])
    df = df.reset_index(drop=True)
    # print(df)
    return df


# generate_synthetic_data(n_weeks = 52, n_sku =5, n_stores=10, seed = 42)
