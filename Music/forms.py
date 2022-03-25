from dataclasses import fields
from django import forms
from .models import MusicType, Author, Song

class MTForm(forms.ModelForm):
    class Meta:
        model=MusicType
        fields='__all__'

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields='__all__'

class SongForm(forms.ModelForm):
    class Meta:
        model=Song
        fields='__all__'