from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import rpy2.robjects as ro
import os
from predict import get_predictions

app = FastAPI()

# Define input data structure
class PredictionRequest(BaseModel):
    data: dict

REQUIRED_COLUMNS = ["animal_id", "sex", "birth_type", "genus", "species", "age", "month_born"]

@app.post("/predict")
async def predict(request: PredictionRequest):
    try:
        for col in REQUIRED_COLUMNS:
            if col not in request.data:
                raise HTTPException(status_code=400, detail=f"Missing required column: {col}")
        return {"predictions": get_predictions(request.data)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
