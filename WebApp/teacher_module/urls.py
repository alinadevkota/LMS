from django.contrib.auth.decorators import login_required
from django.urls import path

from WebApp.teacher_module import views

urlpatterns = (
    # urls for TodoTInfo
    path('', login_required(views.start), name='teacher_home'),
    path('lecturelist/', views.lecturelist, name='lecture_list')
)



