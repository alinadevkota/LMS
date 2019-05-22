from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import AssignHomeworkInfo, AssignQuestionInfo, BoardContentInfo, BoardInfo, CenterInfo, ChapterContentMedia, ChapterContentsInfo, ChapterImgInfo, ChapterInfo, ChapterMissonCheck, ChapterMissonCheckCard, ChapterMissonCheckItem, ChapterWrite, GroupMapping, HomeworkInfo, InningGroup, InningInfo, LearningNote, LectureInfo, LectureUbtInfo, LessonInfo, LessonLog, MemberGroup, MemberInfo, MessageInfo, OmrAnswerInfo, OmrAssignInfo, OmrExampleInfo, OmrQuestionInfo, QAnswerInfo, QAnswerLog, QExampleInfo, QuestionInfo, QuizAnswerInfo, QuizExampleInfo, QuizInfo, ScheduleInfo, TalkMember, TalkMessage, TalkMessageRead, TalkRoom, TodoInfo, TodoTInfo
from .forms import AssignHomeworkInfoForm, AssignQuestionInfoForm, BoardContentInfoForm, BoardInfoForm, CenterInfoForm, ChapterContentMediaForm, ChapterContentsInfoForm, ChapterImgInfoForm, ChapterInfoForm, ChapterMissonCheckForm, ChapterMissonCheckCardForm, ChapterMissonCheckItemForm, ChapterWriteForm, GroupMappingForm, HomeworkInfoForm, InningGroupForm, InningInfoForm, LearningNoteForm, LectureInfoForm, LectureUbtInfoForm, LessonInfoForm, LessonLogForm, MemberGroupForm, MemberInfoForm, MessageInfoForm, OmrAnswerInfoForm, OmrAssignInfoForm, OmrExampleInfoForm, OmrQuestionInfoForm, QAnswerInfoForm, QAnswerLogForm, QExampleInfoForm, QuestionInfoForm, QuizAnswerInfoForm, QuizExampleInfoForm, QuizInfoForm, ScheduleInfoForm, TalkMemberForm, TalkMessageForm, TalkMessageReadForm, TalkRoomForm, TodoInfoForm, TodoTInfoForm


class AssignHomeworkInfoListView(ListView):
    model = AssignHomeworkInfo


class AssignHomeworkInfoCreateView(CreateView):
    model = AssignHomeworkInfo
    form_class = AssignHomeworkInfoForm


class AssignHomeworkInfoDetailView(DetailView):
    model = AssignHomeworkInfo


class AssignHomeworkInfoUpdateView(UpdateView):
    model = AssignHomeworkInfo
    form_class = AssignHomeworkInfoForm


class AssignQuestionInfoListView(ListView):
    model = AssignQuestionInfo


class AssignQuestionInfoCreateView(CreateView):
    model = AssignQuestionInfo
    form_class = AssignQuestionInfoForm


class AssignQuestionInfoDetailView(DetailView):
    model = AssignQuestionInfo


class AssignQuestionInfoUpdateView(UpdateView):
    model = AssignQuestionInfo
    form_class = AssignQuestionInfoForm


class BoardContentInfoListView(ListView):
    model = BoardContentInfo


class BoardContentInfoCreateView(CreateView):
    model = BoardContentInfo
    form_class = BoardContentInfoForm


class BoardContentInfoDetailView(DetailView):
    model = BoardContentInfo


class BoardContentInfoUpdateView(UpdateView):
    model = BoardContentInfo
    form_class = BoardContentInfoForm


class BoardInfoListView(ListView):
    model = BoardInfo


class BoardInfoCreateView(CreateView):
    model = BoardInfo
    form_class = BoardInfoForm


class BoardInfoDetailView(DetailView):
    model = BoardInfo


class BoardInfoUpdateView(UpdateView):
    model = BoardInfo
    form_class = BoardInfoForm


class CenterInfoListView(ListView):
    model = CenterInfo


class CenterInfoCreateView(CreateView):
    model = CenterInfo
    form_class = CenterInfoForm


class CenterInfoDetailView(DetailView):
    model = CenterInfo


class CenterInfoUpdateView(UpdateView):
    model = CenterInfo
    form_class = CenterInfoForm


class ChapterContentMediaListView(ListView):
    model = ChapterContentMedia


class ChapterContentMediaCreateView(CreateView):
    model = ChapterContentMedia
    form_class = ChapterContentMediaForm


class ChapterContentMediaDetailView(DetailView):
    model = ChapterContentMedia


class ChapterContentMediaUpdateView(UpdateView):
    model = ChapterContentMedia
    form_class = ChapterContentMediaForm


class ChapterContentsInfoListView(ListView):
    model = ChapterContentsInfo


