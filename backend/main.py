from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import pickle
import pandas as pd
import os
import uuid
from datetime import datetime
import logging
app = FastAPI()


# -----------------------------
# CORS
# -----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# LOAD MODEL
# -----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# =========================================================
# LOAD MODEL
# =========================================================

model_path = os.path.join(
    BASE_DIR,
    "LinearRegression.pkl"
)

with open(model_path, "rb") as file:
    model = pickle.load(file)


# -----------------------------
# LOAD DATA
# -----------------------------

data_path = os.path.join(
    BASE_DIR,
    "Data",
    "Cleaned Car.csv"
)

car = pd.read_csv(data_path)


# =========================================================
# IN-MEMORY PREDICTION HISTORY
# =========================================================

# This stores predictions while FastAPI is running.
# Data will be lost when the server restarts.

predictions_db = []

# -----------------------------
# REQUEST MODEL
# -----------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

class CarData(BaseModel):
    name: str = Field(min_length=1)
    company: str = Field(min_length=1)
    year: int = Field(ge=1990, le=2026)
    kms_driven: int = Field(ge=0, le=1000000)
    fuel_type: str = Field(min_length=1)
    owner: str = Field(min_length=1)
# -----------------------------
# HOME
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "Car Price Prediction API is running"
    }


# -----------------------------
# GET OPTIONS
# -----------------------------

@app.get("/options")
def options():

    encoder = (
        model
        .named_steps["columntransformer"]
        .named_transformers_["onehotencoder"]
    )

    categories = encoder.categories_

    return {
            "car_models": categories[0].tolist(),
            "companies": categories[1].tolist(),
            "fuel_types": categories[2].tolist(),
            "owners": [
                "First Owner",
                "Second Owner",
                "Third Owner",
                "Fourth Owner"
            ]
}

# -----------------------------
# PREDICT
# -----------------------------

@app.post("/predict")
def predict(data: CarData):

    input_data = pd.DataFrame(
        [[
            data.name,
            data.company,
            data.year,
            data.kms_driven,
            data.fuel_type
        ]],
        columns=[
            "name",
            "company",
            "year",
            "kms_driven",
            "fuel_type"
        ]
    )

    try:

        prediction = model.predict(input_data)
        base_price = float(prediction[0])

        owner_adjustments = {
            "First Owner": 0.00,
            "Second Owner": 0.05,
            "Third Owner": 0.10,
            "Fourth Owner": 0.20
        }

        discount = owner_adjustments.get(data.owner, 0.00)

        predicted_price = round(
        base_price * (1 - discount),
        2
    )

        record = {
            "id": str(uuid.uuid4()),
            "name": data.name,
            "company": data.company,
            "year": data.year,
            "kms_driven": data.kms_driven,
            "fuel_type": data.fuel_type,
            "owner": data.owner,
            "predicted_price": predicted_price,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }


        predictions_db.append(record)

        return {
            "predicted_price": predicted_price
        }

    except Exception as e:

        return {
            "error": str(e)
        }
@app.get("/predictions")
def get_predictions():

    global predictions_db

    # Give old records an ID
    for p in predictions_db:
        if "id" not in p:
            p["id"] = str(uuid.uuid4())

    return {
        "predictions": list(reversed(predictions_db))
    }

@app.delete("/predictions/{prediction_id}")
def delete_prediction(prediction_id: str):

    global predictions_db

    old_count = len(predictions_db)

    predictions_db = [
        p for p in predictions_db
        if p.get("id") != prediction_id
    ]

    if len(predictions_db) == old_count:
        return {
            "success": False,
            "message": "Prediction not found"
        }

    return {
        "success": True,
        "message": "Prediction deleted",
        "deleted": prediction_id
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }