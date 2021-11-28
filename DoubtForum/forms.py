from .models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


SEARCH_TYPES = (
    ("Title", "Title"),
    ("Author", "Author"),
    ("Subject", "Subject"),
)


class DoubtForm(forms.Form):
    """
    Class to collect information to create a doubt object.
    """
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Doubt Heading"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Write your doubt here!"
        })
    )
    link = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            "class": "form-control",
            "placeholder": "Reference Link"
        })
    )
    tag = forms.ModelChoiceField(queryset=Subject.objects.all())


class CommentForm(forms.Form):
    """
    Class to collect information to create a comment object.
    """
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )


class SearchForm(forms.Form):
    """
    Class to collect information on search string.
    """
    search_type = forms.ChoiceField(choices=SEARCH_TYPES)
    search_query = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Search Query',
            }
        )
    )


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        })
    )
