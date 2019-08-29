from django.db import models

from djrichtextfield.models import RichTextField


class CModel(models.Model):
    titleC = models.CharField(max_length=400, verbose_name='Названия')
    textC = RichTextField()
    datesC = models.DateTimeField(auto_now=True)
    viewC = models.IntegerField(default=0)
    imgC = models.ImageField(upload_to='CLessonsImagae', default="default_value",verbose_name='Каритинка 260х180')
    C_like = models.IntegerField(default=0)
    C_dislike = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, verbose_name='URL')

    class Meta:
        ordering = ['-datesC']



    def __unicode__(self):
        return self.titleC

    def __str__(self):
        return self.titleC

    def get_absolute_url(self):
        return "/c_django//%s/" % (self.slug)