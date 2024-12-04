import requests

url = "http://0.0.0.0:8000/predict"  # Replace with the actual server URL

data = {
    "data": {}
}

response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    print("Prediction:", response.json())
else:
    print("Error:", response.status_code, response.text)
