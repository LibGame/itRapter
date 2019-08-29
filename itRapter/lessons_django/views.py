from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView

from news.models import Articles
from .forms import DjangoForm
from .models import DjangoModel, DjangoComment


class DjangoListView(ListView):
    model = DjangoModel
    template_name = 'django_lessons.html'
    paginate_by = 5
    

    def get_context_data(self, **kwargs):
        context = super(DjangoListView, self).get_context_data(**kwargs)
        list_exam = DjangoModel.objects.all()
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

def DjangoDetailView(request, slug):

    django_details = get_object_or_404(DjangoModel, slug=slug)
    articles_top = Articles.objects.all().order_by('-view')[:6]

    if request.method == 'POST':
        comment_form = DjangoForm(request.POST)
        comment_form.save()
    else:
        comment_form = DjangoForm()

    comments = DjangoComment.objects.all()

    return render(request, 'django_lesson.html', {'django_details': django_details,
                                                  'articles_top': articles_top,
                                              'comment_form': comment_form, 'comments': comments,
                                              })


