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
from WebApp.models import LectureInfo


def dashboard(request):
    return render(request, 'student_module/dashboard.html')


def mycourse(request):
    return render(request, 'student_module/myCourse.html')


def quiz(request):
    return render(request, 'student_module/quiz.html')


def quizzes(request):
    return render(request, 'student_module/quizzes.html')


def calendar(request):
    return render(request, 'student_module/calendar.html')

def coursedetail(request):
    return render(request, 'student_module/course_detail.html')



def coursesList(request):
    return render(request, 'student_module/coursesList.html', {'Courses': LectureInfo.objects.all()})
