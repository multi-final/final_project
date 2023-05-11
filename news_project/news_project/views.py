from django.shortcuts import render, get_object_or_404, redirect
# from .models import Photo
# from .forms import PhotoForm
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile
# from django.http import HttpResponse

def main(request):
    return render(request, 'main/sidepannel_test_copy.html')

def test(req):
    return render(req, 'main/test.html')

def login(request):
    pass

def register(request):
    pass

def scrap(request):
    pass