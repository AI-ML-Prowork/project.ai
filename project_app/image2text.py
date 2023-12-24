import requests

API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
headers = {"Authorization": "Bearer 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"}

def query(image_data):
    response = requests.post(API_URL, headers=headers, data=image_data)
    return response.json()

def image_to_text(image):
    image_data = image.read()
    output = query(image_data)
    return output


