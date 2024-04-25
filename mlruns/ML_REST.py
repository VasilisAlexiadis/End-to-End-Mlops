import json
import requests

url = 'http://localhost:5000/invocations'
headers = {'Content-Type': 'application/json'}

request_data = json.dumps({'columns': [["sepal_length", "sepal_width", "petal_length", "petal_width"],"data": [[6.3, 3.3, 6.0, 2.5]]}})
response = requests.post(url, headers=headers, data=request_data)
print(response.text)