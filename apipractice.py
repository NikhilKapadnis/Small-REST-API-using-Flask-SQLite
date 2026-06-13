import requests
import json
print("requests is working")

url = "https://api.stackexchange.com/2.3/questions"
params = {
    "site": "stackoverflow",
    "order": "desc",
    "sort": "activity"
}
response = requests.get(url, params=params)

print("status code:", response.status_code)
print("content-type:", response.headers.get("content-type"))
print("raw response:")
print(response.text[:500])