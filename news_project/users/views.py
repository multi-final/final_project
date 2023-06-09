from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from .models import User
from .forms import UserForm, customUserCreationForm
import json

def signup(req):
    if req.method == "POST":
        form = UserForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(req, user)  # 로그인
            return redirect('/')
    else:
        form = UserForm()
    return render(req, 'users/signup.html', {'form': form})



def user_login(req):
    if req.method == 'GET':
        return render(req, 'users/login.html')
    
    else:
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
 
def password(req):
    if req.method == 'POST':
        old_password=req.POST.get('old_password')
        new_password1=req.POST.get('new_password1')
        new_password2=req.POST.get('new_password2')
        user = req.user
        if check_password(old_password, user.password):
            # 변경한 비밀번호를 동일하게 입력한 경우
            if  new_password1 == new_password2:
                try:
                    validate_password(new_password1)
                # 변경한 비밀번호가 유효하지 않은 경우
                except ValidationError as e:
                    context = {
                    'message': e.messages,
                    'error_code': 1,
                    }                
                    return JsonResponse(context)
                # 변경한 비밀번호가 유효한 경우
                user.set_password(new_password1)
                user.save()
                login(req,user)
                context = {
                    'message': 'Your password was successfully updated!',
                    'error_code': 0,
                    }
                return JsonResponse(context)
            # 변경한 비밀번호를 동일하게 입력하지 않은 경우
            else:
                context = {
                    'message': 'Check the comfirmed password',
                    'error_code': 1,
                    }                
                return JsonResponse(context)
        # 이전 비밀번호를 잘못 입력한 경우    
        else:
            context = {
                'message': 'Check your old_password',
                'error_code': 1,
                }            
            return JsonResponse(context)
    
    return render(req, 'users/password.html')


def delete(req):
    if req.user.is_authenticated:
        req.user.delete()
        logout(req)
    return redirect('/')
