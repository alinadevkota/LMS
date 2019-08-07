from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordContextMixin
# from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import ListView, CreateView, DetailView, UpdateView, FormView

from WebApp.forms import LectureInfoForm, ChapterInfoForm
from WebApp.models import LectureInfo, ChapterInfo, InningInfo
from survey.models import SurveyInfo


def start(request):
    """Start page with a documentation.
    """
    # return render(request,"start.html")
    return render(request, "teacher_module/homepage.html")


def Dashboard(request):
    return render(request, 'teacher_module/homepage.html', )


class LectureInfoListView(ListView):
    model = LectureInfo
    template_name = 'teacher_module/lectureinfo_list.html'
    paginate_by = 2

    def get_queryset(self):
        lectures = LectureInfo.objects.filter(Teacher_Code=self.request.user.id)
        if self.request.GET.get('query'):
            query = self.request.GET.get('query')
            if query:
                qs = lectures.filter(Lecture_Name__contains=query)
                if not len(qs):
                    messages.error(self.request, 'Search not found')
            qs = qs.order_by("-id")  # you don't need this if you set up your ordering on the model
            return qs
        else:
            return lectures
    # def get_queryset(self):
    #     qs = self.model.objects.all()


class LectureInfoCreateView(CreateView):
    model = LectureInfo
    form_class = LectureInfoForm
    template_name = 'teacher_module/lectureinfo_form.html'


class LectureInfoDetailView(DetailView):
    model = LectureInfo
    template_name = 'teacher_module/lectureinfo_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chapters'] = ChapterInfo.objects.filter(Lecture_Code=self.kwargs.get('pk'))
        return context

class LectureInfoUpdateView(UpdateView):
    model = LectureInfo
    form_class = LectureInfoForm
    template_name = 'teacher_module/lectureinfo_form.html'


class ChapterInfoListView(ListView):
    model = ChapterInfo
    template_name = 'teacher_module/chapterinfo_list.html'


class ChapterInfoCreateView(CreateView):
    model = ChapterInfo
    form_class = ChapterInfoForm
    template_name = 'teacher_module/chapterinfo_form.html'



class ChapterInfoDetailView(DetailView):
    model = ChapterInfo
    template_name = 'teacher_module/chapterinfo_detail.html'

def ChapterInfoBuildView(request):
    return render(request, 'teacher_module/lecturebuilder.html')

class ChapterInfoUpdateView(UpdateView):
    model = ChapterInfo
    form_class = ChapterInfoForm
    template_name = 'teacher_module/chapterinfo_form.html'


def ProfileView(request):
    return render(request, 'teacher_module/profile.html')


def makequery(request):
    # model=SurveyInfo
    Course=LectureInfo.objects.all()
    Session=InningInfo.objects.all()
    return render(request, 'teacher_module/makequery.html',{
    'courses': Course,
    'sessions': Session
})