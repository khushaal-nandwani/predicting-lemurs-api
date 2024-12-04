# Predicting Lemurs API

The API is hosted on Heroku and can be accessed at the following URL: https://lemur-predictions-5a0eb4f74f1f.herokuapp.com

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