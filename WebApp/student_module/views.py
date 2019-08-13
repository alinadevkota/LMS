# from django.shortcuts import render
#
#
# def start(request):
#     """Start page with a documentation.
#     """
#     # return render(request,"start.html")
#     return render(request, "student_module/homepage.html")

from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView

from WebApp.models import LectureInfo, GroupMapping


def start(request):
    return render(request, 'student_module/dashboard.html')


def mycourse(request):
    return render(request, 'student_module/myCourse.html')


def quiz(request):
    return render(request, 'student_module/quiz.html')


def quizzes(request):
    return render(request, 'student_module/quizzes.html')


def calendar(request):
    return render(request, 'student_module/calendar.html')


# def coursedetail(request):
#     return render(request, 'student_module/course_detail.html')
# #
class LectureInfoListView(ListView):
    model = LectureInfo
    template_name = 'student_module/lectureinfo_list.html'


class LectureInfoDetailView(DetailView):
    model = LectureInfo
    template_name = 'student_module/lectureinfo_detail.html'


def ProfileView(request):
    return render(request, 'student_module/profile.html')


def questions_student(request):
    return render(request, 'student_module/questions_student.html')


def polls_student(request):
    return render(request, 'student_module/polls_student.html')


def polls_student_view(request):
    return render(request, 'student_module/polls_student_view.html')
