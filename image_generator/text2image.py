import requests

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content
