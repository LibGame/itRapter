from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView

from news.models import Articles
from .models import CModel


class CListView(ListView):
    model = CModel
    template_name = 'c_lessons.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(CListView, self).get_context_data(**kwargs)
        list_exam = CModel.objects.all()
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

        return context


def CDetailView(request, slug):
    c_details = get_object_or_404(CModel, slug=slug)
    articles_top = Articles.objects.all().order_by('-view')[:6]

    return render(request, 'c_lesson.html', {'c_details': c_details,
                                                  'articles_top': articles_top,
                                                  })
