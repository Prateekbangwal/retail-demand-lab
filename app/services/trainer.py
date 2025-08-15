import os

import joblib
import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_absolute_percentage_error, r2_score
from sklearn.model_selection import train_test_split


def train_model(df: pd.DataFrame, target: str = "demand"):
    # required feature columns
    feature_cols = ["price", "promo_flag", "lag_demand_1", "rolling_mean_4", "month"]

    # basic validations
    missing = [c for c in feature_cols + [target] if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # drop rows with NA across features + target (common after lags/rollings)
    df_clean = df[feature_cols + [target]].dropna().reset_index(drop=True)

    if len(df_clean) < 10:
        raise ValueError("Not enough rows after feature generation and NA drop.")

    X = df_clean[feature_cols]
    y = df_clean[target]

    # correct order: X_train, X_test, y_train, y_test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # quick shape guards
    assert len(X_train) == len(y_train)
    assert len(X_test) == len(y_test)

    # model
    model = ElasticNet(random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    # NOTE: if y_test can contain zeros, MAPE can be problematic.
    # For now we keep your metric; consider a "safe MAPE" later.
    metrics = {
        "r2": r2_score(y_test, preds),
        "mape": mean_absolute_percentage_error(y_test, preds),
    }

    # ensure models directory exists, then save
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/elasticnet.pkl")

    return metrics
