from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import Select

from .models import CenterInfo, MemberInfo, LectureInfo, ChapterInfo, ChapterContentsInfo, ChapterMissonCheckCard, \
    ChapterMissonCheckItem, InningInfo, OmrQuestionInfo, QuizInfo, AssignHomeworkInfo, AssignQuestionInfo, BoardInfo, \
    BoardContentInfo, InningGroup, ChapterContentMedia, ChapterImgInfo, ChapterMissonCheck, ChapterWrite, GroupMapping, \
    HomeworkInfo, LearningNote, LectureUbtInfo, LessonInfo, LessonLog, MemberGroup, MessageInfo, OmrAnswerInfo, \
    OmrAssignInfo, OmrExampleInfo, QAnswerInfo, QAnswerLog, QExampleInfo, QuestionInfo, QuizAnswerInfo, QuizExampleInfo, \
    ScheduleInfo, TalkMember, TalkRoom, TalkMessage, TalkMessageRead, TodoInfo, TodoTInfo, USER_ROLES


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'


class UserRegisterForm(UserCreationForm):
    Member_Role = forms.MultipleChoiceField(choices=USER_ROLES, widget=forms.CheckboxSelectMultiple())

    class Meta(UserCreationForm.Meta):
        model = MemberInfo
        fields = ('username', 'email','Member_Role')


class UserUpdateForm(forms.ModelForm):
    role = forms.MultipleChoiceField(choices=USER_ROLES,)

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
        fields = ['Center_Name', 'Center_Address', 'Use_Flag', 'Register_DateTime', 'Register_Agent']


class MemberInfoForm(forms.ModelForm):
    class Meta:
        model = MemberInfo
        fields = '__all__'

class LectureInfoForm(forms.ModelForm):
    class Meta:
        model = LectureInfo
        fields = ['lecture_name', 'lecture_teacher', 'lecture_cover', 'lecture_cover_file', 'lecture_level', 'lecture_info', 'teacher', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'lecture_certification', 'lecture_provider', 'cert_crit_prog', 'cert_crit_post', 'cert_crit_ubt', 'cert_crit_issue', 'center_code']


class ChapterInfoForm(forms.ModelForm):
    class Meta:
        model = ChapterInfo
        fields = ['chapter_no', 'chapter_name', 'topic', 'summary', 'page_num', 'vod_size', 'intro', 'target', 'top_img', 'bottom_img1', 'bottom_img2', 'bottom_img3', 'thum_file', 'vod_file', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'today', 'chapter_type', 'prologue_type', 'tabset', 'chapter_image', 'chapter_use', 'offline_file', 'pre_test_type', 'post_test_type', 'level1_avg', 'level2_avg', 'level3_avg', 'level1_hard_avg', 'level1_medium_avg', 'level1_easy_avg', 'level2_hard_avg', 'level2_medium_avg', 'level2_easy_avg', 'level3_hard_avg', 'level3_medium_avg', 'level3_easy_avg', 'homework_count', 'epilogue_type', 'epilogue_img', 'pbl_flag', 'chapter_use_time', 'lecture_code']


class ChapterContentsInfoForm(forms.ModelForm):
    class Meta:
        model = ChapterContentsInfo
        fields = ['chapter_contents', 'chapter_audio', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'contents_index', 'chapter_type', 'thum_file', 'vod_file', 'today', 'front1_img', 'front1_text', 'back1_img', 'back1_text', 'pdf_file', 'front2_img', 'front3_img', 'front4_img', 'front2_text', 'front3_text', 'front4_text', 'back2_img', 'back3_img', 'back4_img', 'back2_text', 'back3_text', 'back4_text', 'c1_audio', 'c2_audio', 'c3_audio', 'c4_audio', 'vod_size', 'offline_file', 'teacher_guide', 'today_text', 'contents_text', 'pbl_allow', 'pbl_lec_allow', 'chapter_code']


