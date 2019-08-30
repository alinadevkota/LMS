from django.conf.urls import url
from django.urls import path
from django.contrib.auth.decorators import login_required

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

urlpatterns = (
    # urls for TodoTInfo
    path('', login_required(views.start), name='student_home'),
)

urlpatterns += (
    # path('mycourse/', views.mycourse, name="students_mycourse"),
    path('quiz/', views.quiz, name="students_quiz"),
    path('quizzes/', views.quizzes, name="quiz_question"),
    path('calendar/', views.calendar, name="students_calendar"),

)

urlpatterns += (
    # urls for LectureInfo
    path('courseinfo/', views.LectureInfoListView.as_view(),
         name='student_lectureinfo_list'),
    path('courseinfo/mycourses', views.MyCoursesListView.as_view(),
         name='student_mycourses_list'),
    path('courseinfo/detail/<int:pk>/', views.LectureInfoDetailView.as_view(),
         name='student_lectureinfo_detail'),
)

urlpatterns += (
    # urls for ChapterInfo
    path('courseinfo/<int:course>/chapterinfo/', views.ChapterInfoListView.as_view(), name='student_chapterinfo_list'),
    path('courseinfo/<int:course>/chapterinfo/<int:pk>/', views.ChapterInfoDetailView.as_view(),
         name='student_chapterinfo_detail'),
)

urlpatterns += (
    # urls for AssignmentInfo
    path('courseinfo/<int:course>/chapterinfo/<int:chapter>/assignmentinfo/<int:pk>/',
    views.AssignmentInfoDetailView.as_view(),
        name='student_assignmentinfo_detail'),
)

urlpatterns += (
    # urls for Profile
    path('profile/', login_required(views.ProfileView),
         name='student_user_profile'),
)

urlpatterns += (
    path('questions_student/', views.questions_student, name="questions_student"),
)

urlpatterns += (
    path('polls_student/', views.polls_student, name="polls_student"),
)

urlpatterns += (
    path('polls_student_view/', views.polls_student_view,
         name="polls_student_view"),
)
