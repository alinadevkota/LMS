from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'assignhomeworkinfo', api.AssignHomeworkInfoViewSet)
router.register(r'assignquestioninfo', api.AssignQuestionInfoViewSet)
router.register(r'boardcontentinfo', api.BoardContentInfoViewSet)
router.register(r'boardinfo', api.BoardInfoViewSet)
router.register(r'centerinfo', api.CenterInfoViewSet)
router.register(r'chaptercontentmedia', api.ChapterContentMediaViewSet)
router.register(r'chaptercontentsinfo', api.ChapterContentsInfoViewSet)
router.register(r'chapterimginfo', api.ChapterImgInfoViewSet)
router.register(r'chapterinfo', api.ChapterInfoViewSet)
router.register(r'chaptermissoncheck', api.ChapterMissonCheckViewSet)
router.register(r'chaptermissoncheckcard', api.ChapterMissonCheckCardViewSet)
router.register(r'chaptermissoncheckitem', api.ChapterMissonCheckItemViewSet)
router.register(r'chapterwrite', api.ChapterWriteViewSet)
router.register(r'groupmapping', api.GroupMappingViewSet)
router.register(r'homeworkinfo', api.HomeworkInfoViewSet)
router.register(r'inninggroup', api.InningGroupViewSet)
router.register(r'inninginfo', api.InningInfoViewSet)
router.register(r'learningnote', api.LearningNoteViewSet)
router.register(r'lectureinfo', api.LectureInfoViewSet)
router.register(r'lectureubtinfo', api.LectureUbtInfoViewSet)
router.register(r'lessoninfo', api.LessonInfoViewSet)
router.register(r'lessonlog', api.LessonLogViewSet)
router.register(r'membergroup', api.MemberGroupViewSet)
router.register(r'memberinfo', api.MemberInfoViewSet)
router.register(r'messageinfo', api.MessageInfoViewSet)
router.register(r'omranswerinfo', api.OmrAnswerInfoViewSet)
router.register(r'omrassigninfo', api.OmrAssignInfoViewSet)
router.register(r'omrexampleinfo', api.OmrExampleInfoViewSet)
router.register(r'omrquestioninfo', api.OmrQuestionInfoViewSet)
router.register(r'qanswerinfo', api.QAnswerInfoViewSet)
router.register(r'qanswerlog', api.QAnswerLogViewSet)
router.register(r'qexampleinfo', api.QExampleInfoViewSet)
router.register(r'questioninfo', api.QuestionInfoViewSet)
router.register(r'quizanswerinfo', api.QuizAnswerInfoViewSet)
router.register(r'quizexampleinfo', api.QuizExampleInfoViewSet)
router.register(r'quizinfo', api.QuizInfoViewSet)
router.register(r'scheduleinfo', api.ScheduleInfoViewSet)
router.register(r'talkmember', api.TalkMemberViewSet)
router.register(r'talkmessage', api.TalkMessageViewSet)
router.register(r'talkmessageread', api.TalkMessageReadViewSet)
router.register(r'talkroom', api.TalkRoomViewSet)
router.register(r'todoinfo', api.TodoInfoViewSet)
router.register(r'todotinfo', api.TodoTInfoViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for AssignHomeworkInfo
    path('WebApp/assignhomeworkinfo/', views.AssignHomeworkInfoListView.as_view(),
         name='WebApp_assignhomeworkinfo_list'),
    path('WebApp/assignhomeworkinfo/create/', views.AssignHomeworkInfoCreateView.as_view(),
         name='WebApp_assignhomeworkinfo_create'),
    path('WebApp/assignhomeworkinfo/detail/<int:pk>/', views.AssignHomeworkInfoDetailView.as_view(),
         name='WebApp_assignhomeworkinfo_detail'),
    path('WebApp/assignhomeworkinfo/update/<int:pk>/', views.AssignHomeworkInfoUpdateView.as_view(),
         name='WebApp_assignhomeworkinfo_update'),
)

