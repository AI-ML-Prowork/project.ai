from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("text2image/", text2image, name="text2image"),
    path("textclassifier/", textclassifier, name="textclassifier"),
    path("text2audio/", text2audio, name="text2audio"),
    path('text_to_video/', text_to_video, name='text_to_video'),
    path("image2text/", image2text, name="image2text"),
    path("question_answering/", question_answering, name="question_answering"),
    path("phrasemaking/", phrasemaking, name="phrasemaking"),    
]