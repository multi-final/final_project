from django.shortcuts import render, get_object_or_404, redirect
from news.models import Article
from scrap.models import Scrap
from .models import Scrap
from django.db.models import Q
from django.http import HttpResponse
# from .forms import PhotoForm
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile
# from django.http import HttpResponse
import datetime

def scrap(request):
    if request.method=='GET':
        now = datetime.datetime.now() # 현재 형식          <= 24시간전 < 데이터 < 48시간전 30
        articles = Scrap.objects.filter(user = request.user).select_related().order_by('-created_date')
        dbarticles_today = articles.filter(created_date__gte = (datetime.datetime.now()-datetime.timedelta(1)))
        dbarticles_yesterday = articles.filter(created_date__range = (datetime.datetime.now()-datetime.timedelta(2), datetime.datetime.now()-datetime.timedelta(1)))
        dbarticles_this_week = articles.filter(created_date__range = (datetime.datetime.now()-datetime.timedelta(8), datetime.datetime.now()-datetime.timedelta(2)))
        dbarticles_last_week = articles.filter(created_date__range = (datetime.datetime.now()-datetime.timedelta(15), datetime.datetime.now()-datetime.timedelta(8)))
        dbarticles_this_month = articles.filter(created_date__range = (datetime.datetime.now()-datetime.timedelta(31), datetime.datetime.now()-datetime.timedelta(15)))
        dbarticles_long_ago = articles.filter(created_date__lt = (datetime.datetime.now()-datetime.timedelta(31)))

        return render(request, 'scrap/scrap.html', {'dbarticles_today':dbarticles_today, 'dbarticles_yesterday':dbarticles_yesterday, 'dbarticles_this_week':dbarticles_this_week, 'dbarticles_last_week':dbarticles_last_week, 'dbarticles_this_month':dbarticles_this_month, 'dbarticles_long_ago':dbarticles_long_ago})
    
    else:
        press_form=request.POST.getlist('press')
        section_form=request.POST.getlist('section')
        if not press_form and not section_form:
            articles = Article.objects.all().select_related().order_by('-created_date')
        elif press_form and not section_form:
            press_form=list(map(int,press_form))
            articles = Article.objects.filter(press__in=press_form).select_related()
        elif not press_form and section_form:
            section_form=list(map(int,section_form))
            articles = Article.objects.filter(section__in=section_form).select_related()
        else:
            articles = Article.objects.filter(Q(press__in=press_form)&Q(section__in=section_form)).select_related()
        
        # dbarticles_today = articles.filter(created_date__gte = (datetime.datetime.now()-datetime.timedelta(1)))
        # dbarticles_yesterday = articles.filter(created_date__range = (datetime.datetime.now()-datetime.timedelta(2), datetime.datetime.now()-datetime.timedelta(1)))
        # dbarticles_week_ago = articles.filter(created_date__range = (datetime.datetime.now()-datetime.timedelta(8), datetime.datetime.now()-datetime.timedelta(2)))
        # dbarticles_month_ago = articles.filter(created_date__range = (datetime.datetime.now()-datetime.timedelta(31), datetime.datetime.now()-datetime.timedelta(8)))
        dbarticles_today = articles.filter(created_date__gte = (datetime.datetime.now()-datetime.timedelta(1)))
        dbarticles_yesterday = articles.filter(created_date__range = (datetime.datetime.now()-datetime.timedelta(2), datetime.datetime.now()-datetime.timedelta(1)))
        dbarticles_this_week = articles.filter(created_date__range = (datetime.datetime.now()-datetime.timedelta(8), datetime.datetime.now()-datetime.timedelta(2)))
        dbarticles_last_week = articles.filter(created_date__range = (datetime.datetime.now()-datetime.timedelta(15), datetime.datetime.now()-datetime.timedelta(8)))
        dbarticles_this_month = articles.filter(created_date__range = (datetime.datetime.now()-datetime.timedelta(31), datetime.datetime.now()-datetime.timedelta(15)))
        dbarticles_long_ago = articles.filter(created_date__lt = (datetime.datetime.now()-datetime.timedelta(31)))
        context={'dbarticles_today':dbarticles_today, 'dbarticles_yesterday':dbarticles_yesterday,
                 'dbarticles_this_week':dbarticles_this_week, 'dbarticles_last_week':dbarticles_last_week,
                 'dbarticles_this_month':dbarticles_this_month, 'dbarticles_long_ago':dbarticles_long_ago}
        return render(request, 'scrap/scrap.html', context)

# class Scrap(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     created_date = models.DateTimeField(auto_now_add=True)
def scrap_insert(req,id):
    if req.user.is_authenticated:
        user = req.user
        article = Article.objects.get(id=id)
        Scrap.objects.create(
            user = user,
            article = article
        )
        return HttpResponse()
    else:
        return HttpResponse('유효하지 않음.')
def scrap_delete(req, id):
    scrap = Scrap.objects.get(id=id)
    try:
        if req.user == scrap.user:
            scrap.delete()
            return HttpResponse()
        else:
            return HttpResponse('잘못된 접근')
    except scrap.DoesNotExist:
        return HttpResponse('객체 이미 없음')
    
