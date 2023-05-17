from django.shortcuts import render, get_object_or_404, redirect
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile
# from django.http import HttpResponse

# id = models.IntegerField(primary_key=True)
#     headline = models.CharField(max_length=128)
#     press = models.OneToOneField(Press, on_delete=models.CASCADE)
# 		section = models.ForeignKey(Section, on_delete=models.CASCADE)
# 		writer = models.CharField(max_length=32)
# 		url = models.CharField(max_length=32)
#     content = models.TextField()
#     created_date = models.DateTimeField()

def main(req):
    if req.method=='GET':
        # content = Article.objects.filter()
        content=[]
        article_id = []
        for i in range(200):
            content.append(str(i) + 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam ipsa, perspiciatis ullam corporis consequatur cumque similique blanditiis beatae nobis nihil minus alias ratione delectus eos rem eligendi earum! Reprehenderit, soluta!')
            article_id.append(i)
        return render(req, 'news/main.html', {'articles':content, 'article_id':article_id})
    else:
        # select *
        # from Article
        # WHERE press_form IN (넘어온거 1번 OR  넘어온거 3번) and section_form IN (넘어온거 3번)
        
        # SELECT * FROM tCity WHERE name = '서울' AND (popu >= 100 OR area >= 700);

        # -- name(도시이름)이 '서울' 이나 '대구'에 속하는 경우, 모든 필드 출력
        # SELECT * FROM tCity WHERE name IN ('서울','대구');

        # sql
        # Article
        # select(홍길동 = (넘어온거) and section = (넘어온거))
        # content = Article.objects.filter(id=pk)
        # for press_form in press_forms(넘어온거) , section_form, press(모든 언론사), section
        # if(press_form in press or 한겨례 in press) and (section_form):
        press_form=req.POST.getlist('press')
        section_form=req.POST.getlist('section')
        content=[]
        article_id = []
        for i in range(200):
            content.append(str(i) + 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam ipsa, perspiciatis ullam corporis consequatur cumque similique blanditiis beatae nobis nihil minus alias ratione delectus eos rem eligendi earum! Reprehenderit, soluta!')
            article_id.append(i)
        return render(req, 'news/main.html', {'articles':content, 'article_id':article_id, 'press':press_form, 'section':section_form})

