import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
headers = {"Authorization": "Bearer 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"}

def classifier(payload, candidate_labels):
    payload["candidate_labels"] = candidate_labels
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

