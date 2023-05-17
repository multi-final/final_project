from django.shortcuts import render, get_object_or_404, redirect
# from .models import Photo
# from .forms import PhotoForm
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile
# from django.http import HttpResponse
import datetime

def scrap(request):
    now = datetime.datetime.now()
    articles = []
    for i in range(300):
        articles.append({'id':i, 'date': datetime.datetime.now() - datetime.timedelta(i), 'article': str(i) + 'lorem'})
    return render(request, 'scrap/scrap.html', {'articles':articles, 'datenow':now})