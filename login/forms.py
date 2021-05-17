from django import forms
from .models import Anime

class UploadForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ('Anime_title', 'Anime_description', 'Anime_file', 'Anime_Category','Anime_view')

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('message',)