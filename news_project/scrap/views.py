from django.shortcuts import render, get_object_or_404, redirect
# from .models import Photo
# from .forms import PhotoForm
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile
# from django.http import HttpResponse
import datetime

def scrap(request):
    now = datetime.datetime.now() # 현재 형식
    articles = []
    chk = ''
    for i in range(300):
        if i < 1:
            chk = 'today'
        elif i < 2:
            chk = 'yesterday'
        elif i < 8:
            chk = 'week ago'
        elif i < 31:
            chk = 'month ago'
        else:
            chk = 'long ago'
        articles.append({'id':i, 'date': datetime.datetime.now() - datetime.timedelta(i), 'd_chk':chk, 'd_diff':datetime.timedelta(i), 'article': str(i) + 'lorem'})
    return render(request, 'scrap/scrap.html', {'articles':articles, 'datenow':now})