import requests

API_URL = "https://api-inference.huggingface.co/models/distilgpt2"
headers = {"Authorization": "Bearer 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"}

def generate_text(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


	

