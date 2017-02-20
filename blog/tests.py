#coding=utf-8
from django.test import TestCase
from django.utils import timezone
from blog.models import Article

class ArticleMethodTests(TestCase):
    def test_publish(self):
        'publish method should set the published_date as time of now'
        article1 = Article(author_id=1, title='nope', text='nullllll')
        article1.publish()
        time = timezone.now()
        self.assertGreaterEqual(time, article1.published_date)
        self.assertTrue(time - article1.published_date <= timezone.timedelta(hours=0.001))

    # def test_if_exsit(self):
    #     print Article.objects
    #     self.assertTrue(not Article(author_id=1, title='nope', text='nullllll').if_exist())

    #     #self.assertTrue(Article(author_id=1, title='zheshisha?', text='nullllll').if_exist())
    #     self.assertTrue(Article(author_id=1, title='11', text='nullllll').if_exist())
    #     self.assertTrue(Article(author_id=1, title='这又是啥', text='nullllll').if_exist())