class ChapterContentsInfoCreateView(CreateView):
    model = ChapterContentsInfo
    form_class = ChapterContentsInfoForm


class ChapterContentsInfoDetailView(DetailView):
    model = ChapterContentsInfo


class ChapterContentsInfoUpdateView(UpdateView):
    model = ChapterContentsInfo
    form_class = ChapterContentsInfoForm


class ChapterImgInfoListView(ListView):
    model = ChapterImgInfo


class ChapterImgInfoCreateView(CreateView):
    model = ChapterImgInfo
    form_class = ChapterImgInfoForm


class ChapterImgInfoDetailView(DetailView):
    model = ChapterImgInfo


class ChapterImgInfoUpdateView(UpdateView):
    model = ChapterImgInfo
    form_class = ChapterImgInfoForm


class ChapterInfoListView(ListView):
    model = ChapterInfo


class ChapterInfoCreateView(CreateView):
    model = ChapterInfo
    form_class = ChapterInfoForm


class ChapterInfoDetailView(DetailView):
    model = ChapterInfo


class ChapterInfoUpdateView(UpdateView):
    model = ChapterInfo
    form_class = ChapterInfoForm


class ChapterMissonCheckListView(ListView):
    model = ChapterMissonCheck


class ChapterMissonCheckCreateView(CreateView):
    model = ChapterMissonCheck
    form_class = ChapterMissonCheckForm


class ChapterMissonCheckDetailView(DetailView):
    model = ChapterMissonCheck


class ChapterMissonCheckUpdateView(UpdateView):
    model = ChapterMissonCheck
    form_class = ChapterMissonCheckForm


class ChapterMissonCheckCardListView(ListView):
    model = ChapterMissonCheckCard


class ChapterMissonCheckCardCreateView(CreateView):
    model = ChapterMissonCheckCard
    form_class = ChapterMissonCheckCardForm


class ChapterMissonCheckCardDetailView(DetailView):
    model = ChapterMissonCheckCard


class ChapterMissonCheckCardUpdateView(UpdateView):
    model = ChapterMissonCheckCard
    form_class = ChapterMissonCheckCardForm


class ChapterMissonCheckItemListView(ListView):
    model = ChapterMissonCheckItem


class ChapterMissonCheckItemCreateView(CreateView):
    model = ChapterMissonCheckItem
    form_class = ChapterMissonCheckItemForm


class ChapterMissonCheckItemDetailView(DetailView):
    model = ChapterMissonCheckItem


class ChapterMissonCheckItemUpdateView(UpdateView):
    model = ChapterMissonCheckItem
    form_class = ChapterMissonCheckItemForm


class ChapterWriteListView(ListView):
    model = ChapterWrite


class ChapterWriteCreateView(CreateView):
    model = ChapterWrite
    form_class = ChapterWriteForm


class ChapterWriteDetailView(DetailView):
    model = ChapterWrite


class ChapterWriteUpdateView(UpdateView):
    model = ChapterWrite
    form_class = ChapterWriteForm


class GroupMappingListView(ListView):
    model = GroupMapping


class GroupMappingCreateView(CreateView):
    model = GroupMapping
    form_class = GroupMappingForm


class GroupMappingDetailView(DetailView):
    model = GroupMapping


class GroupMappingUpdateView(UpdateView):
    model = GroupMapping
    form_class = GroupMappingForm


class HomeworkInfoListView(ListView):
    model = HomeworkInfo


class HomeworkInfoCreateView(CreateView):
    model = HomeworkInfo
    form_class = HomeworkInfoForm


class HomeworkInfoDetailView(DetailView):
    model = HomeworkInfo


class HomeworkInfoUpdateView(UpdateView):
    model = HomeworkInfo
    form_class = HomeworkInfoForm


class InningGroupListView(ListView):
    model = InningGroup


class InningGroupCreateView(CreateView):
    model = InningGroup
    form_class = InningGroupForm


class InningGroupDetailView(DetailView):
    model = InningGroup


class InningGroupUpdateView(UpdateView):
    model = InningGroup
    form_class = InningGroupForm


class InningInfoListView(ListView):
    model = InningInfo


class InningInfoCreateView(CreateView):
    model = InningInfo
    form_class = InningInfoForm


class InningInfoDetailView(DetailView):
    model = InningInfo


class InningInfoUpdateView(UpdateView):
    model = InningInfo
    form_class = InningInfoForm


class LearningNoteListView(ListView):
    model = LearningNote


class LearningNoteCreateView(CreateView):
    model = LearningNote
    form_class = LearningNoteForm


class LearningNoteDetailView(DetailView):
    model = LearningNote


class LearningNoteUpdateView(UpdateView):
    model = LearningNote
    form_class = LearningNoteForm


class LectureInfoListView(ListView):
    model = LectureInfo


