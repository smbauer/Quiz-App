import requests

QUESTIONS_URL = "https://opentdb.com/api.php"

params = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url=QUESTIONS_URL, params=params)
response.raise_for_status()
question_data = response.json()["results"]
