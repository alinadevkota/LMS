from rest_framework import viewsets, permissions

from . import models
from . import serializers


# class ProfileViewSet(viewsets.ModelViewSet):
#     """ViewSet for the Profile class"""
#
#     queryset = models.Profile.objects.all()
#     serializer_class = serializers.ProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]


class CenterInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the CenterInfo class"""

    queryset = models.CenterInfo.objects.all()
    serializer_class = serializers.CenterInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class MemberInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the MemberInfo class"""

    queryset = models.MemberInfo.objects.all()
    serializer_class = serializers.MemberInfoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ('id', 'username')


class LectureInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the LectureInfo class"""

    queryset = models.LectureInfo.objects.all()
    serializer_class = serializers.LectureInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChapterInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the ChapterInfo class"""

    queryset = models.ChapterInfo.objects.all()
    serializer_class = serializers.ChapterInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChapterContentsInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the ChapterContentsInfo class"""

    queryset = models.ChapterContentsInfo.objects.all()
    serializer_class = serializers.ChapterContentsInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChapterMissonCheckCardViewSet(viewsets.ModelViewSet):
    """ViewSet for the ChapterMissonCheckCard class"""

    queryset = models.ChapterMissonCheckCard.objects.all()
    serializer_class = serializers.ChapterMissonCheckCardSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChapterMissonCheckItemViewSet(viewsets.ModelViewSet):
    """ViewSet for the ChapterMissonCheckItem class"""

    queryset = models.ChapterMissonCheckItem.objects.all()
    serializer_class = serializers.ChapterMissonCheckItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class InningInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the InningInfo class"""

    queryset = models.InningInfo.objects.all()
    serializer_class = serializers.InningInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class SessionInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the InningInfo class"""

    queryset = models.SessionInfo.objects.all()
    serializer_class = serializers.SessionInfoSerializer
    permission_classes = [permissions.IsAuthenticated]



# class OmrQuestionInfoViewSet(viewsets.ModelViewSet):
#     """ViewSet for the OmrQuestionInfo class"""
#
#     queryset = models.OmrQuestionInfo.objects.all()
#     serializer_class = serializers.OmrQuestionInfoSerializer
#     permission_classes = [permissions.IsAuthenticated]


class QuizInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the QuizInfo class"""

    queryset = models.QuizInfo.objects.all()
    serializer_class = serializers.QuizInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class AssignAssignmentInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the AssignHomeworkInfo class"""

    queryset = models.AssignAssignmentInfo.objects.all()
    serializer_class = serializers.AssignAssignmentInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class AssignQuestionInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the AssignQuestionInfo class"""

    queryset = models.AssignQuestionInfo.objects.all()
    serializer_class = serializers.AssignQuestionInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class BoardInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the BoardInfo class"""

    queryset = models.BoardInfo.objects.all()
    serializer_class = serializers.BoardInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class BoardContentInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the BoardContentInfo class"""

    queryset = models.BoardContentInfo.objects.all()
    serializer_class = serializers.BoardContentInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class InningGroupViewSet(viewsets.ModelViewSet):
    """ViewSet for the InningGroup class"""

    queryset = models.InningGroup.objects.all()
    serializer_class = serializers.InningGroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChapterContentMediaViewSet(viewsets.ModelViewSet):
    """ViewSet for the ChapterContentMedia class"""

    queryset = models.ChapterContentMedia.objects.all()
    serializer_class = serializers.ChapterContentMediaSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChapterImgInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the ChapterImgInfo class"""

    queryset = models.ChapterImgInfo.objects.all()
    serializer_class = serializers.ChapterImgInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChapterMissonCheckViewSet(viewsets.ModelViewSet):
    """ViewSet for the ChapterMissonCheck class"""

    queryset = models.ChapterMissonCheck.objects.all()
    serializer_class = serializers.ChapterMissonCheckSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChapterWriteViewSet(viewsets.ModelViewSet):
    """ViewSet for the ChapterWrite class"""

    queryset = models.ChapterWrite.objects.all()
    serializer_class = serializers.ChapterWriteSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupMappingViewSet(viewsets.ModelViewSet):
    """ViewSet for the GroupMapping class"""

    queryset = models.GroupMapping.objects.all()
    serializer_class = serializers.GroupMappingSerializer
    permission_classes = [permissions.IsAuthenticated]


class AssignmentInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the HomeworkInfo class"""

    queryset = models.AssignmentInfo.objects.all()
    serializer_class = serializers.AssignmentInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class LearningNoteViewSet(viewsets.ModelViewSet):
    """ViewSet for the LearningNote class"""

    queryset = models.LearningNote.objects.all()
    serializer_class = serializers.LearningNoteSerializer
    permission_classes = [permissions.IsAuthenticated]


class LectureUbtInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the LectureUbtInfo class"""

    queryset = models.LectureUbtInfo.objects.all()
    serializer_class = serializers.LectureUbtInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class LessonInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the LessonInfo class"""

    queryset = models.LessonInfo.objects.all()
    serializer_class = serializers.LessonInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class LessonLogViewSet(viewsets.ModelViewSet):
    """ViewSet for the LessonLog class"""

    queryset = models.LessonLog.objects.all()
    serializer_class = serializers.LessonLogSerializer
    permission_classes = [permissions.IsAuthenticated]


class MemberGroupViewSet(viewsets.ModelViewSet):
    """ViewSet for the MemberGroup class"""

    queryset = models.MemberGroup.objects.all()
    serializer_class = serializers.MemberGroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class MessageInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the MessageInfo class"""

    queryset = models.MessageInfo.objects.all()
    serializer_class = serializers.MessageInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


# class OmrAnswerInfoViewSet(viewsets.ModelViewSet):
#     """ViewSet for the OmrAnswerInfo class"""
#
#     queryset = models.OmrAnswerInfo.objects.all()
#     serializer_class = serializers.OmrAnswerInfoSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class OmrAssignInfoViewSet(viewsets.ModelViewSet):
#     """ViewSet for the OmrAssignInfo class"""
#
#     queryset = models.OmrAssignInfo.objects.all()
#     serializer_class = serializers.OmrAssignInfoSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class OmrExampleInfoViewSet(viewsets.ModelViewSet):
#     """ViewSet for the OmrExampleInfo class"""
#
#     queryset = models.OmrExampleInfo.objects.all()
#     serializer_class = serializers.OmrExampleInfoSerializer
#     permission_classes = [permissions.IsAuthenticated]


class AssignAnswerInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the AssignAnswerInfo class"""

    queryset = models.AssignAnswerInfo.objects.all()
    serializer_class = serializers.AssignAnswerInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


# class QAnswerLogViewSet(viewsets.ModelViewSet):
#     """ViewSet for the QAnswerLog class"""
#
#     queryset = models.QAnswerLog.objects.all()
#     serializer_class = serializers.QAnswerLogSerializer
#     permission_classes = [permissions.IsAuthenticated]


class QExampleInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the QExampleInfo class"""

    queryset = models.QExampleInfo.objects.all()
    serializer_class = serializers.QExampleInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the QuestionInfo class"""

    queryset = models.QuestionInfo.objects.all()
    serializer_class = serializers.QuestionInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuizAnswerInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the QuizAnswerInfo class"""

    queryset = models.QuizAnswerInfo.objects.all()
    serializer_class = serializers.QuizAnswerInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuizExampleInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the QuizExampleInfo class"""

    queryset = models.QuizExampleInfo.objects.all()
    serializer_class = serializers.QuizExampleInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ScheduleInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the ScheduleInfo class"""

    queryset = models.ScheduleInfo.objects.all()
    serializer_class = serializers.ScheduleInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class TalkMemberViewSet(viewsets.ModelViewSet):
    """ViewSet for the TalkMember class"""

    queryset = models.TalkMember.objects.all()
    serializer_class = serializers.TalkMemberSerializer
    permission_classes = [permissions.IsAuthenticated]


class TalkRoomViewSet(viewsets.ModelViewSet):
    """ViewSet for the TalkRoom class"""

    queryset = models.TalkRoom.objects.all()
    serializer_class = serializers.TalkRoomSerializer
    permission_classes = [permissions.IsAuthenticated]


class TalkMessageViewSet(viewsets.ModelViewSet):
    """ViewSet for the TalkMessage class"""

    queryset = models.TalkMessage.objects.all()
    serializer_class = serializers.TalkMessageSerializer
    permission_classes = [permissions.IsAuthenticated]


class TalkMessageReadViewSet(viewsets.ModelViewSet):
    """ViewSet for the TalkMessageRead class"""

    queryset = models.TalkMessageRead.objects.all()
    serializer_class = serializers.TalkMessageReadSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the TodoInfo class"""

    queryset = models.TodoInfo.objects.all()
    serializer_class = serializers.TodoInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoTInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the TodoTInfo class"""

    queryset = models.TodoTInfo.objects.all()
    serializer_class = serializers.TodoTInfoSerializer
    permission_classes = [permissions.IsAuthenticated]
