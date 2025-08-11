from fastapi import FastAPI

from app.api import routes_health

app = FastAPI(title="Retail Demand & Promotions Lab")

# Include health router
app.include_router(routes_health.router)


# Root route
@app.get("/")
def root():
    return {"message": "Retail Demand & Promotions Lab API"}
