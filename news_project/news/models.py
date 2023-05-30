from django.db import models


class Press(models.Model):
    id = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=32)


class Section(models.Model):
    id = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=32)


class Article(models.Model):
    headline = models.CharField(max_length=128)
    press = models.ForeignKey(Press, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    writer = models.CharField(max_length=128)
    url = models.CharField(max_length=64)
    content = models.TextField()
    created_date = models.DateTimeField()
