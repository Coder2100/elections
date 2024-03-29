from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date puplished')

    def __str__(self):
        return f"{self.question_text}"

    #recently published poll
   # was_published_recently() returns False for questions whose pub_date is older than 1 day.
    #
    def test_was_published_recently_with_old_question(self):
   # def was_published_recently(self):
        time = timezone.now() -datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        #now = timezone.now()
        self.assertIs(old_question.was_published_recently(), False)
        #return now -datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def test_was_published_recently_with_recent_question(self):
        #was_published_recently() returns True for questions whose pub_date is within the last day
        time = timezone.now() -datetime.timedelta(ours=23, minutes=59,seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.choice_text}"