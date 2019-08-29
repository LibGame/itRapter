from django.db import models

# Create your models here.
from djrichtextfield.models import RichTextField


class DjangoModel(models.Model):
    titleDjango = models.CharField(max_length=400, verbose_name='Названия')
    textDjango = RichTextField()
    datesDjango = models.DateTimeField(auto_now=True)
    viewDjango = models.IntegerField(default=0)
    imgDjango = models.ImageField(upload_to='DjangoLessonsImagae', default="default_value",verbose_name='Каритинка 260х180')
    django_like = models.IntegerField(default=0)
    django_dislike = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, verbose_name='URL')

    class Meta:
        ordering = ['-datesDjango']



    def __unicode__(self):
        return self.titleDjango

    def __str__(self):
        return self.titleDjango

    def get_absolute_url(self):
        return "/lessons_django//%s/" % (self.slug)

class DjangoComment (models.Model):
    nameDjango = models.CharField(max_length=100)
    textCommentDjango = models.TextField(default='')
    datesCommentDjango = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-datesCommentDjango']

    def __str__(self):
        return self.nameDjango