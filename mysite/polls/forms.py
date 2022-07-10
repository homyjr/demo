from dataclasses import fields
from django import forms

from .models import Song, Artist



class SongForm(forms.ModelForm):
    
    class Meta:
        model = Song
        fields= '__all__'