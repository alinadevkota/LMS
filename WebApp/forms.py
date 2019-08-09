from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput

from .models import CenterInfo, MemberInfo, LectureInfo, ChapterInfo, ChapterContentsInfo, ChapterMissonCheckCard, \
    ChapterMissonCheckItem, InningInfo,  QuizInfo, AssignmentInfo, QuestionInfo, AssignAssignmentInfo, \
    AssignQuestionInfo, AssignAnswerInfo, BoardInfo, \
    BoardContentInfo, InningGroup, ChapterContentMedia, ChapterImgInfo, ChapterMissonCheck, ChapterWrite, GroupMapping, \
    LearningNote, LectureUbtInfo, LessonInfo, LessonLog, MemberGroup, MessageInfo,  \
    QExampleInfo,  QuizAnswerInfo, QuizExampleInfo, \
    ScheduleInfo, TalkMember, TalkRoom, TalkMessage, TalkMessageRead, TodoInfo, TodoTInfo, USER_ROLES


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'


class UserRegisterForm(UserCreationForm):
    # Member_Role = forms.MultipleChoiceField(choices=USER_ROLES, widget=forms.CheckboxSelectMultiple())

    class Meta(UserCreationForm.Meta):
        model = MemberInfo
        fields = ('username', 'email', 'Member_Gender','Center_Code', 'Is_Student', 'Is_Teacher')


class UserUpdateForm(forms.ModelForm):
    role = forms.MultipleChoiceField(choices=USER_ROLES, )

    class Meta:
        model = MemberInfo
        fields = ('username', 'email')
        widgets = {
            'role': forms.CheckboxSelectMultiple,
        }


class UserUpdateFormForAdmin(forms.ModelForm):
    class Meta:
        model = MemberInfo
        fields = '__all__'


class CenterInfoForm(forms.ModelForm):
    class Meta:
        model = CenterInfo
        fields = ['Center_Name', 'Center_Address', 'Use_Flag', 'Register_Agent']


class MemberInfoForm(forms.ModelForm):
    class Meta:
        model = MemberInfo
        # fields = 'username', 'first_name', 'last_name', 'email', 'date_joined', 'Member_Permanent_Address', 'Member_Temporary_Address', 'Member_BirthDate', 'Member_Phone', 'Member_Avatar', 'Member_Gender', 'Member_Memo','Center_Code'
        fields = '__all__'
        exclude = ('last_login', 'date_joined', 'password', 'is_staff', 'is_active', 'is_superuser')


class LectureInfoForm(forms.ModelForm):
    class Meta:
        model = LectureInfo
        fields = '__all__'


class ChapterInfoForm(forms.ModelForm):
    class Meta:
        model = ChapterInfo
        fields = '__all__'


class ChapterContentsInfoForm(forms.ModelForm):
    class Meta:
        model = ChapterContentsInfo
        fields = '__all__'


class ChapterMissonCheckCardForm(forms.ModelForm):
    class Meta:
        model = ChapterMissonCheckCard
        fields = '__all__'


class ChapterMissonCheckItemForm(forms.ModelForm):
    class Meta:
        model = ChapterMissonCheckItem
        fields = '__all__'


class InningInfoForm(forms.ModelForm):
    class Meta:
        model = InningInfo
        fields = '__all__'


# class OmrQuestionInfoForm(forms.ModelForm):
#     class Meta:
#         model = OmrQuestionInfo
#         fields = '__all__'


class QuizInfoForm(forms.ModelForm):
    class Meta:
        model = QuizInfo
        fields = '__all__'

# AssignmentInfoForms
class AssignmentInfoForm(forms.ModelForm):
    class Meta:
        model = AssignmentInfo
        fields = '__all__'


class QuestionInfoForm(forms.ModelForm):
    class Meta:
        model = QuestionInfo
        fields = '__all__'


class AssignAssignmentInfoForm(forms.ModelForm):
    class Meta:
        model = AssignAssignmentInfo
        fields = '__all__'


