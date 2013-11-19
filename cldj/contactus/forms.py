from django import forms
from django.forms import ModelForm
from contactus.models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ('',)