urlpatterns += (
    # urls for AssignQuestionInfo
    path('WebApp/assignquestioninfo/', views.AssignQuestionInfoListView.as_view(),
         name='WebApp_assignquestioninfo_list'),
    path('WebApp/assignquestioninfo/create/', views.AssignQuestionInfoCreateView.as_view(),
         name='WebApp_assignquestioninfo_create'),
    path('WebApp/assignquestioninfo/detail/<int:pk>/', views.AssignQuestionInfoDetailView.as_view(),
         name='WebApp_assignquestioninfo_detail'),
    path('WebApp/assignquestioninfo/update/<int:pk>/', views.AssignQuestionInfoUpdateView.as_view(),
         name='WebApp_assignquestioninfo_update'),
)

urlpatterns += (
    # urls for BoardContentInfo
    path('WebApp/boardcontentinfo/', views.BoardContentInfoListView.as_view(), name='WebApp_boardcontentinfo_list'),
    path('WebApp/boardcontentinfo/create/', views.BoardContentInfoCreateView.as_view(),
         name='WebApp_boardcontentinfo_create'),
    path('WebApp/boardcontentinfo/detail/<int:pk>/', views.BoardContentInfoDetailView.as_view(),
         name='WebApp_boardcontentinfo_detail'),
    path('WebApp/boardcontentinfo/update/<int:pk>/', views.BoardContentInfoUpdateView.as_view(),
         name='WebApp_boardcontentinfo_update'),
)

urlpatterns += (
    # urls for BoardInfo
    path('WebApp/boardinfo/', views.BoardInfoListView.as_view(), name='WebApp_boardinfo_list'),
    path('WebApp/boardinfo/create/', views.BoardInfoCreateView.as_view(), name='WebApp_boardinfo_create'),
    path('WebApp/boardinfo/detail/<int:pk>/', views.BoardInfoDetailView.as_view(), name='WebApp_boardinfo_detail'),
    path('WebApp/boardinfo/update/<int:pk>/', views.BoardInfoUpdateView.as_view(), name='WebApp_boardinfo_update'),
)

urlpatterns += (
    # urls for CenterInfo
    path('WebApp/centerinfo/', views.CenterInfoListView.as_view(), name='WebApp_centerinfo_list'),
    path('WebApp/centerinfo/create/', views.CenterInfoCreateView.as_view(), name='WebApp_centerinfo_create'),
    path('WebApp/centerinfo/detail/<int:pk>/', views.CenterInfoDetailView.as_view(), name='WebApp_centerinfo_detail'),
    path('WebApp/centerinfo/update/<int:pk>/', views.CenterInfoUpdateView.as_view(), name='WebApp_centerinfo_update'),
)

urlpatterns += (
    # urls for ChapterContentMedia
    path('WebApp/chaptercontentmedia/', views.ChapterContentMediaListView.as_view(),
         name='WebApp_chaptercontentmedia_list'),
    path('WebApp/chaptercontentmedia/create/', views.ChapterContentMediaCreateView.as_view(),
         name='WebApp_chaptercontentmedia_create'),
    path('WebApp/chaptercontentmedia/detail/<int:pk>/', views.ChapterContentMediaDetailView.as_view(),
         name='WebApp_chaptercontentmedia_detail'),
    path('WebApp/chaptercontentmedia/update/<int:pk>/', views.ChapterContentMediaUpdateView.as_view(),
         name='WebApp_chaptercontentmedia_update'),
)

urlpatterns += (
    # urls for ChapterContentsInfo
    path('WebApp/chaptercontentsinfo/', views.ChapterContentsInfoListView.as_view(),
         name='WebApp_chaptercontentsinfo_list'),
    path('WebApp/chaptercontentsinfo/create/', views.ChapterContentsInfoCreateView.as_view(),
         name='WebApp_chaptercontentsinfo_create'),
    path('WebApp/chaptercontentsinfo/detail/<int:pk>/', views.ChapterContentsInfoDetailView.as_view(),
         name='WebApp_chaptercontentsinfo_detail'),
    path('WebApp/chaptercontentsinfo/update/<int:pk>/', views.ChapterContentsInfoUpdateView.as_view(),
         name='WebApp_chaptercontentsinfo_update'),
)

