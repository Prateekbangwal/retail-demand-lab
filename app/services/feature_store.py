def generate_features(df):
    df = df.copy()
    df["lag_demand_1"] = df.groupby(["store_id", "sku_id"])["demand"].shift(1)
    df["rolling_mean_4"] = df.groupby(["store_id", "sku_id"])["demand"].transform(
        lambda x: x.rolling(4).mean()
    )
    df["month"] = df["week"].dt.month
    df = df.dropna()
    return df
