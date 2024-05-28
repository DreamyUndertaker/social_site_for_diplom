# messenger/forms.py
from django import forms
from django.contrib.auth.models import User


class CreateDialogForm(forms.Form):
    participant = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'label': 'собеседник'
        })
    )


class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