urlpatterns += (
    # urls for ChapterImgInfo
    path('WebApp/chapterimginfo/', views.ChapterImgInfoListView.as_view(), name='WebApp_chapterimginfo_list'),
    path('WebApp/chapterimginfo/create/', views.ChapterImgInfoCreateView.as_view(),
         name='WebApp_chapterimginfo_create'),
    path('WebApp/chapterimginfo/detail/<int:pk>/', views.ChapterImgInfoDetailView.as_view(),
         name='WebApp_chapterimginfo_detail'),
    path('WebApp/chapterimginfo/update/<int:pk>/', views.ChapterImgInfoUpdateView.as_view(),
         name='WebApp_chapterimginfo_update'),
)

urlpatterns += (
    # urls for ChapterInfo
    path('WebApp/chapterinfo/', views.ChapterInfoListView.as_view(), name='WebApp_chapterinfo_list'),
    path('WebApp/chapterinfo/create/', views.ChapterInfoCreateView.as_view(), name='WebApp_chapterinfo_create'),
    path('WebApp/chapterinfo/detail/<int:pk>/', views.ChapterInfoDetailView.as_view(),
         name='WebApp_chapterinfo_detail'),
    path('WebApp/chapterinfo/update/<int:pk>/', views.ChapterInfoUpdateView.as_view(),
         name='WebApp_chapterinfo_update'),
)

urlpatterns += (
    # urls for ChapterMissonCheck
    path('WebApp/chaptermissoncheck/', views.ChapterMissonCheckListView.as_view(),
         name='WebApp_chaptermissoncheck_list'),
    path('WebApp/chaptermissoncheck/create/', views.ChapterMissonCheckCreateView.as_view(),
         name='WebApp_chaptermissoncheck_create'),
    path('WebApp/chaptermissoncheck/detail/<int:pk>/', views.ChapterMissonCheckDetailView.as_view(),
         name='WebApp_chaptermissoncheck_detail'),
    path('WebApp/chaptermissoncheck/update/<int:pk>/', views.ChapterMissonCheckUpdateView.as_view(),
         name='WebApp_chaptermissoncheck_update'),
)

urlpatterns += (
    # urls for ChapterMissonCheckCard
    path('WebApp/chaptermissoncheckcard/', views.ChapterMissonCheckCardListView.as_view(),
         name='WebApp_chaptermissoncheckcard_list'),
    path('WebApp/chaptermissoncheckcard/create/', views.ChapterMissonCheckCardCreateView.as_view(),
         name='WebApp_chaptermissoncheckcard_create'),
    path('WebApp/chaptermissoncheckcard/detail/<int:pk>/', views.ChapterMissonCheckCardDetailView.as_view(),
         name='WebApp_chaptermissoncheckcard_detail'),
    path('WebApp/chaptermissoncheckcard/update/<int:pk>/', views.ChapterMissonCheckCardUpdateView.as_view(),
         name='WebApp_chaptermissoncheckcard_update'),
)

urlpatterns += (
    # urls for ChapterMissonCheckItem
    path('WebApp/chaptermissoncheckitem/', views.ChapterMissonCheckItemListView.as_view(),
         name='WebApp_chaptermissoncheckitem_list'),
    path('WebApp/chaptermissoncheckitem/create/', views.ChapterMissonCheckItemCreateView.as_view(),
         name='WebApp_chaptermissoncheckitem_create'),
    path('WebApp/chaptermissoncheckitem/detail/<int:pk>/', views.ChapterMissonCheckItemDetailView.as_view(),
         name='WebApp_chaptermissoncheckitem_detail'),
    path('WebApp/chaptermissoncheckitem/update/<int:pk>/', views.ChapterMissonCheckItemUpdateView.as_view(),
         name='WebApp_chaptermissoncheckitem_update'),
)

