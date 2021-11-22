from django.forms import ModelForm
from .models import *
from django import forms


SEARCH_TYPES =(
    ("Title", "Title"),
    ("Author", "Author"),
    ("Subject", "Subject"),
)


class DoubtForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Doubt Heading"
        })
    )
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Write your doubt here!"
        })
    )
    link = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Reference Link"
        })
    )
    tag = forms.ModelChoiceField(queryset=Subject.objects.all())


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )


class SearchForm(forms.Form):
    search_type = forms.ChoiceField(choices=SEARCH_TYPES)
    search_query = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Search Query"
        })
    )
