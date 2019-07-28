from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path

from WebApp.teacher_module import views
from WebApp.teacher_module.views import LectureInfoListView

urlpatterns = (
    # urls for TodoTInfo
    path('', login_required(views.start), name='teacher_home'),
)
urlpatterns += (
    # urls for LectureInfo
    path('lectureinfo/', views.LectureInfoListView.as_view(), name='teacher_lectureinfo_list'),
    path('lectureinfo/create/', views.LectureInfoCreateView.as_view(), name='teacher_lectureinfo_create'),
    path('lectureinfo/detail/<int:pk>/', views.LectureInfoDetailView.as_view(), name='teacher_lectureinfo_detail'),
    path('lectureinfo/update/<int:pk>/', views.LectureInfoUpdateView.as_view(), name='teacher_lectureinfo_update'),
)

urlpatterns += (
    # urls for ChapterInfo
    path('chapterinfo/', views.ChapterInfoListView.as_view(), name='teacher_chapterinfo_list'),
    path('chapterinfo/create/', views.ChapterInfoCreateView.as_view(), name='teacher_chapterinfo_create'),
    path('chapterinfo/build/', views.ChapterInfoBuildView, name='teacher_chapterinfo_build'),

    path('chapterinfo/detail/<int:pk>/', views.ChapterInfoDetailView.as_view(), name='teacher_chapterinfo_detail'),
    path('chapterinfo/update/<int:pk>/', views.ChapterInfoUpdateView.as_view(), name='teacher_chapterinfo_update'),
)

urlpatterns += (
    # urls for Profile
    path('profile/', login_required(views.ProfileView), name='teacher_user_profile'),

)

urlpatterns += (
    # urls for Profile
    path('makequery/', login_required(views.makequery), name='teacher_makequery'),

)