class ChapterMissonCheckCardForm(forms.ModelForm):
    class Meta:
        model = ChapterMissonCheckCard
        fields = ['check_card_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'chapter_code']


class ChapterMissonCheckItemForm(forms.ModelForm):
    class Meta:
        model = ChapterMissonCheckItem
        fields = ['check_item_code', 'item_text', 'contents_text', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'check_card_code', 'chapter_contents_code']


class InningInfoForm(forms.ModelForm):
    class Meta:
        model = InningInfo
        fields = ['inning_name', 'start_date', 'end_date', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'lecture_code', 'center_code']


class OmrQuestionInfoForm(forms.ModelForm):
    class Meta:
        model = OmrQuestionInfo
        fields = ['subject_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'question_level', 'question_score', 'lecture_code', 'chapter_code']


class QuizInfoForm(forms.ModelForm):
    class Meta:
        model = QuizInfo
        fields = ['subject_code', 'quiz_type', 'quiz_question', 'quiz_media_type', 'quiz_media_file', 'quiz_score', 'quiz_comment', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'quiz_head', 'quiz_media_file2', 'lecture_code', 'chapter_code']


class AssignHomeworkInfoForm(forms.ModelForm):
    class Meta:
        model = AssignHomeworkInfo
        fields = ['subject_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'question_code', 'lecture_code', 'chapter_code', 'member_code']


class AssignQuestionInfoForm(forms.ModelForm):
    class Meta:
        model = AssignQuestionInfo
        fields = ['subject_code', 'question_type', 'use_flag', 'reg_date', 'reg_time', 'udt_date', 'udt_time', 'udt_agent', 'question_code', 'lecture_code', 'chapter_code']


class BoardInfoForm(forms.ModelForm):
    class Meta:
        model = BoardInfo
        fields = ['board_name', 'board_write_level', 'board_read_level', 'board_reply_level', 'board_new_time', 'board_create_time', 'admin_id', 'use_flag', 'reg_date', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']


class BoardContentInfoForm(forms.ModelForm):
    class Meta:
        model = BoardContentInfo
        fields = ['admin_id', 'title', 'contents', 'writer', 'view_cnt', 'ref_code', 'ref_step', 'ref_level', 'write_time', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'board_code']


class InningGroupForm(forms.ModelForm):
    class Meta:
        model = InningGroup
        fields = ['teacher_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'center_code', 'inning_code', 'lecture_code']


class ChapterContentMediaForm(forms.ModelForm):
    class Meta:
        model = ChapterContentMedia
        fields = ['media_type', 'media_desc', 'media_filename', 'use_flag', 'reg_date', 'reg_time', 'udt_date', 'udt_time', 'reg_agent', 'udt_agent', 'chapter_contents_code']


class ChapterImgInfoForm(forms.ModelForm):
    class Meta:
        model = ChapterImgInfo
        fields = ['filename', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'chapter_code']


class ChapterMissonCheckForm(forms.ModelForm):
    class Meta:
        model = ChapterMissonCheck
        fields = ['check_code', 'student_code', 'check_agent_code', 'is_check_yn', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'check_item_code', 'inning_code']


class ChapterWriteForm(forms.ModelForm):
    class Meta:
        model = ChapterWrite
        fields = ['student_code', 'write_content', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'inning_code', 'chapter_contents_code']


class GroupMappingForm(forms.ModelForm):
    class Meta:
        model = GroupMapping
        fields = ['use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'center_code', 'group_code', 'member_code']


class HomeworkInfoForm(forms.ModelForm):
    class Meta:
        model = HomeworkInfo
        fields = ['subject_code', 'level_score', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'level', 'question_code', 'lecture_code', 'chapter_code']


class LearningNoteForm(forms.ModelForm):
    class Meta:
        model = LearningNote
        fields = ['contents_code', 'note_contents', 'note_attachment', 'inning_code', 'lecture_code', 'chapter_code']


class LectureUbtInfoForm(forms.ModelForm):
    class Meta:
        model = LectureUbtInfo
        fields = ['use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'quiz_code', 'lecture_code']


class LessonInfoForm(forms.ModelForm):
    class Meta:
        model = LessonInfo
        fields = ['teacher_code', 'start_date', 'end_date', 'progress', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'ubt_start', 'ubt_end', 'download_count', 'download_date', 'lecture_code', 'member_code', 'center_code', 'inning_code']


class LessonLogForm(forms.ModelForm):
    class Meta:
        model = LessonLog
        fields = ['member_id', 'member_ip', 'member_browser', 'member_os', 'start_date', 'start_time', 'end_date', 'end_time', 'connect_date', 'connect_time', 'connect_count', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'study_time', 'connect_page', 'lesson_code', 'lecture_code', 'chapter_code', 'member_code']


class MemberGroupForm(forms.ModelForm):
    class Meta:
        model = MemberGroup
        fields = ['group_name', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'center_code']


class MessageInfoForm(forms.ModelForm):
    class Meta:
        model = MessageInfo
        fields = ['teacher_code', 'message', 'message_read', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'member_code']


class OmrAnswerInfoForm(forms.ModelForm):
    class Meta:
        model = OmrAnswerInfo
        fields = ['subject_code', 'omr_answer', 'omr_answer_idx', 'omr_answer_correct', 'question_score', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'lecture_code', 'chapter_code', 'member_code', 'question_code', 'lesson_code']


class OmrAssignInfoForm(forms.ModelForm):
    class Meta:
        model = OmrAssignInfo
        fields = ['subject_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'question_code', 'lecture_code', 'chapter_code', 'member_code']


class OmrExampleInfoForm(forms.ModelForm):
    class Meta:
        model = OmrExampleInfo
        fields = ['omr_example_correct', 'omr_example_idx', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'question_code']


class QAnswerInfoForm(forms.ModelForm):
    class Meta:
        model = QAnswerInfo
        fields = ['subject_code', 'question_type', 'question_answer', 'question_idx', 'question_correct', 'question_score', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'lecture_code', 'chapter_code', 'member_code', 'question_code', 'lesson_code']


class QAnswerLogForm(forms.ModelForm):
    class Meta:
        model = QAnswerLog
        fields = ['question_answer', 'question_idx', 'question_score', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'lecture_code', 'member_code', 'question_code']


class QExampleInfoForm(forms.ModelForm):
    class Meta:
        model = QExampleInfo
        fields = ['q_example', 'q_example_correct', 'q_example_idx', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'q_example_type', 'question_code']


class QuestionInfoForm(forms.ModelForm):
    class Meta:
        model = QuestionInfo
        fields = ['subject_code', 'question_type', 'question', 'question_media_type', 'question_media_file', 'question_score', 'question_head', 'question_essay', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'question_media_file2', 'question_comment', 'question_level', 'teacher_contents', 'student_contents', 'lecture_code', 'chapter_code']


class QuizAnswerInfoForm(forms.ModelForm):
    class Meta:
        model = QuizAnswerInfo
        fields = ['subject_code', 'quiz_type', 'quiz_answer', 'quiz_answer_idx', 'quiz_correct', 'quiz_score', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'test_type', 'lecture_code', 'chapter_code', 'member_code', 'quiz_code']


class QuizExampleInfoForm(forms.ModelForm):
    class Meta:
        model = QuizExampleInfo
        fields = ['quiz_example', 'quiz_example_correct', 'quiz_example_idx', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'quiz_example_type', 'quiz_code']


class ScheduleInfoForm(forms.ModelForm):
    class Meta:
        model = ScheduleInfo
        fields = ['title', 'content', 'start_date', 'start_time', 'end_date', 'end_time', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'member_code']


class TalkMemberForm(forms.ModelForm):
    class Meta:
        model = TalkMember
        fields = ['use_flag', 'member_code']


class TalkRoomForm(forms.ModelForm):
    class Meta:
        model = TalkRoom
        fields = ['talk_room_cate_code', 'use_flag', 'lecture_code', 'inning_code']


class TalkMessageForm(forms.ModelForm):
    class Meta:
        model = TalkMessage
        fields = ['message', 'sender_member_code', 'send_date', 'send_time', 'talk_room_id']


class TalkMessageReadForm(forms.ModelForm):
    class Meta:
        model = TalkMessageRead
        fields = ['is_read', 'member_code']


class TodoInfoForm(forms.ModelForm):
    class Meta:
        model = TodoInfo
        fields = ['todo_comment', 'todo_status', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'teacher_code', 'todo_title', 'start_date', 'start_time', 'end_date', 'end_time', 'chapter_code', 'member_code', 'lecture_code']


class TodoTInfoForm(forms.ModelForm):
    class Meta:
        model = TodoTInfo
        fields = ['todo_code', 'todo_t_flag', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'member_code']


