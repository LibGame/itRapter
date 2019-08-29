# Generated by Django 2.2.3 on 2019-07-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameDjango', models.CharField(max_length=100)),
                ('textCommentDjango', models.TextField(default='')),
                ('datesCommentDjango', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-datesCommentDjango'],
            },
        ),
        migrations.CreateModel(
            name='DjangoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleDjango', models.CharField(max_length=400, verbose_name='Названия')),
                ('textDjango', models.TextField(verbose_name='Текст')),
                ('datesDjango', models.DateTimeField(auto_now=True)),
                ('viewDjango', models.IntegerField(default=0)),
                ('imgDjango', models.ImageField(default='default_value', upload_to='DjangoLessonsImagae')),
                ('django_like', models.IntegerField(default=0)),
                ('django_dislike', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-datesDjango'],
            },
        ),
    ]