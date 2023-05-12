from django.shortcuts import render, get_object_or_404, redirect
# from .models import Photo
# from .forms import PhotoForm
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile
# from django.http import HttpResponse

def scrap(request):
    return render(request, 'scrap/scrap.html')