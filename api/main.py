from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "NeuralRetail API Running"}

@app.get("/predict/churn")
def predict_churn():

    return {
        "customer_id": 101,
        "churn_score": round(random.uniform(0, 1), 2)
    }

@app.get("/predict/demand")
def predict_demand():

    return {
        "sku": "SKU-001",
        "predicted_demand": random.randint(100, 500)
    }