urlpatterns += (
    # urls for ChapterWrite
    path('WebApp/chapterwrite/', views.ChapterWriteListView.as_view(), name='WebApp_chapterwrite_list'),
    path('WebApp/chapterwrite/create/', views.ChapterWriteCreateView.as_view(), name='WebApp_chapterwrite_create'),
    path('WebApp/chapterwrite/detail/<int:pk>/', views.ChapterWriteDetailView.as_view(),
         name='WebApp_chapterwrite_detail'),
    path('WebApp/chapterwrite/update/<int:pk>/', views.ChapterWriteUpdateView.as_view(),
         name='WebApp_chapterwrite_update'),
)

urlpatterns += (
    # urls for GroupMapping
    path('WebApp/groupmapping/', views.GroupMappingListView.as_view(), name='WebApp_groupmapping_list'),
    path('WebApp/groupmapping/create/', views.GroupMappingCreateView.as_view(), name='WebApp_groupmapping_create'),
    path('WebApp/groupmapping/detail/<int:pk>/', views.GroupMappingDetailView.as_view(),
         name='WebApp_groupmapping_detail'),
    path('WebApp/groupmapping/update/<int:pk>/', views.GroupMappingUpdateView.as_view(),
         name='WebApp_groupmapping_update'),
)

urlpatterns += (
    # urls for HomeworkInfo
    path('WebApp/homeworkinfo/', views.HomeworkInfoListView.as_view(), name='WebApp_homeworkinfo_list'),
    path('WebApp/homeworkinfo/create/', views.HomeworkInfoCreateView.as_view(), name='WebApp_homeworkinfo_create'),
    path('WebApp/homeworkinfo/detail/<int:pk>/', views.HomeworkInfoDetailView.as_view(),
         name='WebApp_homeworkinfo_detail'),
    path('WebApp/homeworkinfo/update/<int:pk>/', views.HomeworkInfoUpdateView.as_view(),
         name='WebApp_homeworkinfo_update'),
)

urlpatterns += (
    # urls for InningGroup
    path('WebApp/inninggroup/', views.InningGroupListView.as_view(), name='WebApp_inninggroup_list'),
    path('WebApp/inninggroup/create/', views.InningGroupCreateView.as_view(), name='WebApp_inninggroup_create'),
    path('WebApp/inninggroup/detail/<int:pk>/', views.InningGroupDetailView.as_view(),
         name='WebApp_inninggroup_detail'),
    path('WebApp/inninggroup/update/<int:pk>/', views.InningGroupUpdateView.as_view(),
         name='WebApp_inninggroup_update'),
)

urlpatterns += (
    # urls for InningInfo
    path('WebApp/inninginfo/', views.InningInfoListView.as_view(), name='WebApp_inninginfo_list'),
    path('WebApp/inninginfo/create/', views.InningInfoCreateView.as_view(), name='WebApp_inninginfo_create'),
    path('WebApp/inninginfo/detail/<int:pk>/', views.InningInfoDetailView.as_view(), name='WebApp_inninginfo_detail'),
    path('WebApp/inninginfo/update/<int:pk>/', views.InningInfoUpdateView.as_view(), name='WebApp_inninginfo_update'),
)

urlpatterns += (
    # urls for LearningNote
    path('WebApp/learningnote/', views.LearningNoteListView.as_view(), name='WebApp_learningnote_list'),
    path('WebApp/learningnote/create/', views.LearningNoteCreateView.as_view(), name='WebApp_learningnote_create'),
    path('WebApp/learningnote/detail/<int:pk>/', views.LearningNoteDetailView.as_view(),
         name='WebApp_learningnote_detail'),
    path('WebApp/learningnote/update/<int:pk>/', views.LearningNoteUpdateView.as_view(),
         name='WebApp_learningnote_update'),
)

urlpatterns += (
    # urls for LectureInfo
    path('WebApp/lectureinfo/', views.LectureInfoListView.as_view(), name='WebApp_lectureinfo_list'),
    path('WebApp/lectureinfo/create/', views.LectureInfoCreateView.as_view(), name='WebApp_lectureinfo_create'),
    path('WebApp/lectureinfo/detail/<int:pk>/', views.LectureInfoDetailView.as_view(),
         name='WebApp_lectureinfo_detail'),
    path('WebApp/lectureinfo/update/<int:pk>/', views.LectureInfoUpdateView.as_view(),
         name='WebApp_lectureinfo_update'),
)

