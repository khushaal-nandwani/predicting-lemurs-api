# Predicting Lemurs API (Not Live)

This repository contains the api for the model created in the paper [Lifespan Analysis of Lemurs in Wild and Captive Environments](https://github.com/khushaal-nandwani/predicting-lemurs). The API is hosted on Heroku and can be accessed at the following URL: https://lemur-predictions-5a0eb4f74f1f.herokuapp.com

To make predictions of lemur in wild and captive, please send a POST request to the URL 
```https://lemur-predictions-5a0eb4f74f1f.herokuapp.com/predict``` 
with the following JSON payload:

```json
{
  "data": {
        "animal_id": ["0002", "0007", "0030", "0046"],
        "sex": ["M", "M", "F", "M"],
        "birth_type": ["wild", "wild", "wild", "wild"],
        "genus": ["O", "O", "E", "H"],
        "species": ["GG", "GG", "COL", "GG"],
        "age": [3.93, 7.55, 5.55, 1.50],
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

# Heroku Error

Unfortunately, the API is live but does not run at the moment. This is because making R run on heroku is a bit of a challenge and I am still working on it. I am trying to use [this buildpack](https://github.com/virtualstaticvoid/heroku-buildpack-r) to make it work, however Heroku is throwing an error of `App not compatible with buildpack`.

# Structure

The API is structured in the following manner:

- `app.py`: The main file that contains the API code. 
- `predict.py`: This file contains the code for making predictions. It opens the model file using `rpy2` library and makes predictions.
- `test_api.py` contains a simple test for the API. It sends a POST request to the API and checks if the response is as expected.
