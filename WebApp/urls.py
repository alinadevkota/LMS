from django.conf.urls import url
# from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()

# router.register(r'profile', api.ProfileViewSet)
router.register(r'centerinfo', api.CenterInfoViewSet)
router.register(r'memberinfo', api.MemberInfoViewSet)
router.register(r'lectureinfo', api.LectureInfoViewSet)
router.register(r'chapterinfo', api.ChapterInfoViewSet)
router.register(r'chaptercontentsinfo', api.ChapterContentsInfoViewSet)
router.register(r'chaptermissoncheckcard', api.ChapterMissonCheckCardViewSet)
router.register(r'chaptermissoncheckitem', api.ChapterMissonCheckItemViewSet)
router.register(r'inninginfo', api.InningInfoViewSet)
# router.register(r'omrquestioninfo', api.OmrQuestionInfoViewSet)
router.register(r'quizinfo', api.QuizInfoViewSet)
router.register(r'assignassignmentinfo', api.AssignAssignmentInfoViewSet)
router.register(r'assignquestioninfo', api.AssignQuestionInfoViewSet)
router.register(r'boardinfo', api.BoardInfoViewSet)
router.register(r'boardcontentinfo', api.BoardContentInfoViewSet)
router.register(r'inninggroup', api.InningGroupViewSet)
router.register(r'chaptercontentmedia', api.ChapterContentMediaViewSet)
router.register(r'chapterimginfo', api.ChapterImgInfoViewSet)
router.register(r'chaptermissoncheck', api.ChapterMissonCheckViewSet)
router.register(r'chapterwrite', api.ChapterWriteViewSet)
router.register(r'groupmapping', api.GroupMappingViewSet)
router.register(r'assignmentinfo', api.AssignmentInfoViewSet)
router.register(r'learningnote', api.LearningNoteViewSet)
router.register(r'lectureubtinfo', api.LectureUbtInfoViewSet)
router.register(r'lessoninfo', api.LessonInfoViewSet)
router.register(r'lessonlog', api.LessonLogViewSet)
router.register(r'membergroup', api.MemberGroupViewSet)
router.register(r'messageinfo', api.MessageInfoViewSet)
# router.register(r'omranswerinfo', api.OmrAnswerInfoViewSet)
# router.register(r'omrassigninfo', api.OmrAssignInfoViewSet)
# router.register(r'omrexampleinfo', api.OmrExampleInfoViewSet)
router.register(r'assignanswerinfo', api.AssignAnswerInfoViewSet)
# router.register(r'qanswerlog', api.QAnswerLogViewSet)
router.register(r'qexampleinfo', api.QExampleInfoViewSet)
router.register(r'questioninfo', api.QuestionInfoViewSet)
router.register(r'quizanswerinfo', api.QuizAnswerInfoViewSet)
router.register(r'quizexampleinfo', api.QuizExampleInfoViewSet)
router.register(r'scheduleinfo', api.ScheduleInfoViewSet)
router.register(r'talkmember', api.TalkMemberViewSet)
router.register(r'talkroom', api.TalkRoomViewSet)
router.register(r'talkmessage', api.TalkMessageViewSet)
router.register(r'talkmessageread', api.TalkMessageReadViewSet)
router.register(r'todoinfo', api.TodoInfoViewSet)
router.register(r'todotinfo', api.TodoTInfoViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
    url(r'^$', views.start, name='start'),
    url(r'^login/$', views.login, {'template_name': 'registration/login.html',
                                   'redirect_authenticated_user': True}, name='login'),

    url(r'^.*logout/$', views.logout, {'template_name': 'registration/logout.html', 'next_page': '/'}, name='logout'),

    url(r'^.*editprofile/$', views.editprofile, name='editprofile'),

    url(r'^successlogin/$', views.loginsuccess, name='loginsuccess'),

    url(r'^.*register/$', views.register.as_view(), name='register'),
)

# urlpatterns += (
#     # urls for Profile
#     path('profile/', views.ProfileListView.as_view(), name='profile_list'),
#     path('profile/create/', views.ProfileCreateView.as_view(), name='profile_create'),
#     path('profile/detail/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
#     path('profile/update/<int:pk>/', views.ProfileUpdateView.as_view(), name='profile_update'),
# )

