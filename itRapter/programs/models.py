from django.db import models
from autoslug import AutoSlugField


# Create your models here.
from djrichtextfield.models import RichTextField


class Programs(models.Model):
    title = models.CharField(max_length=200 , verbose_name='titleProg')
    storyPrograms = RichTextField()
    previewPrograms = models.ImageField(upload_to='' , verbose_name='Каритинка 260х180')
    slug = models.SlugField(unique=True, verbose_name='URL')
    languegesPrograms = models.TextField(default='' , verbose_name='языки которые поддерживает программа')
    demandPrograms = models.TextField(default='' , verbose_name='Требования')
    memoryPrograms = models.TextField(default='' , verbose_name='Место, на жестком диске')
    uploadPrograms = models.TextField(default='' , verbose_name='Сыллка с установкой')
    date = models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ['-date']
        verbose_name = 'Программы'
        verbose_name_plural = 'Программы'


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/programms/%s/" % (self.slug)