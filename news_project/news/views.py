from django.shortcuts import render, get_object_or_404, redirect
from .models import Section, Press, Article
from django.db.models import Q
# from django.core.files.storage import default_storage
# from django.core.files.base import articleFile
# from django.http import HttpResponse

# id = models.IntegerField(primary_key=True)
#     headline = models.CharField(max_length=128)
#     press = models.OneToOneField(Press, on_delete=models.CASCADE)
# 		section = models.ForeignKey(Section, on_delete=models.CASCADE)
# 		writer = models.CharField(max_length=32)
# 		url = models.CharField(max_length=32)
#     article = models.TextField()
#     created_date = models.DateTimeField()

def main(req):
    if req.method=='GET':
        articles = Article.objects.all().select_related()
        return render(req, 'news/main.html', {'articles':articles})
    else:
        press_form=req.POST.getlist('press')
        section_form=req.POST.getlist('section')
        if not press_form and not section_form:
            articles = Article.objects.all().select_related()
        elif press_form and not section_form:
            press_form=list(map(int,press_form))
            articles = Article.objects.filter(press__in=press_form).select_related()
        elif not press_form and section_form:
            section_form=list(map(int,section_form))
            articles = Article.objects.filter(section__in=section_form).select_related()
        else:
            articles = Article.objects.filter(Q(press__in=press_form)&Q(section__in=section_form)).select_related()

        return render(req, 'news/main.html', {'articles':articles})
