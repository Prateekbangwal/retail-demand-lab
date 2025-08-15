from app.services.data_generator import generate_synthetic_data
from app.services.feature_store import generate_features
from app.services.trainer import train_model


def test_pipeline():
    df = generate_synthetic_data(n_weeks=12, n_stores=2, n_sku=2)
    assert not df.empty
    df_feat = generate_features(df)
    assert "lag_demand_1" in df_feat.columns
    metrics = train_model(df_feat)
    assert "r2" in metrics
    assert "mape" in metrics