class LectureInfoCreateView(CreateView):
    model = LectureInfo
    form_class = LectureInfoForm


class LectureInfoDetailView(DetailView):
    model = LectureInfo


class LectureInfoUpdateView(UpdateView):
    model = LectureInfo
    form_class = LectureInfoForm


class LectureUbtInfoListView(ListView):
    model = LectureUbtInfo


class LectureUbtInfoCreateView(CreateView):
    model = LectureUbtInfo
    form_class = LectureUbtInfoForm


class LectureUbtInfoDetailView(DetailView):
    model = LectureUbtInfo


class LectureUbtInfoUpdateView(UpdateView):
    model = LectureUbtInfo
    form_class = LectureUbtInfoForm


class LessonInfoListView(ListView):
    model = LessonInfo


class LessonInfoCreateView(CreateView):
    model = LessonInfo
    form_class = LessonInfoForm


class LessonInfoDetailView(DetailView):
    model = LessonInfo


class LessonInfoUpdateView(UpdateView):
    model = LessonInfo
    form_class = LessonInfoForm


class LessonLogListView(ListView):
    model = LessonLog


class LessonLogCreateView(CreateView):
    model = LessonLog
    form_class = LessonLogForm


class LessonLogDetailView(DetailView):
    model = LessonLog


class LessonLogUpdateView(UpdateView):
    model = LessonLog
    form_class = LessonLogForm


class MemberGroupListView(ListView):
    model = MemberGroup


class MemberGroupCreateView(CreateView):
    model = MemberGroup
    form_class = MemberGroupForm


class MemberGroupDetailView(DetailView):
    model = MemberGroup


class MemberGroupUpdateView(UpdateView):
    model = MemberGroup
    form_class = MemberGroupForm


class MemberInfoListView(ListView):
    model = MemberInfo


class MemberInfoCreateView(CreateView):
    model = MemberInfo
    form_class = MemberInfoForm


class MemberInfoDetailView(DetailView):
    model = MemberInfo


class MemberInfoUpdateView(UpdateView):
    model = MemberInfo
    form_class = MemberInfoForm


class MessageInfoListView(ListView):
    model = MessageInfo


class MessageInfoCreateView(CreateView):
    model = MessageInfo
    form_class = MessageInfoForm


class MessageInfoDetailView(DetailView):
    model = MessageInfo


class MessageInfoUpdateView(UpdateView):
    model = MessageInfo
    form_class = MessageInfoForm


class OmrAnswerInfoListView(ListView):
    model = OmrAnswerInfo


class OmrAnswerInfoCreateView(CreateView):
    model = OmrAnswerInfo
    form_class = OmrAnswerInfoForm


class OmrAnswerInfoDetailView(DetailView):
    model = OmrAnswerInfo


class OmrAnswerInfoUpdateView(UpdateView):
    model = OmrAnswerInfo
    form_class = OmrAnswerInfoForm


class OmrAssignInfoListView(ListView):
    model = OmrAssignInfo


class OmrAssignInfoCreateView(CreateView):
    model = OmrAssignInfo
    form_class = OmrAssignInfoForm


class OmrAssignInfoDetailView(DetailView):
    model = OmrAssignInfo


class OmrAssignInfoUpdateView(UpdateView):
    model = OmrAssignInfo
    form_class = OmrAssignInfoForm


class OmrExampleInfoListView(ListView):
    model = OmrExampleInfo


class OmrExampleInfoCreateView(CreateView):
    model = OmrExampleInfo
    form_class = OmrExampleInfoForm


class OmrExampleInfoDetailView(DetailView):
    model = OmrExampleInfo


class OmrExampleInfoUpdateView(UpdateView):
    model = OmrExampleInfo
    form_class = OmrExampleInfoForm


class OmrQuestionInfoListView(ListView):
    model = OmrQuestionInfo


class OmrQuestionInfoCreateView(CreateView):
    model = OmrQuestionInfo
    form_class = OmrQuestionInfoForm


class OmrQuestionInfoDetailView(DetailView):
    model = OmrQuestionInfo


class OmrQuestionInfoUpdateView(UpdateView):
    model = OmrQuestionInfo
    form_class = OmrQuestionInfoForm


class QAnswerInfoListView(ListView):
    model = QAnswerInfo


class QAnswerInfoCreateView(CreateView):
    model = QAnswerInfo
    form_class = QAnswerInfoForm


class QAnswerInfoDetailView(DetailView):
    model = QAnswerInfo


class QAnswerInfoUpdateView(UpdateView):
    model = QAnswerInfo
    form_class = QAnswerInfoForm


class QAnswerLogListView(ListView):
    model = QAnswerLog


class QAnswerLogCreateView(CreateView):
    model = QAnswerLog
    form_class = QAnswerLogForm