urlpatterns += (
    # urls for Profile
    path('profile/', login_required(views.ProfileView), name='user_profile'),
    path('change-password/', views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('change-password/<int:pk>/', views.change_password_others),
)

urlpatterns += (
    # urls for CenterInfo
    path('centerinfo/', login_required(views.CenterInfoListView.as_view()), name='centerinfo_list'),
    path('centerinfo/create/', login_required(views.CenterInfoCreateView.as_view()), name='centerinfo_create'),
    path('centerinfo/detail/<int:pk>/', views.CenterInfoDetailView.as_view(), name='centerinfo_detail'),
    path('centerinfo/update/<int:pk>/', views.CenterInfoUpdateView.as_view(), name='centerinfo_update'),
    path('centerinfo/delete/<int:pk>/', views.CenterInfoDeleteView, name='centerinfo_delete'),
    # url(r'^deletethread/(?P<pk>\d+)/$', views.thread_delete, name='smart_forum_thread_delete'),

)

urlpatterns += (
    # urls for MemberInfo
    path('memberinfo/', views.MemberInfoListView.as_view(), name='memberinfo_list'),
    path('memberinfo/create/', views.MemberInfoCreateView.as_view(), name='memberinfo_create'),
    path('memberinfo/detail/<int:pk>/', views.MemberInfoDetailView.as_view(), name='memberinfo_detail'),
    path('memberinfo/update/<int:pk>/', views.MemberInfoUpdateView.as_view(), name='memberinfo_update'),
    path('memberinfo/delete/<int:pk>/', views.MemberInfoDeleteView.as_view(), name='memberinfo_delete'),
)

urlpatterns += (
    # urls for LectureInfo
    path('courseinfo/', views.LectureInfoListView.as_view(), name='lectureinfo_list'),
    path('courseinfo/create /', views.LectureInfoCreateView.as_view(), name='lectureinfo_create'),
    path('courseinfo/<int:pk>/', views.LectureInfoDetailView.as_view(), name='lectureinfo_detail'),
    path('courseinfo/edit/<int:pk>/', views.LectureInfoUpdateView.as_view(), name='lectureinfo_update'),
)

urlpatterns += (
    # urls for ChapterInfo
    path('courseinfo/<int:course>/chapterinfo/', views.ChapterInfoListView.as_view(), name='chapterinfo_list'),
    path('courseinfo/<int:course>/create/', views.ChapterInfoCreateView.as_view(), name='chapterinfo_create'),
    path('courseinfo/<int:course>/chapterinfo/<int:pk>/', views.ChapterInfoDetailView.as_view(), name='chapterinfo_detail'),
    path('courseinfo/<int:course>/chapterinfo/<int:pk>/edit/', views.ChapterInfoUpdateView.as_view(), name='chapterinfo_update'),
)

urlpatterns += (
    # urls for ChapterContentsInfo
    path('chaptercontentsinfo/', views.ChapterContentsInfoListView.as_view(), name='chaptercontentsinfo_list'),
    path('chaptercontentsinfo/create/', views.ChapterContentsInfoCreateView.as_view(),
         name='chaptercontentsinfo_create'),
    path('chaptercontentsinfo/detail/<int:pk>/', views.ChapterContentsInfoDetailView.as_view(),
         name='chaptercontentsinfo_detail'),
    path('chaptercontentsinfo/update/<int:pk>/', views.ChapterContentsInfoUpdateView.as_view(),
         name='chaptercontentsinfo_update'),
)

urlpatterns += (
    # urls for ChapterMissonCheckCard
    path('chaptermissoncheckcard/', views.ChapterMissonCheckCardListView.as_view(), name='chaptermissoncheckcard_list'),
    path('chaptermissoncheckcard/create/', views.ChapterMissonCheckCardCreateView.as_view(),
         name='chaptermissoncheckcard_create'),
    path('chaptermissoncheckcard/detail/<int:pk>/', views.ChapterMissonCheckCardDetailView.as_view(),
         name='chaptermissoncheckcard_detail'),
    path('chaptermissoncheckcard/update/<int:pk>/', views.ChapterMissonCheckCardUpdateView.as_view(),
         name='chaptermissoncheckcard_update'),
)

urlpatterns += (
    # urls for ChapterMissonCheckItem
    path('chaptermissoncheckitem/', views.ChapterMissonCheckItemListView.as_view(), name='chaptermissoncheckitem_list'),
    path('chaptermissoncheckitem/create/', views.ChapterMissonCheckItemCreateView.as_view(),
         name='chaptermissoncheckitem_create'),
    path('chaptermissoncheckitem/detail/<int:pk>/', views.ChapterMissonCheckItemDetailView.as_view(),
         name='chaptermissoncheckitem_detail'),
    path('chaptermissoncheckitem/update/<int:pk>/', views.ChapterMissonCheckItemUpdateView.as_view(),
         name='chaptermissoncheckitem_update'),
)

urlpatterns += (
    # urls for InningInfo
    path('inninginfo/', views.InningInfoListView.as_view(), name='inninginfo_list'),
    path('inninginfo/create/', views.InningInfoCreateView.as_view(), name='inninginfo_create'),
    path('inninginfo/detail/<int:pk>/', views.InningInfoDetailView.as_view(), name='inninginfo_detail'),
    path('inninginfo/update/<int:pk>/', views.InningInfoUpdateView.as_view(), name='inninginfo_update'),
)

# urlpatterns += (
#     # urls for OmrQuestionInfo
#     path('omrquestioninfo/', views.OmrQuestionInfoListView.as_view(), name='omrquestioninfo_list'),
#     path('omrquestioninfo/create/', views.OmrQuestionInfoCreateView.as_view(), name='omrquestioninfo_create'),
#     path('omrquestioninfo/detail/<int:pk>/', views.OmrQuestionInfoDetailView.as_view(), name='omrquestioninfo_detail'),
#     path('omrquestioninfo/update/<int:pk>/', views.OmrQuestionInfoUpdateView.as_view(), name='omrquestioninfo_update'),
# )

urlpatterns += (
    # urls for QuizInfo
    path('quizinfo/', views.QuizInfoListView.as_view(), name='quizinfo_list'),
    path('quizinfo/create/', views.QuizInfoCreateView.as_view(), name='quizinfo_create'),
    path('quizinfo/detail/<int:pk>/', views.QuizInfoDetailView.as_view(), name='quizinfo_detail'),
    path('quizinfo/update/<int:pk>/', views.QuizInfoUpdateView.as_view(), name='quizinfo_update'),
)

urlpatterns += (
    # urls for HomeworkInfo
    path('assignmentinfo/', views.AssignmentInfoListView.as_view(), name='assignmentinfo_list'),
    path('assignmentinfo/create/', views.AssignmentInfoCreateView.as_view(), name='assignmentinfo_create'),
    path('assignmentinfo/detail/<int:pk>/', views.AssignmentInfoDetailView.as_view(), name='assignmentinfo_detail'),
    path('assignmentinfo/update/<int:pk>/', views.AssignmentInfoUpdateView.as_view(), name='assignmentinfo_update'),
)

urlpatterns += (
    # urls for QuestionInfo
    path('questioninfo/', views.QuestionInfoListView.as_view(), name='questioninfo_list'),
    path('questioninfo/create/', views.QuestionInfoCreateView.as_view(), name='questioninfo_create'),
    path('questioninfo/detail/<int:pk>/', views.QuestionInfoDetailView.as_view(), name='questioninfo_detail'),
    path('questioninfo/update/<int:pk>/', views.QuestionInfoUpdateView.as_view(), name='questioninfo_update'),
)

urlpatterns += (
    # urls for AssignHomeworkInfo
    path('assignassignmentinfo/', views.AssignAssignmentInfoListView.as_view(), name='assignassignmentinfo_list'),
    path('assignassignmentinfo/create/', views.AssignAssignmentInfoCreateView.as_view(),
         name='assignassignmentinfo_create'),
    path('assignassignmentinfo/detail/<int:pk>/', views.AssignAssignmentInfoDetailView.as_view(),
         name='assignassignmentinfo_detail'),
    path('assignassignmentinfo/update/<int:pk>/', views.AssignAssignmentInfoUpdateView.as_view(),
         name='assignassignmentinfo_update'),
)

urlpatterns += (
    # urls for AssignQuestionInfo
    path('assignquestioninfo/', views.AssignQuestionInfoListView.as_view(), name='assignquestioninfo_list'),
    path('assignquestioninfo/create/', views.AssignQuestionInfoCreateView.as_view(), name='assignquestioninfo_create'),
    path('assignquestioninfo/detail/<int:pk>/', views.AssignQuestionInfoDetailView.as_view(),
         name='assignquestioninfo_detail'),
    path('assignquestioninfo/update/<int:pk>/', views.AssignQuestionInfoUpdateView.as_view(),
         name='assignquestioninfo_update'),
)

urlpatterns += (
    # urls for AssignAnswerInfo
    path('assignanswerinfo/', views.AssignAnswerInfoListView.as_view(), name='assignanswerinfo_list'),
    path('assignanswerinfo/create/', views.AssignAnswerInfoCreateView.as_view(), name='assignanswerinfo_create'),
    path('assignanswerinfo/detail/<int:pk>/', views.AssignAnswerInfoDetailView.as_view(), name='assignanswerinfo_detail'),
    path('assignanswerinfo/update/<int:pk>/', views.AssignAnswerInfoUpdateView.as_view(), name='assignanswerinfo_update'),
)


urlpatterns += (
    # urls for BoardInfo
    path('boardinfo/', views.BoardInfoListView.as_view(), name='boardinfo_list'),
    path('boardinfo/create/', views.BoardInfoCreateView.as_view(), name='boardinfo_create'),
    path('boardinfo/detail/<int:pk>/', views.BoardInfoDetailView.as_view(), name='boardinfo_detail'),
    path('boardinfo/update/<int:pk>/', views.BoardInfoUpdateView.as_view(), name='boardinfo_update'),
)

urlpatterns += (
    # urls for BoardContentInfo
    path('boardcontentinfo/', views.BoardContentInfoListView.as_view(), name='boardcontentinfo_list'),
    path('boardcontentinfo/create/', views.BoardContentInfoCreateView.as_view(), name='boardcontentinfo_create'),
    path('boardcontentinfo/detail/<int:pk>/', views.BoardContentInfoDetailView.as_view(),
         name='boardcontentinfo_detail'),
    path('boardcontentinfo/update/<int:pk>/', views.BoardContentInfoUpdateView.as_view(),
         name='boardcontentinfo_update'),
)

urlpatterns += (
    # urls for InningGroup
    path('inninggroup/', views.InningGroupListView.as_view(), name='inninggroup_list'),
    path('inninggroup/create/', views.InningGroupCreateView.as_view(), name='inninggroup_create'),
    path('inninggroup/detail/<int:pk>/', views.InningGroupDetailView.as_view(), name='inninggroup_detail'),
    path('inninggroup/update/<int:pk>/', views.InningGroupUpdateView.as_view(), name='inninggroup_update'),
)

urlpatterns += (
    # urls for ChapterContentMedia
    path('chaptercontentmedia/', views.ChapterContentMediaListView.as_view(), name='chaptercontentmedia_list'),
    path('chaptercontentmedia/create/', views.ChapterContentMediaCreateView.as_view(),
         name='chaptercontentmedia_create'),
    path('chaptercontentmedia/detail/<int:pk>/', views.ChapterContentMediaDetailView.as_view(),
         name='chaptercontentmedia_detail'),
    path('chaptercontentmedia/update/<int:pk>/', views.ChapterContentMediaUpdateView.as_view(),
         name='chaptercontentmedia_update'),
)

urlpatterns += (
    # urls for ChapterImgInfo
    path('chapterimginfo/', views.ChapterImgInfoListView.as_view(), name='chapterimginfo_list'),
    path('chapterimginfo/create/', views.ChapterImgInfoCreateView.as_view(), name='chapterimginfo_create'),
    path('chapterimginfo/detail/<int:pk>/', views.ChapterImgInfoDetailView.as_view(), name='chapterimginfo_detail'),
    path('chapterimginfo/update/<int:pk>/', views.ChapterImgInfoUpdateView.as_view(), name='chapterimginfo_update'),
)

urlpatterns += (
    # urls for ChapterMissonCheck
    path('chaptermissoncheck/', views.ChapterMissonCheckListView.as_view(), name='chaptermissoncheck_list'),
    path('chaptermissoncheck/create/', views.ChapterMissonCheckCreateView.as_view(), name='chaptermissoncheck_create'),
    path('chaptermissoncheck/detail/<int:pk>/', views.ChapterMissonCheckDetailView.as_view(),
         name='chaptermissoncheck_detail'),
    path('chaptermissoncheck/update/<int:pk>/', views.ChapterMissonCheckUpdateView.as_view(),
         name='chaptermissoncheck_update'),
)

urlpatterns += (
    # urls for ChapterWrite
    path('chapterwrite/', views.ChapterWriteListView.as_view(), name='chapterwrite_list'),
    path('chapterwrite/create/', views.ChapterWriteCreateView.as_view(), name='chapterwrite_create'),
    path('chapterwrite/detail/<int:pk>/', views.ChapterWriteDetailView.as_view(), name='chapterwrite_detail'),
    path('chapterwrite/update/<int:pk>/', views.ChapterWriteUpdateView.as_view(), name='chapterwrite_update'),
)

urlpatterns += (
    # urls for GroupMapping
    path('groupmapping/', views.GroupMappingListView.as_view(), name='groupmapping_list'),
    path('groupmapping/create/', views.GroupMappingCreateView.as_view(), name='groupmapping_create'),
    path('groupmapping/detail/<int:pk>/', views.GroupMappingDetailView.as_view(), name='groupmapping_detail'),
    path('groupmapping/update/<int:pk>/', views.GroupMappingUpdateView.as_view(), name='groupmapping_update'),
)

urlpatterns += (
    # urls for LearningNote
    path('learningnote/', views.LearningNoteListView.as_view(), name='learningnote_list'),
    path('learningnote/create/', views.LearningNoteCreateView.as_view(), name='learningnote_create'),
    path('learningnote/detail/<int:pk>/', views.LearningNoteDetailView.as_view(), name='learningnote_detail'),
    path('learningnote/update/<int:pk>/', views.LearningNoteUpdateView.as_view(), name='learningnote_update'),
)

urlpatterns += (
    # urls for LectureUbtInfo
    path('lectureubtinfo/', views.LectureUbtInfoListView.as_view(), name='lectureubtinfo_list'),
    path('lectureubtinfo/create/', views.LectureUbtInfoCreateView.as_view(), name='lectureubtinfo_create'),
    path('lectureubtinfo/detail/<int:pk>/', views.LectureUbtInfoDetailView.as_view(), name='lectureubtinfo_detail'),
    path('lectureubtinfo/update/<int:pk>/', views.LectureUbtInfoUpdateView.as_view(), name='lectureubtinfo_update'),
)

urlpatterns += (
    # urls for LessonInfo
    path('lessoninfo/', views.LessonInfoListView.as_view(), name='lessoninfo_list'),
    path('lessoninfo/create/', views.LessonInfoCreateView.as_view(), name='lessoninfo_create'),
    path('lessoninfo/detail/<int:pk>/', views.LessonInfoDetailView.as_view(), name='lessoninfo_detail'),
    path('lessoninfo/update/<int:pk>/', views.LessonInfoUpdateView.as_view(), name='lessoninfo_update'),
)

urlpatterns += (
    # urls for LessonLog
    path('lessonlog/', views.LessonLogListView.as_view(), name='lessonlog_list'),
    path('lessonlog/create/', views.LessonLogCreateView.as_view(), name='lessonlog_create'),
    path('lessonlog/detail/<int:pk>/', views.LessonLogDetailView.as_view(), name='lessonlog_detail'),
    path('lessonlog/update/<int:pk>/', views.LessonLogUpdateView.as_view(), name='lessonlog_update'),
)

urlpatterns += (
    # urls for MemberGroup
    path('membergroup/', views.MemberGroupListView.as_view(), name='membergroup_list'),
    path('membergroup/create/', views.MemberGroupCreateView.as_view(), name='membergroup_create'),
    path('membergroup/detail/<int:pk>/', views.MemberGroupDetailView.as_view(), name='membergroup_detail'),
    path('membergroup/update/<int:pk>/', views.MemberGroupUpdateView.as_view(), name='membergroup_update'),
)

urlpatterns += (
    # urls for MessageInfo
    path('messageinfo/', views.MessageInfoListView.as_view(), name='messageinfo_list'),
    path('messageinfo/create/', views.MessageInfoCreateView.as_view(), name='messageinfo_create'),
    path('messageinfo/detail/<int:pk>/', views.MessageInfoDetailView.as_view(), name='messageinfo_detail'),
    path('messageinfo/update/<int:pk>/', views.MessageInfoUpdateView.as_view(), name='messageinfo_update'),
)

# urlpatterns += (
#     # urls for OmrAnswerInfo
#     path('omranswerinfo/', views.OmrAnswerInfoListView.as_view(), name='omranswerinfo_list'),
#     path('omranswerinfo/create/', views.OmrAnswerInfoCreateView.as_view(), name='omranswerinfo_create'),
#     path('omranswerinfo/detail/<int:pk>/', views.OmrAnswerInfoDetailView.as_view(), name='omranswerinfo_detail'),
#     path('omranswerinfo/update/<int:pk>/', views.OmrAnswerInfoUpdateView.as_view(), name='omranswerinfo_update'),
# )
#
# urlpatterns += (
#     # urls for OmrAssignInfo
#     path('omrassigninfo/', views.OmrAssignInfoListView.as_view(), name='omrassigninfo_list'),
#     path('omrassigninfo/create/', views.OmrAssignInfoCreateView.as_view(), name='omrassigninfo_create'),
#     path('omrassigninfo/detail/<int:pk>/', views.OmrAssignInfoDetailView.as_view(), name='omrassigninfo_detail'),
#     path('omrassigninfo/update/<int:pk>/', views.OmrAssignInfoUpdateView.as_view(), name='omrassigninfo_update'),
# )
#
# urlpatterns += (
#     # urls for OmrExampleInfo
#     path('omrexampleinfo/', views.OmrExampleInfoListView.as_view(), name='omrexampleinfo_list'),
#     path('omrexampleinfo/create/', views.OmrExampleInfoCreateView.as_view(), name='omrexampleinfo_create'),
#     path('omrexampleinfo/detail/<int:pk>/', views.OmrExampleInfoDetailView.as_view(), name='omrexampleinfo_detail'),
#     path('omrexampleinfo/update/<int:pk>/', views.OmrExampleInfoUpdateView.as_view(), name='omrexampleinfo_update'),
# )


# urlpatterns += (
#     # urls for QAnswerLog
#     path('qanswerlog/', views.QAnswerLogListView.as_view(), name='qanswerlog_list'),
#     path('qanswerlog/create/', views.QAnswerLogCreateView.as_view(), name='qanswerlog_create'),
#     path('qanswerlog/detail/<int:pk>/', views.QAnswerLogDetailView.as_view(), name='qanswerlog_detail'),
#     path('qanswerlog/update/<int:pk>/', views.QAnswerLogUpdateView.as_view(), name='qanswerlog_update'),
# )

urlpatterns += (
    # urls for QExampleInfo
    path('qexampleinfo/', views.QExampleInfoListView.as_view(), name='qexampleinfo_list'),
    path('qexampleinfo/create/', views.QExampleInfoCreateView.as_view(), name='qexampleinfo_create'),
    path('qexampleinfo/detail/<int:pk>/', views.QExampleInfoDetailView.as_view(), name='qexampleinfo_detail'),
    path('qexampleinfo/update/<int:pk>/', views.QExampleInfoUpdateView.as_view(), name='qexampleinfo_update'),
)

urlpatterns += (
    # urls for QuizAnswerInfo
    path('quizanswerinfo/', views.QuizAnswerInfoListView.as_view(), name='quizanswerinfo_list'),
    path('quizanswerinfo/create/', views.QuizAnswerInfoCreateView.as_view(), name='quizanswerinfo_create'),
    path('quizanswerinfo/detail/<int:pk>/', views.QuizAnswerInfoDetailView.as_view(), name='quizanswerinfo_detail'),
    path('quizanswerinfo/update/<int:pk>/', views.QuizAnswerInfoUpdateView.as_view(), name='quizanswerinfo_update'),
)

urlpatterns += (
    # urls for QuizExampleInfo
    path('quizexampleinfo/', views.QuizExampleInfoListView.as_view(), name='quizexampleinfo_list'),
    path('quizexampleinfo/create/', views.QuizExampleInfoCreateView.as_view(), name='quizexampleinfo_create'),
    path('quizexampleinfo/detail/<int:pk>/', views.QuizExampleInfoDetailView.as_view(), name='quizexampleinfo_detail'),
    path('quizexampleinfo/update/<int:pk>/', views.QuizExampleInfoUpdateView.as_view(), name='quizexampleinfo_update'),
)

urlpatterns += (
    # urls for ScheduleInfo
    path('scheduleinfo/', views.ScheduleInfoListView.as_view(), name='scheduleinfo_list'),
    path('scheduleinfo/create/', views.ScheduleInfoCreateView.as_view(), name='scheduleinfo_create'),
    path('scheduleinfo/detail/<int:pk>/', views.ScheduleInfoDetailView.as_view(), name='scheduleinfo_detail'),
    path('scheduleinfo/update/<int:pk>/', views.ScheduleInfoUpdateView.as_view(), name='scheduleinfo_update'),
)

urlpatterns += (
    # urls for TalkMember
    path('talkmember/', views.TalkMemberListView.as_view(), name='talkmember_list'),
    path('talkmember/create/', views.TalkMemberCreateView.as_view(), name='talkmember_create'),
    path('talkmember/detail/<int:pk>/', views.TalkMemberDetailView.as_view(), name='talkmember_detail'),
    path('talkmember/update/<int:pk>/', views.TalkMemberUpdateView.as_view(), name='talkmember_update'),
)

urlpatterns += (
    # urls for TalkRoom
    path('talkroom/', views.TalkRoomListView.as_view(), name='talkroom_list'),
    path('talkroom/create/', views.TalkRoomCreateView.as_view(), name='talkroom_create'),
    path('talkroom/detail/<int:pk>/', views.TalkRoomDetailView.as_view(), name='talkroom_detail'),
    path('talkroom/update/<int:pk>/', views.TalkRoomUpdateView.as_view(), name='talkroom_update'),
)

urlpatterns += (
    # urls for TalkMessage
    path('talkmessage/', views.TalkMessageListView.as_view(), name='talkmessage_list'),
    path('talkmessage/create/', views.TalkMessageCreateView.as_view(), name='talkmessage_create'),
    path('talkmessage/detail/<int:pk>/', views.TalkMessageDetailView.as_view(), name='talkmessage_detail'),
    path('talkmessage/update/<int:pk>/', views.TalkMessageUpdateView.as_view(), name='talkmessage_update'),
)

urlpatterns += (
    # urls for TalkMessageRead
    path('talkmessageread/', views.TalkMessageReadListView.as_view(), name='talkmessageread_list'),
    path('talkmessageread/create/', views.TalkMessageReadCreateView.as_view(), name='talkmessageread_create'),
    path('talkmessageread/detail/<int:pk>/', views.TalkMessageReadDetailView.as_view(), name='talkmessageread_detail'),
    path('talkmessageread/update/<int:pk>/', views.TalkMessageReadUpdateView.as_view(), name='talkmessageread_update'),
)

urlpatterns += (
    # urls for TodoInfo
    path('todoinfo/', views.TodoInfoListView.as_view(), name='todoinfo_list'),
    path('todoinfo/create/', views.TodoInfoCreateView.as_view(), name='todoinfo_create'),
    path('todoinfo/detail/<int:pk>/', views.TodoInfoDetailView.as_view(), name='todoinfo_detail'),
    path('todoinfo/update/<int:pk>/', views.TodoInfoUpdateView.as_view(), name='todoinfo_update'),
)

urlpatterns += (
    # urls for TodoTInfo
    path('todotinfo/', views.TodoTInfoListView.as_view(), name='todotinfo_list'),
    path('todotinfo/create/', views.TodoTInfoCreateView.as_view(), name='todotinfo_create'),
    path('todotinfo/detail/<int:pk>/', views.TodoTInfoDetailView.as_view(), name='todotinfo_detail'),
    path('todotinfo/update/<int:pk>/', views.TodoTInfoUpdateView.as_view(), name='todotinfo_update'),
)
urlpatterns += (
    path('calendar/', views.calendar, name="admin_calendar"),
)

urlpatterns += (
    path('question/', views.question, name="questions"),  
)

urlpatterns += (
    path('question_teachers/', views.question_teachers, name="question_teachers"),   
)
urlpatterns += (
    path('questions_student/', views.questions_student, name="questions_student"),   
)
urlpatterns += (
    path('polls/', views.polls, name="polls"),
)
urlpatterns += (
    path('polls_teachers/', views.polls_teachers, name="polls_teachers"),
)
urlpatterns += (
    path('polls_student/', views.polls_student, name="polls_student"),
)
urlpatterns += (
    path('survey/', views.survey, name="survey"),
)
