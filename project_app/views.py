from django.shortcuts import render
from gtts import gTTS
from io import BytesIO
from .phrase import generate_text
from django import forms
from .questionanswering import answer_question
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .image2text import image_to_text
import io
import base64
from .text2image import query
from PIL import Image
from .textclassification import classifier
from .labels import CANDIDATE_LABELS

def index(request):
    return render(request, "index.html")

class ImageUploadForm(forms.Form):
    image = forms.ImageField()


@csrf_exempt
def image2text(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            output = image_to_text(image)
            return render(request, 'image2textresult.html', {'output': output})
    else:
        form = ImageUploadForm()
        
    return render(request, 'image2text.html', {'form': form})




        
        
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def image2text_api(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['image']
            output = image_to_text(image)
            return Response({'output': output}, status=status.HTTP_200_OK)
        else:
            errors = form.errors
            print(f"Form validation errors: {errors}")
            return Response({'error': 'Invalid form data', 'details': errors}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def text2image(request):
    if request.method == 'POST':
        text_input = request.POST.get('text_input', '')
        image_bytes = query({
            "inputs": text_input,
        })
        image = Image.open(io.BytesIO(image_bytes))
        img_io = io.BytesIO()
        image.save(img_io, format='JPEG')
        img_url = base64.b64encode(img_io.getvalue()).decode()
        return render(request, 'image.html', {'img_url': img_url})
    return render(request, 'text2image.html')


@csrf_exempt
def textclassifier(request):
    if request.method == 'POST':
        sequence = request.POST.get('sequence', '')
        candidate_labels = CANDIDATE_LABELS
        payload = {"inputs": sequence, "parameters": {"candidate_labels": candidate_labels}}
        results = classifier(payload, candidate_labels)
        
        # print("API Response:", results)
        
        if 'scores' in results and 'labels' in results:
            max_index = results['scores'].index(max(results['scores']))
            label_with_highest_percentage = results['labels'][max_index]
            highest_percentage = results['scores'][max_index]

            return render(request, 'result.html', {'label': label_with_highest_percentage, 'percentage': highest_percentage, 'sequence': sequence})
        else:            
            error_message = "Invalid response format from the API"
            return render(request, 'error.html', {'error_message': error_message})
        
    return render(request, 'textclassification.html')


@csrf_exempt
def question_answering(request):
    if request.method == 'POST':
        context = request.POST.get('context', '')
        question = request.POST.get('question', '')
        answer = answer_question(context, question)
        return render(request, 'answer.html', {'answer': answer, 'context': context, 'question': question})

    return render(request, 'questionanswering.html')


@csrf_exempt
def phrasemaking(request):
    if request.method == 'POST':        
        prompt = request.POST.get('text', '')          
        generated_text = generate_text(prompt)  
        return render(request, 'phrasemaking.html', {'output': generated_text, 'input_text': prompt})
    else:
        return render(request, 'phrasemaking.html', {'output': '', 'input_text': ''})
    





@csrf_exempt
def text2audio(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        if text:
            speech = gTTS(text)
            audio_buffer = BytesIO()
            speech.write_to_fp(audio_buffer)
            audio_buffer.seek(0)
            
            response = HttpResponse(audio_buffer.read(), content_type='audio/mpeg')
            response['Content-Disposition'] = 'attachment; filename="text_speech.mp3"'
            return response

    return render(request, 'text2audio.html')