class QAnswerLogDetailView(DetailView):
    model = QAnswerLog


class QAnswerLogUpdateView(UpdateView):
    model = QAnswerLog
    form_class = QAnswerLogForm


class QExampleInfoListView(ListView):
    model = QExampleInfo


class QExampleInfoCreateView(CreateView):
    model = QExampleInfo
    form_class = QExampleInfoForm


class QExampleInfoDetailView(DetailView):
    model = QExampleInfo


class QExampleInfoUpdateView(UpdateView):
    model = QExampleInfo
    form_class = QExampleInfoForm


class QuestionInfoListView(ListView):
    model = QuestionInfo


class QuestionInfoCreateView(CreateView):
    model = QuestionInfo
    form_class = QuestionInfoForm


class QuestionInfoDetailView(DetailView):
    model = QuestionInfo


class QuestionInfoUpdateView(UpdateView):
    model = QuestionInfo
    form_class = QuestionInfoForm


class QuizAnswerInfoListView(ListView):
    model = QuizAnswerInfo


class QuizAnswerInfoCreateView(CreateView):
    model = QuizAnswerInfo
    form_class = QuizAnswerInfoForm


class QuizAnswerInfoDetailView(DetailView):
    model = QuizAnswerInfo


class QuizAnswerInfoUpdateView(UpdateView):
    model = QuizAnswerInfo
    form_class = QuizAnswerInfoForm


class QuizExampleInfoListView(ListView):
    model = QuizExampleInfo


class QuizExampleInfoCreateView(CreateView):
    model = QuizExampleInfo
    form_class = QuizExampleInfoForm


class QuizExampleInfoDetailView(DetailView):
    model = QuizExampleInfo


class QuizExampleInfoUpdateView(UpdateView):
    model = QuizExampleInfo
    form_class = QuizExampleInfoForm


class QuizInfoListView(ListView):
    model = QuizInfo


class QuizInfoCreateView(CreateView):
    model = QuizInfo
    form_class = QuizInfoForm


class QuizInfoDetailView(DetailView):
    model = QuizInfo


class QuizInfoUpdateView(UpdateView):
    model = QuizInfo
    form_class = QuizInfoForm


class ScheduleInfoListView(ListView):
    model = ScheduleInfo


class ScheduleInfoCreateView(CreateView):
    model = ScheduleInfo
    form_class = ScheduleInfoForm


class ScheduleInfoDetailView(DetailView):
    model = ScheduleInfo


class ScheduleInfoUpdateView(UpdateView):
    model = ScheduleInfo
    form_class = ScheduleInfoForm


class TalkMemberListView(ListView):
    model = TalkMember


class TalkMemberCreateView(CreateView):
    model = TalkMember
    form_class = TalkMemberForm


class TalkMemberDetailView(DetailView):
    model = TalkMember


class TalkMemberUpdateView(UpdateView):
    model = TalkMember
    form_class = TalkMemberForm


class TalkMessageListView(ListView):
    model = TalkMessage


class TalkMessageCreateView(CreateView):
    model = TalkMessage
    form_class = TalkMessageForm


class TalkMessageDetailView(DetailView):
    model = TalkMessage


class TalkMessageUpdateView(UpdateView):
    model = TalkMessage
    form_class = TalkMessageForm


class TalkMessageReadListView(ListView):
    model = TalkMessageRead


class TalkMessageReadCreateView(CreateView):
    model = TalkMessageRead
    form_class = TalkMessageReadForm


class TalkMessageReadDetailView(DetailView):
    model = TalkMessageRead


class TalkMessageReadUpdateView(UpdateView):
    model = TalkMessageRead
    form_class = TalkMessageReadForm


class TalkRoomListView(ListView):
    model = TalkRoom


class TalkRoomCreateView(CreateView):
    model = TalkRoom
    form_class = TalkRoomForm


class TalkRoomDetailView(DetailView):
    model = TalkRoom


class TalkRoomUpdateView(UpdateView):
    model = TalkRoom
    form_class = TalkRoomForm


class TodoInfoListView(ListView):
    model = TodoInfo


class TodoInfoCreateView(CreateView):
    model = TodoInfo
    form_class = TodoInfoForm


class TodoInfoDetailView(DetailView):
    model = TodoInfo


class TodoInfoUpdateView(UpdateView):
    model = TodoInfo
    form_class = TodoInfoForm


class TodoTInfoListView(ListView):
    model = TodoTInfo


class TodoTInfoCreateView(CreateView):
    model = TodoTInfo
    form_class = TodoTInfoForm


class TodoTInfoDetailView(DetailView):
    model = TodoTInfo


class TodoTInfoUpdateView(UpdateView):
    model = TodoTInfo
    form_class = TodoTInfoForm

