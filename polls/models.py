# Create your models here.
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    """Question model"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('date end', default=None, null=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """Check that question was published recently"""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        current = timezone.now()
        return current - datetime.timedelta(days=1) <= self.pub_date <= current

    def can_vote(self):
        """Check that question is published"""
        current = timezone.now()
        return current >= self.pub_date

    def can_vote(self):
        """For check that question user can vote"""
        current = timezone.now()
        if self.end_date is None:
            return self.pub_date <= current
        return self.pub_date <= current <= self.end_date


class Choice(models.Model):
    """Choice model"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    # votes = models.IntegerField(default=0) # no neet in iteration3

    def __str__(self):
        return self.choice_text

    @property
    def votes(self):
        return Vote.objects.filter(choice=self).count()


class Vote(models.Model):
    """Vote model"""
    objects = None
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
