from fastapi import APIRouter

from app.services.data_generator import generate_synthetic_data
from app.services.feature_store import generate_features
from app.services.trainer import train_model

router = APIRouter()


@router.post("/train")
def train_endpoint():
    df = generate_synthetic_data()
    df_feat = generate_features(df)
    metrics = train_model(df_feat)
    return {"status": "success", "metrics": metrics}