urlpatterns += (
    # urls for LectureUbtInfo
    path('WebApp/lectureubtinfo/', views.LectureUbtInfoListView.as_view(), name='WebApp_lectureubtinfo_list'),
    path('WebApp/lectureubtinfo/create/', views.LectureUbtInfoCreateView.as_view(),
         name='WebApp_lectureubtinfo_create'),
    path('WebApp/lectureubtinfo/detail/<int:pk>/', views.LectureUbtInfoDetailView.as_view(),
         name='WebApp_lectureubtinfo_detail'),
    path('WebApp/lectureubtinfo/update/<int:pk>/', views.LectureUbtInfoUpdateView.as_view(),
         name='WebApp_lectureubtinfo_update'),
)

urlpatterns += (
    # urls for LessonInfo
    path('WebApp/lessoninfo/', views.LessonInfoListView.as_view(), name='WebApp_lessoninfo_list'),
    path('WebApp/lessoninfo/create/', views.LessonInfoCreateView.as_view(), name='WebApp_lessoninfo_create'),
    path('WebApp/lessoninfo/detail/<int:pk>/', views.LessonInfoDetailView.as_view(), name='WebApp_lessoninfo_detail'),
    path('WebApp/lessoninfo/update/<int:pk>/', views.LessonInfoUpdateView.as_view(), name='WebApp_lessoninfo_update'),
)

urlpatterns += (
    # urls for LessonLog
    path('WebApp/lessonlog/', views.LessonLogListView.as_view(), name='WebApp_lessonlog_list'),
    path('WebApp/lessonlog/create/', views.LessonLogCreateView.as_view(), name='WebApp_lessonlog_create'),
    path('WebApp/lessonlog/detail/<int:pk>/', views.LessonLogDetailView.as_view(), name='WebApp_lessonlog_detail'),
    path('WebApp/lessonlog/update/<int:pk>/', views.LessonLogUpdateView.as_view(), name='WebApp_lessonlog_update'),
)

urlpatterns += (
    # urls for MemberGroup
    path('WebApp/membergroup/', views.MemberGroupListView.as_view(), name='WebApp_membergroup_list'),
    path('WebApp/membergroup/create/', views.MemberGroupCreateView.as_view(), name='WebApp_membergroup_create'),
    path('WebApp/membergroup/detail/<int:pk>/', views.MemberGroupDetailView.as_view(),
         name='WebApp_membergroup_detail'),
    path('WebApp/membergroup/update/<int:pk>/', views.MemberGroupUpdateView.as_view(),
         name='WebApp_membergroup_update'),
)

urlpatterns += (
    # urls for MemberInfo
    path('WebApp/memberinfo/', views.MemberInfoListView.as_view(), name='WebApp_memberinfo_list'),
    path('WebApp/memberinfo/create/', views.MemberInfoCreateView.as_view(), name='WebApp_memberinfo_create'),
    path('WebApp/memberinfo/detail/<int:pk>/', views.MemberInfoDetailView.as_view(), name='WebApp_memberinfo_detail'),
    path('WebApp/memberinfo/update/<int:pk>/', views.MemberInfoUpdateView.as_view(), name='WebApp_memberinfo_update'),
)

urlpatterns += (
    # urls for MessageInfo
    path('WebApp/messageinfo/', views.MessageInfoListView.as_view(), name='WebApp_messageinfo_list'),
    path('WebApp/messageinfo/create/', views.MessageInfoCreateView.as_view(), name='WebApp_messageinfo_create'),
    path('WebApp/messageinfo/detail/<int:pk>/', views.MessageInfoDetailView.as_view(),
         name='WebApp_messageinfo_detail'),
    path('WebApp/messageinfo/update/<int:pk>/', views.MessageInfoUpdateView.as_view(),
         name='WebApp_messageinfo_update'),
)

