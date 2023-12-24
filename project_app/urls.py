from django.urls import path
from .views import *


urlpatterns = [
    path("",index, name="index"),
    path("image_to_text/", image2text, name="image2text"),
    path("text2image/", text2image, name="text2image"),
    path("textclassifier/", textclassifier, name="textclassifier"),
    path("question_answering/", question_answering, name="question_answering"),
    path("phrasemaking/", phrasemaking, name="phrasemaking"), 
    path("text2audio/", text2audio, name="text2audio"),



    #api path
    path('image2text/', image2text_api, name='image2text_api'),

    
]
