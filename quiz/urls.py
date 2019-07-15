from django.urls import path

from quiz import views

try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url, path

from .views import QuizListView, QuizCreateView, CategoriesListView, \
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList, \
    QuizMarkingDetail, QuizTake, MCQuestionCreateView, TFQuestionCreateView, \
    EssayQuestionCreateView, MCQuestionUpdateView, TFQuestionUpdateView, EssayQuestionUpdateView

urlpatterns = [

    url(r'^$', view=QuizListView.as_view(), name='quiz_index'),

    url(r'^category/$', view=CategoriesListView.as_view(), name='quiz_category_list_all'),

    url(r'^category/(?P<category_name>[\w|\W-]+)/$', view=ViewQuizListByCategory.as_view(), name='quiz_category_list_matching'),

    url(r'^progress/$', view=QuizUserProgressView.as_view(), name='quiz_progress'),

    url(r'^marking/$', view=QuizMarkingList.as_view(), name='quiz_marking'),

    url(r'^marking/(?P<pk>[\d.]+)/$', view=QuizMarkingDetail.as_view(), name='quiz_marking_detail'),

     # passes variable 'quiz_name' to quiz_take view
    # url(r'^(?P<slug>[\w-]+)/$', view=QuizDetailView.as_view(), name='quiz_start_page'),

    url(r'^(?P<quiz_name>[\w-]+)/take/$', view=QuizTake.as_view(), name='quiz_question'),
]

urlpatterns += (
    # urls for LectureInfo
    # path('lectureinfo/', views.LectureInfoListView.as_view(), name='lectureinfo_list'),
    path('create/', QuizCreateView.as_view(), name='quiz_create'),

    path('mcquestion/', views.MCQuestionListView.as_view(), name='mcquestion_list'),
    path('mcquestion/create/', MCQuestionCreateView.as_view(), name='mcquestion_create'),
    path('mcquestion/update/<int:pk>', MCQuestionUpdateView.as_view(), name='mcquestion_update'),
    path('mcquestion/detail/<int:pk>/', views.MCQuestionDetailView.as_view(), name='mcquestion_detail'),
    path('mcquestion/delete/<int:pk>/', views.MCQuestionDeleteView, name='mcquestion_delete'),

    path('tfquestion/', views.TFQuestionListView.as_view(), name='tfquestion_list'),
    path('tfquestion/create/', TFQuestionCreateView.as_view(), name='tfquestion_create'),
    path('tfquestion/update/<int:pk>', TFQuestionUpdateView.as_view(), name='tfquestion_update'),
    path('tfquestion/detail/<int:pk>/', views.TFQuestionDetailView.as_view(), name='tfquestion_detail'),
    path('tfquestion/delete/<int:pk>/', views.TFQuestionDeleteView, name='tfquestion_delete'),

    path('essayquestion/', views.EssayQuestionListView.as_view(), name='essayquestion_list'),
    path('essayquestion/create/', EssayQuestionCreateView.as_view(), name='essayquestion_create'),
    path('essayquestion/update/<int:pk>', EssayQuestionUpdateView.as_view(), name='essayquestion_update'),
    path('essayquestion/detail/<int:pk>/', views.EssayQuestionDetailView.as_view(), name='essayquestion_detail'),
    path('essayquestion/delete/<int:pk>/', views.EssayQuestionDeleteView, name='essayquestion_delete'),

)


