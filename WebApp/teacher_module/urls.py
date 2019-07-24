from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path

from WebApp.teacher_module import views
from WebApp.teacher_module.views import LectureInfoListView

urlpatterns = (
    # urls for TodoTInfo
    path('', login_required(views.start), name='teacher_home'),
    path('', views.Dashboard, name='teacher_dashboard'),
    path('lectureinfolist/', LectureInfoListView.as_view(), name='lecture_list'),
    url(r'^lectureinfolist/(?P<pk>\d+)/$', views.lecturedetail, name='lecture_detail'),
)
urlpatterns += (
    # urls for LectureInfo
    path('lectureinfo/', views.LectureInfoListView.as_view(), name='teacher_lectureinfo_list'),
    path('lectureinfo/create/', views.LectureInfoCreateView.as_view(), name='teacher_lectureinfo_create'),
    path('lectureinfo/detail/<int:pk>/', views.LectureInfoDetailView.as_view(), name='teacher_lectureinfo_detail'),
    path('lectureinfo/update/<int:pk>/', views.LectureInfoUpdateView.as_view(), name='teacher_lectureinfo_update'),
)




