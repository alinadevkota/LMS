from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'categoryinfo', api.CategoryInfoViewSet)
router.register(r'surveyinfo', api.SurveyInfoViewSet)
router.register(r'questioninfo', api.QuestionInfoViewSet)
router.register(r'optioninfo', api.OptionInfoViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for CategoryInfo
    path('categoryinfo/', views.CategoryInfoListView.as_view(), name='categoryinfo_list'),
    path('categoryinfo/create/', views.CategoryInfoCreateView.as_view(), name='categoryinfo_create'),
    path('categoryinfo/detail/<int:pk>/', views.CategoryInfoDetailView.as_view(), name='categoryinfo_detail'),
    path('categoryinfo/update/<int:pk>/', views.CategoryInfoUpdateView.as_view(), name='categoryinfo_update'),
)

urlpatterns += (
    # urls for SurveyInfo
    path('surveyinfo/', views.SurveyInfoListView.as_view(), name='surveyinfo_list'),
    path('surveyinfo/create/', views.SurveyInfoCreateView.as_view(), name='surveyinfo_create'),
    path('surveyinfo/detail/<int:pk>/', views.SurveyInfoDetailView.as_view(), name='surveyinfo_detail'),
    path('surveyinfo/update/<int:pk>/', views.SurveyInfoUpdateView.as_view(), name='surveyinfo_update'),
)

urlpatterns += (
    # urls for QuestionInfo
    path('questioninfo/', views.QuestionInfoListView.as_view(), name='questioninfo_list'),
    path('questioninfo/create/', views.QuestionInfoCreateView.as_view(), name='questioninfo_create'),
    path('questioninfo/detail/<int:pk>/', views.QuestionInfoDetailView.as_view(), name='questioninfo_detail'),
    path('questioninfo/update/<int:pk>/', views.QuestionInfoUpdateView.as_view(), name='questioninfo_update'),
)

urlpatterns += (
    # urls for OptionInfo
    path('optioninfo/', views.OptionInfoListView.as_view(), name='optioninfo_list'),
    path('optioninfo/create/', views.OptionInfoCreateView.as_view(), name='optioninfo_create'),
    path('optioninfo/detail/<int:pk>/', views.OptionInfoDetailView.as_view(), name='optioninfo_detail'),
    path('optioninfo/update/<int:pk>/', views.OptionInfoUpdateView.as_view(), name='optioninfo_update'),
)

