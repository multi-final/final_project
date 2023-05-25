from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import User
from .forms import UserForm


# fields = ("username", "password1", "password2", "email")
def signup(req):
    if req.method == 'GET':
        form = UserForm()
        return render(req, 'users/signup.html', {'form': form})
    if req.method == "POST":
        form = UserForm(req.POST)
        if form.is_valid():
            new_user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            login(req,new_user)
            return redirect('/')
        else:
            return render(req,'users/signup.html',{'form':form})

def user_login(req):
    if req.method == 'GET':
        return render(req, 'users/login.html')
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        login = authenticate(req,username=username, password=password)
        print(login)
        if login is not None:
            login(req, login)
            return redirect('/')
        else:
            return HttpResponse('<script> alert("로그인 실패."); location.href="/users/login/";</script>')

def user_logout(req):
    logout(req)
    return redirect('/')
# 
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponse()
        else:
            messages.error(request, 'Please correct the error below.')
    
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/password.html', {'form': form})