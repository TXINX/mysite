#coding=utf-8
from django.db import models
from django.utils import timezone


class Article(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, default='无标题')
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def if_exist(self):
        print self.title
        article = Article.objects.filter(title=self.title)
        return bool(article)

    def __unicode__(self):
        return self.title
