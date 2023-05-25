from django.shortcuts import render, get_object_or_404, redirect
from .models import Section, Press, Article
from scrap.models import Scrap
from django.db.models import Q, F
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import json

def main(req):
    if req.method=='GET':
        articles = Article.objects.all().select_related()
        articles = articles.order_by('-created_date')
        scrap = {}
        if req.user.is_authenticated:
            scrap = Scrap.objects.filter(user=req.user).select_related().order_by('-article__created_date')
        
        paginator = Paginator(articles, 10)
        page = None
        
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        
        if scrap:
            return render(req, 'news/main.html', {'articles':articles, 'scrap':scrap})
        else:
            return render(req, 'news/main.html', {'articles':articles})
    else:
        scrap = {}
        if req.user.is_authenticated:
            scrap = Scrap.objects.filter(user=req.user).select_related()
        
        press_form=req.POST.getlist('press')
        section_form=req.POST.getlist('section')

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
            return render(req, 'news/main.html', {'articles':articles, "press_list":press_form, "section_list":section_form, "scrap":scrap})
        
        else:
            return render(req, 'news/main.html', {'articles':articles, "press_list":press_form, "section_list":section_form})

def main_ajax(req):
        press_form=list(map(int,req.POST.getlist('press')[0].split()))
        section_form=list(map(int,req.POST.getlist('section')[0].split()))
        
        if not press_form and not section_form:
            post_list = Article.objects.all().select_related()
        
        elif press_form and not section_form:
            post_list = Article.objects.filter(press__in=press_form).select_related()
        
        elif not press_form and section_form:
            post_list = Article.objects.filter(section__in=section_form).select_related()
        
        else:
            post_list = Article.objects.filter(Q(press__in=press_form)&Q(section__in=section_form)).select_related()
        
        post_list = post_list.order_by('-created_date')
        paginator = Paginator(post_list, 10)
        page = int(req.POST.get('page'))
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = None

        context = {'articles':post_list, "press_list":press_form, "section_list":section_form}
        return render(req, 'news/main_ajax.html', context) #Ajax 로 호출하는 템플릿은 _ajax로 표시.