urlpatterns += (
    # urls for OmrAnswerInfo
    path('WebApp/omranswerinfo/', views.OmrAnswerInfoListView.as_view(), name='WebApp_omranswerinfo_list'),
    path('WebApp/omranswerinfo/create/', views.OmrAnswerInfoCreateView.as_view(), name='WebApp_omranswerinfo_create'),
    path('WebApp/omranswerinfo/detail/<int:pk>/', views.OmrAnswerInfoDetailView.as_view(),
         name='WebApp_omranswerinfo_detail'),
    path('WebApp/omranswerinfo/update/<int:pk>/', views.OmrAnswerInfoUpdateView.as_view(),
         name='WebApp_omranswerinfo_update'),
)

urlpatterns += (
    # urls for OmrAssignInfo
    path('WebApp/omrassigninfo/', views.OmrAssignInfoListView.as_view(), name='WebApp_omrassigninfo_list'),
    path('WebApp/omrassigninfo/create/', views.OmrAssignInfoCreateView.as_view(), name='WebApp_omrassigninfo_create'),
    path('WebApp/omrassigninfo/detail/<int:pk>/', views.OmrAssignInfoDetailView.as_view(),
         name='WebApp_omrassigninfo_detail'),
    path('WebApp/omrassigninfo/update/<int:pk>/', views.OmrAssignInfoUpdateView.as_view(),
         name='WebApp_omrassigninfo_update'),
)

urlpatterns += (
    # urls for OmrExampleInfo
    path('WebApp/omrexampleinfo/', views.OmrExampleInfoListView.as_view(), name='WebApp_omrexampleinfo_list'),
    path('WebApp/omrexampleinfo/create/', views.OmrExampleInfoCreateView.as_view(),
         name='WebApp_omrexampleinfo_create'),
    path('WebApp/omrexampleinfo/detail/<int:pk>/', views.OmrExampleInfoDetailView.as_view(),
         name='WebApp_omrexampleinfo_detail'),
    path('WebApp/omrexampleinfo/update/<int:pk>/', views.OmrExampleInfoUpdateView.as_view(),
         name='WebApp_omrexampleinfo_update'),
)

urlpatterns += (
    # urls for OmrQuestionInfo
    path('WebApp/omrquestioninfo/', views.OmrQuestionInfoListView.as_view(), name='WebApp_omrquestioninfo_list'),
    path('WebApp/omrquestioninfo/create/', views.OmrQuestionInfoCreateView.as_view(),
         name='WebApp_omrquestioninfo_create'),
    path('WebApp/omrquestioninfo/detail/<int:pk>/', views.OmrQuestionInfoDetailView.as_view(),
         name='WebApp_omrquestioninfo_detail'),
    path('WebApp/omrquestioninfo/update/<int:pk>/', views.OmrQuestionInfoUpdateView.as_view(),
         name='WebApp_omrquestioninfo_update'),
)

urlpatterns += (
    # urls for QAnswerInfo
    path('WebApp/qanswerinfo/', views.QAnswerInfoListView.as_view(), name='WebApp_qanswerinfo_list'),
    path('WebApp/qanswerinfo/create/', views.QAnswerInfoCreateView.as_view(), name='WebApp_qanswerinfo_create'),
    path('WebApp/qanswerinfo/detail/<int:pk>/', views.QAnswerInfoDetailView.as_view(),
         name='WebApp_qanswerinfo_detail'),
    path('WebApp/qanswerinfo/update/<int:pk>/', views.QAnswerInfoUpdateView.as_view(),
         name='WebApp_qanswerinfo_update'),
)

urlpatterns += (
    # urls for QAnswerLog
    path('WebApp/qanswerlog/', views.QAnswerLogListView.as_view(), name='WebApp_qanswerlog_list'),
    path('WebApp/qanswerlog/create/', views.QAnswerLogCreateView.as_view(), name='WebApp_qanswerlog_create'),
    path('WebApp/qanswerlog/detail/<int:pk>/', views.QAnswerLogDetailView.as_view(), name='WebApp_qanswerlog_detail'),
    path('WebApp/qanswerlog/update/<int:pk>/', views.QAnswerLogUpdateView.as_view(), name='WebApp_qanswerlog_update'),
)

