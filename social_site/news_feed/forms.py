from django import forms
from .models import Comment, News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']