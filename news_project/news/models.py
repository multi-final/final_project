from django.db import models
import datetime


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
    
    def centence_split(self):
        centences = self.content.split('다.')
        centences.pop()
        return centences
        
# 예상 모델
class Keyword(models.Model):
    word = models.CharField(max_length=64)
    count = models.IntegerField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    date = models.DateTimeField()

    # json형식으로 보내기 위해 변환하는 함수
    def to_json(self):
    	return {
            "x": self.word,
            #"category": self.section,
            "value": self.count
        }
