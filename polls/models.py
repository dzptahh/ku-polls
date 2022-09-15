# Create your models here.
import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('date end', default=None, null=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        current = timezone.now()
<<<<<<< HEAD
        return current - datetime.timedelta(days=1) <= self.pub_date <= current
=======
        return current >= self.pub_date
>>>>>>> a0a223bfc7f1d66cdcca052b31f3cedf87620a81

    def can_vote(self):
        current = timezone.now()
        if self.end_date is None:
            return self.pub_date <= current
        return self.pub_date <= current <= self.end_date


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
