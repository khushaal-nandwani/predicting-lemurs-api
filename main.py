from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import rpy2.robjects as ro
from fastapi.middleware.cors import CORSMiddleware
from predict import get_predictions

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Add your frontend URL here
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


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
