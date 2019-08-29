import datetime

from django.contrib import messages, auth
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from taggit.models import Tag
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from .models import Articles, PageHit, CommentModel
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.db.models import Count

from django.http import HttpResponseRedirect, HttpResponse, response
from django.shortcuts import render

from django.db.models import F
from .forms import Comments


class ArticleIndex(ListView):
    model = Articles
    template_name = 'news/posts.html'
    paginate_by = 6


    def get_context_data(self, **kwargs):
        context = super(ArticleIndex, self).get_context_data(**kwargs)
        list_exam = Articles.objects.all()
        paginator = Paginator(list_exam, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)

        context['list_exams'] = file_exams
        context['articles_top'] = Articles.objects.all().order_by('-view')[:6]
        context['articles_tag'] = Articles.objects.all()
        context['tag'] = tag = None
        return context


def post_list(request):
    object_list = Articles.published.all()
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'news/home.html',
                  {'page': page,
                   'posts': posts})


def ArticleDetailView(request, slug):
    tag=None
    Articles.objects.filter(slug=slug).update(view=F('view') + 1)
    article_details = Articles.objects.filter(slug=slug).first()
    articles_top= Articles.objects.all().order_by('-view')[:6]
    if request.method == 'POST':
        comment_form = Comments(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('some-view-name')
    else:
        comment_form = Comments()
    comments = CommentModel.objects.all()
    return render(
        request,
        'news/post.html',
        {
           'article_details': article_details,
           'comment_form': comment_form,
           'articles_top': articles_top,
           'comments': comments,
            'tag': tag
        }
    )

def post_search(request):
    query = request.GET.get('search')
    if query:
        results = Articles.objects.filter(title__icontains=query).order_by('-date')

        total_results = results.count()
        return render(request,
                      'news/posts.html',
                      {
                          'results': results,
                          'query': query,
                          'total_results': total_results})
    else:
        messages.info(request, 'no results found for {}', format(query))




def tags_list(request, tag_slug=None):
    object_list = Articles.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'news/list.html', {'page': page,
                                              'posts': posts,
                                              'tag': tag})







def post_list(request, tag_slug=None):
    object_list = Articles.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'news/list.html', {'page': page,
                                                   'posts': posts,
                                                   'tag': tag})







def addlike(request, slug):
    if slug in request.COOKIES:
        response = HttpResponseRedirect('/')
    else:


        article = get_object_or_404(Articles, id=slug)  # возвращает id статьи или 404.
        article.article_like += 1  # Прибавляет единицу к article_likes
        article.save()  # сохраняет
        response = HttpResponseRedirect('/')
        response.set_cookie(str(slug), "like")
        return response  # делает редирект на ту же страницу


def adddislike(request, slug):
    if slug in request.COOKIES:
        response = HttpResponseRedirect('/')
    else:


        article = get_object_or_404(Articles, id=slug)  # возвращает id статьи или 404.
        article.article_dislike += 1  # Прибавляет единицу к article_likes
        article.save()  # сохраняет
        response = HttpResponseRedirect('/')
        response.set_cookie(str(slug), "dislike")
        return response  # делает редирект на ту же страницу



def aboutUs(request):
    return render(request,'news/aboutUs.html')



