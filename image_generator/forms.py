
from django import forms

class TextForm(forms.Form):
    prompt = forms.CharField(max_length=100, required=True)
