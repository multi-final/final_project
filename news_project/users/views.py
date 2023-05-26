from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from .models import User
from .forms import UserForm
import json


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
        username = req.POST.get('username')
        password = req.POST.get('password')

        user_login = authenticate(req,username=username, password=password)
        if user_login is not None:
            login(req, user_login)
            print('로그인 성공')
            return redirect('/')
        else:
            return render(req, 'users/login.html',{'error':'a'})

def user_logout(req):
    logout(req)
    return redirect('/')
# 
def password(req):
    if req.method == 'POST':
        print(req.POST)
        print(req.user)
        # <QueryDict: {'csrfmiddlewaretoken': ['IgcaNpYrjlSGwsDJd4cHv8OAuNxwBuGuugJaUVut6lzcPfh53CQnSGeYH3gkA0uD'], 'old_password': ['qew'], 'new_password1': ['asg'], 'new_password2': ['qwet']}>
        old_password=req.POST.get('old_password')
        new_password1=req.POST.get('new_password1')
        new_password2=req.POST.get('new_password2')
        user = req.user
        if check_password(old_password, user.password):
            if  new_password1 == new_password2:
                try:
                    validate_password(new_password1)
                except ValidationError as e:
                    context = {
                    'message': e.messages,
                    'error_code': 1,
                    }
                
                    return JsonResponse(context)
                user.set_password(new_password1)
                user.save()
                login(req,user)
                context = {
                    'message': 'Your password was successfully updated!',
                    'error_code': 0,
                    }
                
                return JsonResponse(context)
            else:
                context = {
                    'message': 'Check the comfirmed password',
                    'error_code': 1,
                    }
                
                return JsonResponse(context)
        else:
            context = {
                'message': 'Check your old_password',
                'error_code': 1,
                }
            
            return JsonResponse(context)
        #식사 후에 이거 json으로 오류코드 만들어서 보낼 궁리 해봐야 함
        # form = PasswordChangeForm(req.user, req.POST)
        # print(form)
        # if form.is_valid():
        #     user = form.save()
        #     update_session_auth_hash(req, user)  # Important!
        #     messages.success(req, 'Your password was successfully updated!')
        #     return HttpResponse()
        # else:
        #     messages.error(req, 'Please correct the error below.')
        #     return HttpResponse()
    
    else:
        form = PasswordChangeForm(req.user)
    return render(req, 'users/password.html', {'form': form})


def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        logout(request)
    return redirect('/')
