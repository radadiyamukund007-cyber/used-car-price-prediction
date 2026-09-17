from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import pandas as pd
import os

app = FastAPI()


# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# BASE DIRECTORY
# =========================================================

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


# =========================================================
# LOAD DATASET
# =========================================================

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


# =========================================================
# REQUEST MODEL
# =========================================================

class CarData(BaseModel):
    name: str
    company: str
    year: int
    kms_driven: int
    fuel_type: str


# =========================================================
# HOME
# =========================================================

@app.get("/")
def home():
    return {
        "message": "Car Price Prediction API is running"
    }


# =========================================================
# GET OPTIONS
# =========================================================

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
        "fuel_types": categories[2].tolist()
    }


# =========================================================
# PREDICT
# =========================================================

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

        # Make prediction
        prediction = model.predict(input_data)

        predicted_price = round(float(prediction[0]), 2)

        # -------------------------------------------------
        # SAVE PREDICTION TO HISTORY
        # -------------------------------------------------

        record = {
            "name": data.name,
            "company": data.company,
            "year": data.year,
            "kms_driven": data.kms_driven,
            "fuel_type": data.fuel_type,
            "predicted_price": predicted_price
        }

        predictions_db.append(record)

        # -------------------------------------------------
        # RETURN RESULT
        # -------------------------------------------------

        return {
            "predicted_price": predicted_price
        }

    except Exception as e:

        return {
            "error": str(e)
        }


# =========================================================
# GET PREDICTION HISTORY
# =========================================================

@app.get("/predictions")
def get_predictions():

    # Most recent prediction first
    return {
        "predictions": list(reversed(predictions_db))
    }