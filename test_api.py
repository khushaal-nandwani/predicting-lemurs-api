import requests

url = "https://lemur-predictions-5a0eb4f74f1f.herokuapp.com/predict"  # Replace with the actual server URL

data = {
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

response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    print("Prediction:", response.json())
else:
    print("Error:", response.status_code, response.text)