urlpatterns += (
    # urls for QExampleInfo
    path('WebApp/qexampleinfo/', views.QExampleInfoListView.as_view(), name='WebApp_qexampleinfo_list'),
    path('WebApp/qexampleinfo/create/', views.QExampleInfoCreateView.as_view(), name='WebApp_qexampleinfo_create'),
    path('WebApp/qexampleinfo/detail/<int:pk>/', views.QExampleInfoDetailView.as_view(),
         name='WebApp_qexampleinfo_detail'),
    path('WebApp/qexampleinfo/update/<int:pk>/', views.QExampleInfoUpdateView.as_view(),
         name='WebApp_qexampleinfo_update'),
)

urlpatterns += (
    # urls for QuestionInfo
    path('WebApp/questioninfo/', views.QuestionInfoListView.as_view(), name='WebApp_questioninfo_list'),
    path('WebApp/questioninfo/create/', views.QuestionInfoCreateView.as_view(), name='WebApp_questioninfo_create'),
    path('WebApp/questioninfo/detail/<int:pk>/', views.QuestionInfoDetailView.as_view(),
         name='WebApp_questioninfo_detail'),
    path('WebApp/questioninfo/update/<int:pk>/', views.QuestionInfoUpdateView.as_view(),
         name='WebApp_questioninfo_update'),
)

urlpatterns += (
    # urls for QuizAnswerInfo
    path('WebApp/quizanswerinfo/', views.QuizAnswerInfoListView.as_view(), name='WebApp_quizanswerinfo_list'),
    path('WebApp/quizanswerinfo/create/', views.QuizAnswerInfoCreateView.as_view(),
         name='WebApp_quizanswerinfo_create'),
    path('WebApp/quizanswerinfo/detail/<int:pk>/', views.QuizAnswerInfoDetailView.as_view(),
         name='WebApp_quizanswerinfo_detail'),
    path('WebApp/quizanswerinfo/update/<int:pk>/', views.QuizAnswerInfoUpdateView.as_view(),
         name='WebApp_quizanswerinfo_update'),
)

urlpatterns += (
    # urls for QuizExampleInfo
    path('WebApp/quizexampleinfo/', views.QuizExampleInfoListView.as_view(), name='WebApp_quizexampleinfo_list'),
    path('WebApp/quizexampleinfo/create/', views.QuizExampleInfoCreateView.as_view(),
         name='WebApp_quizexampleinfo_create'),
    path('WebApp/quizexampleinfo/detail/<int:pk>/', views.QuizExampleInfoDetailView.as_view(),
         name='WebApp_quizexampleinfo_detail'),
    path('WebApp/quizexampleinfo/update/<int:pk>/', views.QuizExampleInfoUpdateView.as_view(),
         name='WebApp_quizexampleinfo_update'),
)

urlpatterns += (
    # urls for QuizInfo
    path('WebApp/quizinfo/', views.QuizInfoListView.as_view(), name='WebApp_quizinfo_list'),
    path('WebApp/quizinfo/create/', views.QuizInfoCreateView.as_view(), name='WebApp_quizinfo_create'),
    path('WebApp/quizinfo/detail/<int:pk>/', views.QuizInfoDetailView.as_view(), name='WebApp_quizinfo_detail'),
    path('WebApp/quizinfo/update/<int:pk>/', views.QuizInfoUpdateView.as_view(), name='WebApp_quizinfo_update'),
)

urlpatterns += (
    # urls for ScheduleInfo
    path('WebApp/scheduleinfo/', views.ScheduleInfoListView.as_view(), name='WebApp_scheduleinfo_list'),
    path('WebApp/scheduleinfo/create/', views.ScheduleInfoCreateView.as_view(), name='WebApp_scheduleinfo_create'),
    path('WebApp/scheduleinfo/detail/<int:pk>/', views.ScheduleInfoDetailView.as_view(),
         name='WebApp_scheduleinfo_detail'),
    path('WebApp/scheduleinfo/update/<int:pk>/', views.ScheduleInfoUpdateView.as_view(),
         name='WebApp_scheduleinfo_update'),
)

