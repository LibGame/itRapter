from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.db.models import F

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView, DetailView
from django.contrib import messages

from news.models import Articles
from .models import Programs




class ProgramsList(ListView):
    model = Programs
    template_name = 'programs/programms.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(ProgramsList, self).get_context_data(**kwargs)
        list_exam = Programs.objects.all()
        paginator = Paginator(list_exam, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
        context['programms_top'] = Articles.objects.all().order_by('-view')[:6]
        context['list_exams'] = file_exams
        return context

# class ProgramsDetail(DetailView):
#     model = Articles
#     template_name = 'programs/programm.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(ProgramsDetail, self).get_context_data(**kwargs)
#         context['top_art'] = Articles.objects.all().order_by('-view')[:10]
#         context['top_prog'] = Programs.objects.all().order_by('?')[:10]



def ProgramsDetail(request, slug):
     tag=None
     article_details = get_object_or_404(Programs,slug=slug)
     top_art = Articles.objects.all().order_by('-view')[:6]
     top_prog = Programs.objects.all().order_by('?')[:6]
     articles_top = Articles.objects.all().order_by('-view')[:6]

     return render(
         request,
         'programs/programm.html',
         {
            'article_details': article_details,
             'top_art':top_art,
             'articles_top':articles_top,
             'top_prog':top_prog,
             'tag': tag
         }
     )




def post_searchProgramm(request):
    queryProgramm = request.GET.get('searchProgramm')
    if queryProgramm:
        results = Programs.objects.filter(title__icontains=queryProgramm).order_by('-date')

        total_results = results.count()
        return render(request,
                      'news/posts.html',
                      {
                          'results': results,
                          'query': queryProgramm,
                          'total_results': total_results})
    else:
        messages.info(request, 'no results found for {}', format(queryProgramm))