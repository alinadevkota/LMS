from django.urls import path

from WebApp.student_module import views

#
# urlpatterns = (
#     # urls for TodoTInfo
#     path('', login_required(views.start), name='student_home'),
# )
#
#
#

# from django.urls import path
# from . import views

urlpatterns = [
    path('', views.dashboard),
    path('dashboard/', views.dashboard, name="students_dashboard"),
    path('mycourse/', views.mycourse, name="students_mycourse"),
    path('quiz/', views.quiz, name="students_quiz"),
    path('quizzes/', views.quizzes, name="quiz_question"),
    path('calendar/', views.calendar, name="students_calendar"),
    path('course_detail/', views.coursedetail, name="course_detail"),
    path('coursesList/', views.coursesList, name="students_coursesList")
]
