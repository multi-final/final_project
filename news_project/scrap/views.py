from django.shortcuts import render, get_object_or_404, redirect
from news.models import Article
from scrap.models import Scrap
from .models import Scrap
from django.db.models import Q
from django.http import HttpResponse
import json
import datetime

def scrap(request):
    if request.method=='GET':
        now = datetime.datetime.now()
        # 유저가 스크랩 한 기사 필터링
        articles = Scrap.objects.filter(user = request.user).select_related().order_by('-created_date')
        # 설정한 기간별로 기사 나누기
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
        
        context={

            'dbarticles_today':dbarticles_today,
            'dbarticles_this_week':dbarticles_this_week,
            'dbarticles_last_week':dbarticles_last_week,
            'dbarticles_long_ago':dbarticles_long_ago

            }
        return render(request, 'scrap/scrap.html', context)

def scrap_insert(req,id):
    if req.user.is_authenticated:
        user = req.user
        article = Article.objects.get(id=id)   # 스크랩한 기사
        # 스크랩 한 내용 저장
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

def search(req):
    if req.method=='GET':
        search = req.GET.get('search')
        press = req.GET.get('press').replace("'","")
        section = req.GET.get('section').replace("'","")

        if press:
            press = json.loads(press)

        if section:
            section = json.loads(section)

        user_article = Scrap.objects.filter(user=req.user).select_related().order_by('-created_date')
        if not press and not section:
            articles = user_article
        elif press and not section:
            press=list(map(int,press))
            articles = user_article.filter(article__press__in=press).select_related()
        elif not press and section:
            section=list(map(int,section))
            articles = user_article.filter(article__section__in=section).select_related()
        else:
            articles = user_article.filter(Q(article__press__in=press)&Q(article__section__in=section)).select_related()

        articles = articles.filter(Q(article__headline__contains=search)|Q(article__content__contains=search)).select_related()

        now = datetime.datetime.now()
        # 유저가 스크랩 한 기사 필터링
        # 설정한 기간별로 기사 나누기
        dbarticles_today = articles.filter(created_date__gte = (now-datetime.timedelta(1)))
        dbarticles_this_week = articles.filter(created_date__range = (now-datetime.timedelta(8), now-datetime.timedelta(1)))
        dbarticles_last_week = articles.filter(created_date__range = (now-datetime.timedelta(15), now-datetime.timedelta(8)))
        dbarticles_long_ago = articles.filter(created_date__lt = (now-datetime.timedelta(15)))

        context = {
            'dbarticles_today':dbarticles_today,
            'dbarticles_this_week':dbarticles_this_week,
            'dbarticles_last_week':dbarticles_last_week,
            'dbarticles_long_ago':dbarticles_long_ago,
            "q":search
        }

        return render(req, 'scrap/scrap.html', context)
    
    else:

        search=req.GET.get('search')
        press_form=req.POST.getlist('press')
        section_form=req.POST.getlist('section')
        user_article = Scrap.objects.filter(user=req.user).select_related().order_by('-created_date')
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
        
        articles = articles.filter(Q(article__headline__contains=search)|Q(article__content__contains=search)).select_related()
        
        now = datetime.datetime.now()
        dbarticles_today = articles.filter(created_date__gte = (now-datetime.timedelta(1)))
        dbarticles_this_week = articles.filter(created_date__range = (now-datetime.timedelta(8), now-datetime.timedelta(1)))
        dbarticles_last_week = articles.filter(created_date__range = (now-datetime.timedelta(15), now-datetime.timedelta(8)))
        dbarticles_long_ago = articles.filter(created_date__lt = (now-datetime.timedelta(15)))
        
        context={

            'dbarticles_today':dbarticles_today,
            'dbarticles_this_week':dbarticles_this_week,
            'dbarticles_last_week':dbarticles_last_week,
            'dbarticles_long_ago':dbarticles_long_ago,
            "q":search

            }
        return render(req, 'scrap/scrap.html', context)
    
