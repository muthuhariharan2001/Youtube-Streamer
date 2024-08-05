from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

class VideoSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=200)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