class AssignQuestionInfoForm(forms.ModelForm):
    class Meta:
        model = AssignQuestionInfo
        fields = '__all__'

class AssignAnswerInfoForm(forms.ModelForm):
    class Meta:
        model = AssignAnswerInfo
        fields = '__all__'


class BoardInfoForm(forms.ModelForm):
    class Meta:
        model = BoardInfo
        fields = '__all__'


class BoardContentInfoForm(forms.ModelForm):
    class Meta:
        model = BoardContentInfo
        fields = '__all__'


class InningGroupForm(forms.ModelForm):
    class Meta:
        model = InningGroup
        fields = '__all__'


class ChapterContentMediaForm(forms.ModelForm):
    class Meta:
        model = ChapterContentMedia
        fields = '__all__'


class ChapterImgInfoForm(forms.ModelForm):
    class Meta:
        model = ChapterImgInfo
        fields = '__all__'


class ChapterMissonCheckForm(forms.ModelForm):
    class Meta:
        model = ChapterMissonCheck
        fields = '__all__'


class ChapterWriteForm(forms.ModelForm):
    class Meta:
        model = ChapterWrite
        fields = '__all__'


class GroupMappingForm(forms.ModelForm):
    class Meta:
        model = GroupMapping
        fields = '__all__'


class LearningNoteForm(forms.ModelForm):
    class Meta:
        model = LearningNote
        fields = '__all__'


class LectureUbtInfoForm(forms.ModelForm):
    class Meta:
        model = LectureUbtInfo
        fields = '__all__'


class LessonInfoForm(forms.ModelForm):
    class Meta:
        model = LessonInfo
        fields = '__all__'


class LessonLogForm(forms.ModelForm):
    class Meta:
        model = LessonLog
        fields = '__all__'


class MemberGroupForm(forms.ModelForm):
    class Meta:
        model = MemberGroup
        fields = '__all__'


class MessageInfoForm(forms.ModelForm):
    class Meta:
        model = MessageInfo
        fields = '__all__'


# class OmrAnswerInfoForm(forms.ModelForm):
#     class Meta:
#         model = OmrAnswerInfo
#         fields = '__all__'
#
#
# class OmrAssignInfoForm(forms.ModelForm):
#     class Meta:
#         model = OmrAssignInfo
#         fields = '__all__'
#
#
# class OmrExampleInfoForm(forms.ModelForm):
#     class Meta:
#         model = OmrExampleInfo
#         fields = '__all__'



class QExampleInfoForm(forms.ModelForm):
    class Meta:
        model = QExampleInfo
        fields = '__all__'


class QuizAnswerInfoForm(forms.ModelForm):
    class Meta:
        model = QuizAnswerInfo
        fields = '__all__'


class QuizExampleInfoForm(forms.ModelForm):
    class Meta:
        model = QuizExampleInfo
        fields = '__all__'


class ScheduleInfoForm(forms.ModelForm):
    class Meta:
        model = ScheduleInfo
        fields = '__all__'


class TalkMemberForm(forms.ModelForm):
    class Meta:
        model = TalkMember
        fields = '__all__'


class TalkRoomForm(forms.ModelForm):
    class Meta:
        model = TalkRoom
        fields = '__all__'


class TalkMessageForm(forms.ModelForm):
    class Meta:
        model = TalkMessage
        fields = '__all__'


class TalkMessageReadForm(forms.ModelForm):
    class Meta:
        model = TalkMessageRead
        fields = '__all__'


class TodoInfoForm(forms.ModelForm):
    class Meta:
        model = TodoInfo
        fields = '__all__'


class TodoTInfoForm(forms.ModelForm):
    class Meta:
        model = TodoTInfo
        fields = '__all__'


class ChangeOthersPasswordForm(forms.Form):
    attrs = {
        "type": "password"
    }
    password = forms.CharField(widget=forms.TextInput(attrs=attrs))
