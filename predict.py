import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
import pandas as pd

INPUT_DATA = {
    "animal_id": ["0002", "0007", "0030", "0046"],
    "sex": ["M", "M", "F", "M"],
    "birth_type": ["wild", "wild", "wild", "wild"],
    "genus": ["O", "O", "E", "H"],
    "species": ["GG", "GG", "COL", "GG"],
    "age": [3.93, 7.55, 5.55, 1.50],
    "month_born": ["Jan", "Jan", "Oct", "Dec"]
}
pandas2ri.activate()

# Load the R base package
base = importr('base')

captive_rds = "captive_model.rds"
wild_rds = "wild_model.rds"

# Load the model
read_rds = ro.r['readRDS']
captive_model = read_rds(captive_rds)
wild_model = read_rds(wild_rds)

def get_predictions(input_data):
    data = pd.DataFrame(input_data)

    # Convert to R data frame
    r_data = pandas2ri.py2rpy(data)

    # Predict using the model
    predict_function = ro.r['predict']
    captive_predictions = predict_function(captive_model, newdata=r_data)
    wild_predictions = predict_function(wild_model, newdata=r_data)

    # Convert R prediction output to Python
    captive_predictions = list(captive_predictions)
    wild_predictions = list(wild_predictions)

    # convert np float to python float
    for i in range(len(captive_predictions)):
        wild_predictions[i] = float(wild_predictions[i])
        captive_predictions[i] = float(captive_predictions[i])

    predictions = {
        "predicted captive lifespan/s": captive_predictions,
        "predicted wild lifespan/s": wild_predictions
    }
    return predictions