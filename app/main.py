from fastapi import FastAPI

from app.api import routes_health, routes_train  # import the new train route module

app = FastAPI(title="Retail Demand & Promotions Lab")

# Include routers
app.include_router(routes_health.router)
app.include_router(routes_train.router)  # now /train will be available


# Root route
@app.get("/")
def root():
    return {"message": "Retail Demand & Promotions Lab API"}
