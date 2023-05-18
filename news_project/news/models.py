from django.db import models


class Press(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)


class Section(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)


class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    headline = models.CharField(max_length=128)
    press = models.ForeignKey(Press, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    writer = models.CharField(max_length=32)
    url = models.CharField(max_length=32)
    content = models.TextField()
    created_date = models.DateTimeField()
