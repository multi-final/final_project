from django.db import models
import datetime


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

    def since_time(self):
        time_diff = datetime.datetime.now() - self.created_date
        days = time_diff.days
        hours, pre_sec = divmod(time_diff.seconds,3600)
        minutes = pre_sec // 60

        if days >= 1:
            return f'{days}일 전'
        elif hours >= 1:
            return f'{hours}시간 전'
        elif minutes >= 1:
            return f'{minutes}분 전'
        else:
            return '방금 전'
        