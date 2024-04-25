import json
import requests

# The URL for the MLflow model serving endpoint
url = 'http://localhost:5000/invocations'
headers = {'Content-Type': 'application/json'}

# Prepare the request data as a JSON payload
request_data = json.dumps({
    'columns': ["sepal_length", "sepal_width", "petal_length", "petal_width"],
    'data': [[6.3, 3.3, 6.0, 2.5]]
})

# Make the POST request and print the response
response = requests.post(url, headers=headers, data=request_data)
print(response.text)
