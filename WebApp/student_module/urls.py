from django.contrib.auth.decorators import login_required
from django.urls import path

from WebApp.student_module import views

urlpatterns = (
    # urls for TodoTInfo
    path('', login_required(views.start), name='student_home'),
)



