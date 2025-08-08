import requests

API_TOKEN = "xxxxxxxxxxxxxxxxx"
JOB_ID = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
RUNDECK_URL = f"http://localhost:4440/api/53/job/{JOB_ID}/run"

headers = {
    "X-Rundeck-Auth-Token": API_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "options": {
        "message": "Hello depuis Python via API 🐍"
    }
}

response = requests.post(RUNDECK_URL, headers=headers, json=payload)

print("Status code:", response.status_code)
print("Response:", response.text)
