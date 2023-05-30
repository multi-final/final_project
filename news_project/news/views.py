from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from scrap.models import Scrap
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import json
from datetime import datetime as dt

def main(req):
    # 카테고리 미선택 시
    if req.method=='GET':
        # 생성일자순으로 정렬
        articles = Article.objects.all().select_related().order_by('-created_date')
        # 스크랩 기사 유무 확인
        scrap = {}
        if req.user.is_authenticated:
            scrap = Scrap.objects.filter(user=req.user).select_related().order_by('-article__created_date')
  
        # time_now = dt.now()
        articles_count=articles.count()
        # 페이지네이터로 분리
        paginator = Paginator(articles, 10)
        page = None
        
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        
        if scrap:
            return render(req, 'news/main.html', {'articles':articles, 'scrap':scrap , "articles_count":articles_count})
        else:
            return render(req, 'news/main.html', {'articles':articles, "articles_count":articles_count})
    # 카테고리 선택 시
    else:
        scrap = {}
        if req.user.is_authenticated:
            scrap = Scrap.objects.filter(user=req.user).select_related()
        
        press_form=req.POST.getlist('press')
        section_form=req.POST.getlist('section')
        # 선택한 카테고리 별로 필터링
        if not press_form and not section_form:
            articles = Article.objects.all().select_related()

        elif press_form and not section_form:
            press_form=list(map(int,press_form))
            articles = Article.objects.filter(press__in=press_form).select_related()
            if scrap:
                scrap = scrap.filter(article__press__in=press_form).select_related()

        elif not press_form and section_form:
            section_form=list(map(int,section_form))
            articles = Article.objects.filter(section__in=section_form).select_related()
            if scrap:
                scrap = scrap.filter(article__section__in=section_form).select_related()

        else:
            press_form=list(map(int,press_form))
            section_form=list(map(int,section_form))
            articles = Article.objects.filter(Q(press__in=press_form)&Q(section__in=section_form)).select_related()
            if scrap:
                scrap = scrap.filter(Q(article__press__in=press_form)&Q(article__section__in=section_form)).select_related()
        
        articles = articles.order_by('-created_date')
        articles_count=articles.count()

        paginator = Paginator(articles, 10)
        page = req.POST.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

        
        if scrap:
            scrap = scrap.order_by('-article__created_date')
            return render(req, 'news/main.html', {'articles':articles, "press_list":press_form, "section_list":section_form, "scrap":scrap, "articles_count":articles_count})
        
        else:
            return render(req, 'news/main.html', {'articles':articles, "press_list":press_form, "section_list":section_form, 'articles_count':articles_count})

def main_ajax(req):
        # 이전에 검색했던 카테고리 정보
        press_form=0
        section_form=0
        if req.POST.get('press') != None:
            press_form=json.loads(req.POST.get('press'))
        if req.POST.get('section') != None:
            section_form=json.loads(req.POST.get('section'))
        
        if not press_form and not section_form:
            post_list = Article.objects.all().select_related()
        
        elif press_form and not section_form:
            post_list = Article.objects.filter(press__in=press_form).select_related()
        
        elif not press_form and section_form:
            post_list = Article.objects.filter(section__in=section_form).select_related()
        
        else:
            post_list = Article.objects.filter(Q(press__in=press_form)&Q(section__in=section_form)).select_related()
        
        # 검색 기능을 사용했다면(search가 있는 경우)
        if req.POST.get('q'):
            search=req.POST.get('q')
            post_list = post_list.filter(Q(headline__contains=search)|Q(content__contains=search)).select_related()
        post_list = post_list.order_by('-created_date')

        paginator = Paginator(post_list, 10)
        page = int(req.POST.get('page'))
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = None

        context = {
            'articles':post_list,
            "press_list":press_form,
            "section_list":section_form
            }
        return render(req, 'news/main_ajax.html', context) #Ajax 로 호출하는 템플릿은 _ajax로 표시.

def search(req):
    if req.method=='GET':
        scrap={}
        if req.user.is_authenticated:
            scrap = Scrap.objects.filter(user=req.user).select_related()

        search=req.GET.get('search')

        if 'press=' in req.GET:
            press = json.loads(req.GET.get('press'))
        else:
            press=None

        if 'section=' in req.GET:
            section = json.loads(req.GET.get('section'))
        else:
            section=None

        if not press and not section:
            post_list = Article.objects.all().select_related()
            
        elif press and not section:
            post_list = Article.objects.filter(press__in=press).select_related()
            if scrap:
                scrap = scrap.filter(article__press__in=press).select_related()

        elif not press and section:
            post_list = Article.objects.filter(section__in=section).select_related()
            if scrap:
                scrap = scrap.filter(article__section__in=section).select_related()

        else:
            post_list = Article.objects.filter(Q(press__in=press)&Q(section__in=section)).select_related()
            if scrap:
                scrap = scrap.filter(Q(article__press__in=press)&Q(article__section__in=section)).select_related()
        
        post_list = post_list.filter(Q(headline__contains=search)|Q(content__contains=search)).select_related()
        
        post_list = post_list.order_by('-created_date')
        articles_count = post_list.count()
        paginator = Paginator(post_list, 10)
        page = req.POST.get('page')
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)

        if scrap:
            scrap = scrap.order_by('-article__created_date')
            return render(req, 'news/main.html', {'articles':post_list, "press_list":press, "section_list":section, "scrap":scrap, "q":search, "articles_count":articles_count})
            
        else:
            return render(req, 'news/main.html', {'articles':post_list, "press_list":press, "section_list":section, "q":search, "articles_count":articles_count})
    else:
        scrap={}
        if req.user.is_authenticated:
            scrap = Scrap.objects.filter(user=req.user).select_related()
        search=req.GET.get('search')
        press=req.POST.getlist('press')
        section=req.POST.getlist('section')
        if not press and not section:
            post_list = Article.objects.all().select_related()
            
        elif press and not section:
            post_list = Article.objects.filter(press__in=press).select_related()
            if scrap:
                scrap = scrap.filter(article__press__in=press).select_related()

        elif not press and section:
            post_list = Article.objects.filter(section__in=section).select_related()
            if scrap:
                scrap = scrap.filter(article__section__in=section).select_related()

        else:
            post_list = Article.objects.filter(Q(press__in=press)&Q(section__in=section)).select_related()
            if scrap:
                scrap = scrap.filter(Q(article__press__in=press)&Q(article__section__in=section)).select_related()
        
        post_list = post_list.filter(Q(headline__contains=search)|Q(content__contains=search)).select_related()
        
        post_list = post_list.order_by('-created_date')
        paginator = Paginator(post_list, 10)
        page = req.POST.get('page')
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)

        if scrap:
            scrap = scrap.order_by('-article__created_date')
            return render(req, 'news/main.html', {'articles':post_list, "press_list":press, "section_list":section, "scrap":scrap, "q":search, 'articles_count':articles_count})
            
        else:
            return render(req, 'news/main.html', {'articles':post_list, "press_list":press, "section_list":section, "q":search, 'articles_count':articles_count})
