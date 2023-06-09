from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# 현재 사용중인 form
class UserForm(UserCreationForm):
    email = forms.EmailField(label="email")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")

class customUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': '아이디'
            }
        ),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'input',
                'placeholder': '이메일'
            }
        ),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
                'placeholder': '비밀번호'
            }
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
                'placeholder': '비밀번호 확인'
            }
        ),
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2',)