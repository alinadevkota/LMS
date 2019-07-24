from django.shortcuts import render
from django.views.generic import ListView

from WebApp.models import LectureInfo


def start(request):
    """Start page with a documentation.
    """
    # return render(request,"start.html")
    return render(request, "teacher_module/homepage.html")


class LectureInfoListView(ListView):
    model = LectureInfo
    template_name = 'teacher_module/lectureinfo_list.html'


def lecturedetail(request, pk=''):
    return render(request, 'teacher_module/course_detail.html', {'Course': LectureInfo.objects.get(id=pk)})


def Dashboard(request):
    return render(request, 'teacher_module/homepage.html', )