from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView

from news.models import Articles
from .forms import JarForm
from .models import JarModel, JarComment


class JarListView(ListView):
    model = JarModel
    template_name = 'Jar_lessons.html'
    paginate_by = 5
    context_object_name = 'JarList'

    def get_context_data(self, **kwargs):
        context = super(JarListView, self).get_context_data(**kwargs)
        list_exam = JarModel.objects.all()
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


def JarDetailView(request, slug):
    jar_details = get_object_or_404(JarModel, slug=slug)
    articles_top = Articles.objects.all().order_by('-view')[:6]

    if request.method == 'POST':
        comment_form = JarForm(request.POST)
        comment_form.save()
    else:
        comment_form = JarForm()

    comments = JarComment.objects.all()

    return render(request, 'jar_lesson.html', {'jar_details': jar_details,
                                               'articles_top': articles_top,
                                                  'comment_form': comment_form, 'comments': comments,
                                                  })

