from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pickle
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
with open("models/house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

class HouseInput(BaseModel):
    area_sqft: float
    bedrooms: int
    bathrooms: int
    location_score: int

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict_price(data: HouseInput):
    features = np.array([[ 
        data.area_sqft,
        data.bedrooms,
        data.bathrooms,
        data.location_score
    ]])

    price = model.predict(features)[0]

    return {
        "predicted_price": round(float(price), 2)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

