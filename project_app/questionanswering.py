import requests

API_URL = "https://api-inference.huggingface.co/models/timpal0l/mdeberta-v3-base-squad2"
headers = {"Authorization": "Bearer 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"}

def answer_question(context, question):
    payload = {"context": context, "question": question}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
	





