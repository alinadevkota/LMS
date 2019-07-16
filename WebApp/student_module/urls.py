from django.conf.urls import url
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
    path('coursesList/', views.coursesList, name="students_coursesList"),
    url(r'^courseList/(?P<pk>\d+)/$', views.coursedetail, name='course_detail'),
]

urlpatterns += (
    # urls for ChapterInfo
    #path('chapterinfo/', views.ChapterInfoListView.as_view(), name='chapterinfo_list'),
    #path('chapterinfo/create/', views.ChapterInfoCreateView.as_view(), name='chapterinfo_create'),
    path('lectureinfo/detail/<int:pk>/', views.LectureInfoDetailView.as_view(), name='studentcourse_detail'),
   # path('chapterinfo/update/<int:pk>/', views.ChapterInfoUpdateView.as_view(), name='chapterinfo_update'),
)
