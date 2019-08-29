from django.db import models
from djrichtextfield.models import RichTextField
from djrichtextfield.widgets import RichTextWidget
from taggit.managers import TaggableManager
from autoslug import AutoSlugField
from django.utils import timezone
from uuslug import slugify

class Articles(models.Model):
    title = models.CharField(max_length= 200)
    post = RichTextField()
    slug = models.SlugField(unique=True, verbose_name='URL')
    date = models.DateTimeField()
    img = models.ImageField(upload_to='', default="default_value",verbose_name='Каритинка 260х180')
    tags = TaggableManager()
    article_like = models.IntegerField(default='0')
    article_dislike = models.IntegerField(default='0')
    view = models.IntegerField(default='0')
    datesArticle = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-datesArticle']


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/news/%s/" % (self.slug)


class PageHit(models.Model):
    url = models.CharField(unique=True, max_length=3000)
    count = models.PositiveIntegerField(default=0)


class CommentModel(models.Model):
    name = models.CharField(max_length=100)
    text = RichTextField()
    dates = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-dates']

    def __str__(self):
        return self.name