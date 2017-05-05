#coding=utf-8
from django.db import models
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name


class Article(models.Model):
    #author = models.ForeignKey('auth.User')
    author = models.CharField(max_length=50, default='踢叉叉')
    title = models.CharField(max_length=200, default='无标题')
    tags = models.ManyToManyField(Tag)
    text = models.TextField("正文")
    published_date = models.DateTimeField("发布时间", auto_now_add=True)
    last_modified_date = models.DateTimeField('最后一次修改时间', auto_now=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def if_exist(self):
        article = Article.objects.filter(title=self.title)
        return bool(article)

    def __unicode__(self):
        return self.title
