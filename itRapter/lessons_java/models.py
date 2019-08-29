from django.db import models

# Create your models here.
from djrichtextfield.models import RichTextField


class JarModel(models.Model):
    titleJar = models.CharField(max_length=400, verbose_name='Названия')
    textJar = RichTextField()
    datesJar = models.DateTimeField(auto_now=True)
    viewJar = models.IntegerField(default=0)
    imgJar = models.ImageField(upload_to='JavaLessonsImagae', default="default_value",verbose_name='Каритинка 260х180')
    jar_like = models.IntegerField(default=0)
    jar_dislike = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, verbose_name='URL')

    class Meta:
        ordering = ['-datesJar']


    def __unicode__(self):
        return self.titleJar

    def __str__(self):
        return self.titleJar

    def get_absolute_url(self):
        return "/lessons_jar//%s/" % (self.slug)


class JarComment (models.Model):
    nameJar = models.CharField(max_length=100)
    textCommentJar = models.TextField(default='')
    datesCommentJar = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-datesCommentJar']

    def __str__(self):
        return self.nameJar