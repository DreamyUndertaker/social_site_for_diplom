from django.forms import ModelForm, TextInput
from .models import Comment, News

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['content']
        widgets = {
            "content": TextInput(attrs={
                'content': 'form-control',
                'placeholder': 'Текст статьи'
            }),
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']