urlpatterns += (
    # urls for TalkMember
    path('WebApp/talkmember/', views.TalkMemberListView.as_view(), name='WebApp_talkmember_list'),
    path('WebApp/talkmember/create/', views.TalkMemberCreateView.as_view(), name='WebApp_talkmember_create'),
    path('WebApp/talkmember/detail/<int:pk>/', views.TalkMemberDetailView.as_view(), name='WebApp_talkmember_detail'),
    path('WebApp/talkmember/update/<int:pk>/', views.TalkMemberUpdateView.as_view(), name='WebApp_talkmember_update'),
)

urlpatterns += (
    # urls for TalkMessage
    path('WebApp/talkmessage/', views.TalkMessageListView.as_view(), name='WebApp_talkmessage_list'),
    path('WebApp/talkmessage/create/', views.TalkMessageCreateView.as_view(), name='WebApp_talkmessage_create'),
    path('WebApp/talkmessage/detail/<int:pk>/', views.TalkMessageDetailView.as_view(),
         name='WebApp_talkmessage_detail'),
    path('WebApp/talkmessage/update/<int:pk>/', views.TalkMessageUpdateView.as_view(),
         name='WebApp_talkmessage_update'),
)

urlpatterns += (
    # urls for TalkMessageRead
    path('WebApp/talkmessageread/', views.TalkMessageReadListView.as_view(), name='WebApp_talkmessageread_list'),
    path('WebApp/talkmessageread/create/', views.TalkMessageReadCreateView.as_view(),
         name='WebApp_talkmessageread_create'),
    path('WebApp/talkmessageread/detail/<int:pk>/', views.TalkMessageReadDetailView.as_view(),
         name='WebApp_talkmessageread_detail'),
    path('WebApp/talkmessageread/update/<int:pk>/', views.TalkMessageReadUpdateView.as_view(),
         name='WebApp_talkmessageread_update'),
)

urlpatterns += (
    # urls for TalkRoom
    path('WebApp/talkroom/', views.TalkRoomListView.as_view(), name='WebApp_talkroom_list'),
    path('WebApp/talkroom/create/', views.TalkRoomCreateView.as_view(), name='WebApp_talkroom_create'),
    path('WebApp/talkroom/detail/<int:pk>/', views.TalkRoomDetailView.as_view(), name='WebApp_talkroom_detail'),
    path('WebApp/talkroom/update/<int:pk>/', views.TalkRoomUpdateView.as_view(), name='WebApp_talkroom_update'),
)

urlpatterns += (
    # urls for TodoInfo
    path('WebApp/todoinfo/', views.TodoInfoListView.as_view(), name='WebApp_todoinfo_list'),
    path('WebApp/todoinfo/create/', views.TodoInfoCreateView.as_view(), name='WebApp_todoinfo_create'),
    path('WebApp/todoinfo/detail/<int:pk>/', views.TodoInfoDetailView.as_view(), name='WebApp_todoinfo_detail'),
    path('WebApp/todoinfo/update/<int:pk>/', views.TodoInfoUpdateView.as_view(), name='WebApp_todoinfo_update'),
)

urlpatterns += (
    # urls for TodoTInfo
    path('WebApp/todotinfo/', views.TodoTInfoListView.as_view(), name='WebApp_todotinfo_list'),
    path('WebApp/todotinfo/create/', views.TodoTInfoCreateView.as_view(), name='WebApp_todotinfo_create'),
    path('WebApp/todotinfo/detail/<int:pk>/', views.TodoTInfoDetailView.as_view(), name='WebApp_todotinfo_detail'),
    path('WebApp/todotinfo/update/<int:pk>/', views.TodoTInfoUpdateView.as_view(), name='WebApp_todotinfo_update'),
)
