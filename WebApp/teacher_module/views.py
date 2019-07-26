from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordContextMixin
from django.core.checks import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import ListView, CreateView, DetailView, UpdateView, FormView

from WebApp.forms import LectureInfoForm, ChapterInfoForm
from WebApp.models import LectureInfo, ChapterInfo


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


class LectureInfoCreateView(CreateView):
    model = LectureInfo
    form_class = LectureInfoForm
    template_name = 'teacher_module/lectureinfo_form.html'


class LectureInfoDetailView(DetailView):
    model = LectureInfo
    template_name = 'teacher_module/lectureinfo_detail.html'


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
