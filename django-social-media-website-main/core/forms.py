# Create a VideoUploadForm in your forms.py
from django import forms
from .models import Video

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video', 'caption']  # Add any additional fields as needed
