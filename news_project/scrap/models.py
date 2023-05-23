from django.db import models
from news.models import Article
from users.models import User

# Create your models here.
class Scrap(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)