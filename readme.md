# Predicting Lemurs API

This repository contains the api for the model created in the paper [Lifespan Analysis of Lemurs in Wild and Captive Environments](https://github.com/khushaal-nandwani/predicting-lemurs). The API is hosted on AWS EC2 instance.

There is a frontend available for this API which is on [this site](http://3.99.183.165:5173) and the code for the frontend can be found in [this repo](https://github.com/khushaal-nandwani/predicting-lemurs-frontend).


To make predictions of lemur in wild and captive, please send a POST request to the URL 

```http://3.99.183.165:8000/predict```

with the following JSON payload:

```json
{
  "data": {
        "animal_id": ["0002", "0007", "0030", "0046"],
        "sex": ["M", "M", "F", "M"],
        "genus": ["O", "O", "E", "H"],
        "species": ["GG", "GG", "COL", "GG"],
        "month_born": ["Jan", "Jan", "Oct", "Dec"]
    }
}
```

You should expect to see predictions in the following manner

```json

{
    "predictions": {
        "predicted captive lifespan/s": [25.0, 25.0, 25.0, 25.0],
        "predicted wild lifespan/s": [25.0, 25.0, 25.0, 25.0]
    }
}
```

# Structure

The API is structured in the following manner:

- `app.py`: The main file that contains the API code. 
- `predict.py`: This file contains the code for making predictions. It opens the model file using `rpy2` library and makes predictions.
- `test_api.py` contains a simple test for the API. It sends a POST request to the API and checks if the response is as expected.


# Running in Local

To run the API in local, please install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

Then run the following command:

```bash
uvicorn main:app --host=0.0.0.0 --port=8000
```

