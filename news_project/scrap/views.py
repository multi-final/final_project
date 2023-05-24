from django.shortcuts import render, get_object_or_404, redirect
from news.models import Article
from scrap.models import Scrap
from .models import Scrap
from django.db.models import Q
from django.http import HttpResponse

import datetime

def scrap(request):
    if request.method=='GET':
        now = datetime.datetime.now() # 현재 형식          <= 24시간전 < 데이터 < 48시간전 30
        articles = Scrap.objects.filter(user = request.user).select_related().order_by('-created_date')
        dbarticles_today = articles.filter(created_date__gte = (now-datetime.timedelta(1)))
        dbarticles_this_week = articles.filter(created_date__range = (now-datetime.timedelta(8), now-datetime.timedelta(1)))
        dbarticles_last_week = articles.filter(created_date__range = (now-datetime.timedelta(15), now-datetime.timedelta(8)))
        dbarticles_long_ago = articles.filter(created_date__lt = (now-datetime.timedelta(15)))

        return render(request, 'scrap/scrap.html', {'dbarticles_today':dbarticles_today, 'dbarticles_this_week':dbarticles_this_week, 'dbarticles_last_week':dbarticles_last_week,'dbarticles_long_ago':dbarticles_long_ago})
    
    else:
        press_form=request.POST.getlist('press')
        section_form=request.POST.getlist('section')
        user_article = Scrap.objects.filter(user=request.user).select_related().order_by('-created_date')
        if not press_form and not section_form:
            articles = user_article
        elif press_form and not section_form:
            press_form=list(map(int,press_form))
            articles = user_article.filter(article__press__in=press_form).select_related()
        elif not press_form and section_form:
            section_form=list(map(int,section_form))
            articles = user_article.filter(article__section__in=section_form).select_related()
        else:
            articles = user_article.filter(Q(article__press__in=press_form)&Q(article__section__in=section_form)).select_related()
        now = datetime.datetime.now()
        dbarticles_today = articles.filter(created_date__gte = (now-datetime.timedelta(1)))
        dbarticles_this_week = articles.filter(created_date__range = (now-datetime.timedelta(8), now-datetime.timedelta(1)))
        dbarticles_last_week = articles.filter(created_date__range = (now-datetime.timedelta(15), now-datetime.timedelta(8)))
        dbarticles_long_ago = articles.filter(created_date__lt = (now-datetime.timedelta(15)))
        context={'dbarticles_today':dbarticles_today,'dbarticles_this_week':dbarticles_this_week,
                 'dbarticles_last_week':dbarticles_last_week,'dbarticles_long_ago':dbarticles_long_ago}
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
    
