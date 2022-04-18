from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, fields
from .models import Notes

TAGS = (
        ("work", "WORK"),
        ("recipes", "RECIPES"),
        ("sports", "SPORTS"),
    )


class NotesForm(ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder":"Enter Title"
    }))
    description = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
         "class": "form-control", "placeholder":"Enter Notes", "rows":"8"
    }))
    tags = forms.RadioSelect(choices=TAGS)

    class Meta:
        model = Notes
        fields = ['title', 'description','tags']
