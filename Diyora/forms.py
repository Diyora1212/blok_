from django import forms
from django.core.exceptions import ValidationError
from .models import User, Post
from django.forms import ModelForm


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'date_posted', 'author']

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'date_posted', 'author']

class PostDeleteForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'content', 'date_posted', 'author']
        model = Post
        exclude = ['author']


class UserRegisterModelForm(forms.ModelForm):
    password1 = forms.CharField(max_length=128)
    password2 = forms.CharField(max_length=128)

    def save(self, commit=True):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 == password2:
            user = super().save(commit)
            user.set_password(password1)
            user.save()
        else:
            raise ValidationError("Password must be match")

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128)
