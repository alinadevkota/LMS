from django import forms

from .models import AssignHomeworkInfo, AssignQuestionInfo, BoardContentInfo, BoardInfo, CenterInfo, \
    ChapterContentMedia, ChapterContentsInfo, ChapterImgInfo, ChapterInfo, ChapterMissonCheck, ChapterMissonCheckCard, \
    ChapterMissonCheckItem, ChapterWrite, GroupMapping, HomeworkInfo, InningGroup, InningInfo, LearningNote, \
    LectureInfo, LectureUbtInfo, LessonInfo, LessonLog, MemberGroup, MemberInfo, MessageInfo, OmrAnswerInfo, \
    OmrAssignInfo, OmrExampleInfo, OmrQuestionInfo, QAnswerInfo, QAnswerLog, QExampleInfo, QuestionInfo, QuizAnswerInfo, \
    QuizExampleInfo, QuizInfo, ScheduleInfo, TalkMember, TalkMessage, TalkMessageRead, TalkRoom, TodoInfo, TodoTInfo


class AssignHomeworkInfoForm(forms.ModelForm):
    class Meta:
        model = AssignHomeworkInfo
        fields = ['question_code', 'subject_code', 'lecture_code', 'chapter_code', 'member_code', 'use_flag',
                  'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']


class AssignQuestionInfoForm(forms.ModelForm):
    class Meta:
        model = AssignQuestionInfo
        fields = ['question_code', 'subject_code', 'lecture_code', 'chapter_code', 'question_type', 'use_flag',
                  'reg_date', 'reg_time', 'udt_date', 'udt_time', 'udt_agent']


class BoardContentInfoForm(forms.ModelForm):
    class Meta:
        model = BoardContentInfo
        fields = ['board_code', 'admin_id', 'title', 'contents', 'writer', 'view_cnt', 'ref_code', 'ref_step',
                  'ref_level', 'write_time', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time',
                  'udt_agent']


class BoardInfoForm(forms.ModelForm):
    class Meta:
        model = BoardInfo
        fields = ['board_name', 'board_write_level', 'board_read_level', 'board_reply_level', 'board_new_time',
                  'board_create_time', 'admin_id', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date',
                  'udt_time', 'udt_agent']


class CenterInfoForm(forms.ModelForm):
    class Meta:
        model = CenterInfo
        fields = ['center_name', 'center_location', 'center_tel', 'use_flag', 'reg_date', 'reg_time', 'reg_agent',
                  'udt_date', 'udt_time', 'udt_agent']


class ChapterContentMediaForm(forms.ModelForm):
    class Meta:
        model = ChapterContentMedia
        fields = ['chapter_contents_code', 'media_type', 'media_desc', 'media_filename', 'use_flag', 'reg_date',
                  'reg_time', 'udt_date', 'udt_time', 'reg_agent', 'udt_agent']


class ChapterContentsInfoForm(forms.ModelForm):
    class Meta:
        model = ChapterContentsInfo
        fields = ['chapter_code', 'chapter_contents', 'chapter_audio', 'use_flag', 'reg_date', 'reg_time', 'reg_agent',
                  'udt_date', 'udt_time', 'udt_agent', 'contents_index', 'chapter_type', 'thum_file', 'vod_file',
                  'today', 'front1_img', 'front1_text', 'back1_img', 'back1_text', 'pdf_file', 'front2_img',
                  'front3_img', 'front4_img', 'front2_text', 'front3_text', 'front4_text', 'back2_img', 'back3_img',
                  'back4_img', 'back2_text', 'back3_text', 'back4_text', 'c1_audio', 'c2_audio', 'c3_audio', 'c4_audio',
                  'vod_size', 'offline_file', 'teacher_guide', 'today_text', 'contents_text', 'pbl_allow',
                  'pbl_lec_allow']


class ChapterImgInfoForm(forms.ModelForm):
    class Meta:
        model = ChapterImgInfo
        fields = ['chapter_code', 'filename', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time',
                  'udt_agent']


class ChapterInfoForm(forms.ModelForm):
    class Meta:
        model = ChapterInfo
        fields = ['lecture_code', 'chapter_no', 'chapter_name', 'topic', 'summary', 'page_num', 'vod_size', 'intro',
                  'target', 'top_img', 'bottom_img1', 'bottom_img2', 'bottom_img3', 'thum_file', 'vod_file', 'use_flag',
                  'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'today', 'chapter_type',
                  'prologue_type', 'tabset', 'chapter_image', 'chapter_use', 'offline_file', 'pre_test_type',
                  'post_test_type', 'level1_avg', 'level2_avg', 'level3_avg', 'level1_hard_avg', 'level1_medium_avg',
                  'level1_easy_avg', 'level2_hard_avg', 'level2_medium_avg', 'level2_easy_avg', 'level3_hard_avg',
                  'level3_medium_avg', 'level3_easy_avg', 'homework_count', 'epilogue_type', 'epilogue_img', 'pbl_flag',
                  'chapter_use_time']


class ChapterMissonCheckForm(forms.ModelForm):
    class Meta:
        model = ChapterMissonCheck
        fields = ['check_code', 'check_item_code', 'student_code', 'check_agent_code', 'is_check_yn', 'use_flag',
                  'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'inning_code']


class ChapterMissonCheckCardForm(forms.ModelForm):
    class Meta:
        model = ChapterMissonCheckCard
        fields = ['check_card_code', 'chapter_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date',
                  'udt_time', 'udt_agent']


class ChapterMissonCheckItemForm(forms.ModelForm):
    class Meta:
        model = ChapterMissonCheckItem
        fields = ['check_item_code', 'check_card_code', 'item_text', 'contents_text', 'use_flag', 'reg_date',
                  'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'chapter_contents_code']


class ChapterWriteForm(forms.ModelForm):
    class Meta:
        model = ChapterWrite
        fields = ['inning_code', 'chapter_contents_code', 'student_code', 'write_content', 'use_flag', 'reg_date',
                  'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']


class GroupMappingForm(forms.ModelForm):
    class Meta:
        model = GroupMapping
        fields = ['center_code', 'group_code', 'member_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent',
                  'udt_date', 'udt_time', 'udt_agent']


class HomeworkInfoForm(forms.ModelForm):
    class Meta:
        model = HomeworkInfo
        fields = ['question_code', 'subject_code', 'lecture_code', 'chapter_code', 'level_score', 'use_flag',
                  'reg_date', 'reg_time', 'reg_agent', 'level']


class InningGroupForm(forms.ModelForm):
    class Meta:
        model = InningGroup
        fields = ['center_code', 'inning_code', 'lecture_code', 'teacher_code', 'use_flag', 'reg_date', 'reg_time',
                  'reg_agent', 'udt_date', 'udt_time', 'udt_agent']


class InningInfoForm(forms.ModelForm):
    class Meta:
        model = InningInfo
        fields = ['inning_name', 'lecture_code', 'start_date', 'end_date', 'use_flag', 'reg_date', 'reg_time',
                  'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'center_code']


class LearningNoteForm(forms.ModelForm):
    class Meta:
        model = LearningNote
        fields = ['inning_code', 'lecture_code', 'chapter_code', 'contents_code', 'note_contents', 'note_attachment']


class LectureInfoForm(forms.ModelForm):
    class Meta:
        model = LectureInfo
        fields = ['lecture_name', 'lecture_teacher', 'lecture_cover', 'lecture_cover_file', 'lecture_level',
                  'lecture_info', 'teacher', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time',
                  'udt_agent', 'lecture_certification', 'lecture_provider', 'cert_crit_prog', 'cert_crit_post',
                  'cert_crit_ubt', 'cert_crit_issue', 'center_code']


class LectureUbtInfoForm(forms.ModelForm):
    class Meta:
        model = LectureUbtInfo
        fields = ['quiz_code', 'lecture_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time',
                  'udt_agent']


class LessonInfoForm(forms.ModelForm):
    class Meta:
        model = LessonInfo
        fields = ['lecture_code', 'member_code', 'teacher_code', 'start_date', 'end_date', 'progress', 'use_flag',
                  'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'ubt_start', 'ubt_end',
                  'download_count', 'download_date', 'center_code', 'inning_code']


class LessonLogForm(forms.ModelForm):
    class Meta:
        model = LessonLog
        fields = ['lesson_code', 'lecture_code', 'chapter_code', 'member_code', 'member_id', 'member_ip',
                  'member_browser', 'member_os', 'start_date', 'start_time', 'end_date', 'end_time', 'connect_date',
                  'connect_time', 'connect_count', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date',
                  'udt_time', 'udt_agent', 'study_time', 'connect_page']


class MemberGroupForm(forms.ModelForm):
    class Meta:
        model = MemberGroup
        fields = ['center_code', 'group_name', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time',
                  'udt_agent']


class MemberInfoForm(forms.ModelForm):
    class Meta:
        model = MemberInfo
        fields = ['member_id', 'member_level', 'member_pw', 'member_name', 'member_jumin', 'member_birth',
                  'member_college', 'member_email', 'member_phone', 'member_post', 'member_addr1', 'member_addr2',
                  'member_file', 'member_gender', 'member_major', 'member_nation', 'use_flag', 'reg_date', 'reg_time',
                  'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'center_code', 'member_fax', 'member_memo']


class MessageInfoForm(forms.ModelForm):
    class Meta:
        model = MessageInfo
        fields = ['teacher_code', 'member_code', 'message', 'message_read', 'use_flag', 'reg_date', 'reg_time',
                  'reg_agent', 'udt_date', 'udt_time', 'udt_agent']


class OmrAnswerInfoForm(forms.ModelForm):
    class Meta:
        model = OmrAnswerInfo
        fields = ['subject_code', 'lecture_code', 'chapter_code', 'member_code', 'question_code', 'omr_answer',
                  'omr_answer_idx', 'omr_answer_correct', 'question_score', 'use_flag', 'reg_date', 'reg_time',
                  'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'lesson_code']


class OmrAssignInfoForm(forms.ModelForm):
    class Meta:
        model = OmrAssignInfo
        fields = ['question_code', 'subject_code', 'lecture_code', 'chapter_code', 'member_code', 'use_flag',
                  'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']


class OmrExampleInfoForm(forms.ModelForm):
    class Meta:
        model = OmrExampleInfo
        fields = ['question_code', 'omr_example_correct', 'omr_example_idx', 'use_flag', 'reg_date', 'reg_time',
                  'reg_agent', 'udt_date', 'udt_time', 'udt_agent']


class OmrQuestionInfoForm(forms.ModelForm):
    class Meta:
        model = OmrQuestionInfo
        fields = ['subject_code', 'lecture_code', 'chapter_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent',
                  'udt_date', 'udt_time', 'udt_agent', 'question_level', 'question_score']


class QAnswerInfoForm(forms.ModelForm):
    class Meta:
        model = QAnswerInfo
        fields = ['subject_code', 'lecture_code', 'chapter_code', 'member_code', 'question_code', 'question_type',
                  'question_answer', 'question_idx', 'question_correct', 'question_score', 'use_flag', 'reg_date',
                  'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'lesson_code']


class QAnswerLogForm(forms.ModelForm):
    class Meta:
        model = QAnswerLog
        fields = ['lecture_code', 'member_code', 'question_code', 'question_answer', 'question_idx', 'question_score',
                  'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']


class QExampleInfoForm(forms.ModelForm):
    class Meta:
        model = QExampleInfo
        fields = ['question_code', 'q_example', 'q_example_correct', 'q_example_idx', 'use_flag', 'reg_date',
                  'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'q_example_type']


class QuestionInfoForm(forms.ModelForm):
    class Meta:
        model = QuestionInfo
        fields = ['subject_code', 'lecture_code', 'chapter_code', 'question_type', 'question', 'question_media_type',
                  'question_media_file', 'question_score', 'question_head', 'question_essay', 'use_flag', 'reg_date',
                  'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'question_media_file2',
                  'question_comment', 'question_level', 'teacher_contents', 'student_contents']


class QuizAnswerInfoForm(forms.ModelForm):
    class Meta:
        model = QuizAnswerInfo
        fields = ['subject_code', 'lecture_code', 'chapter_code', 'member_code', 'quiz_code', 'quiz_type',
                  'quiz_answer', 'quiz_answer_idx', 'quiz_correct', 'quiz_score', 'use_flag', 'reg_date', 'reg_time',
                  'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'test_type']


class QuizExampleInfoForm(forms.ModelForm):
    class Meta:
        model = QuizExampleInfo
        fields = ['quiz_code', 'quiz_example', 'quiz_example_correct', 'quiz_example_idx', 'use_flag', 'reg_date',
                  'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'quiz_example_type']


class QuizInfoForm(forms.ModelForm):
    class Meta:
        model = QuizInfo
        fields = ['subject_code', 'lecture_code', 'chapter_code', 'quiz_type', 'quiz_question', 'quiz_media_type',
                  'quiz_media_file', 'quiz_score', 'quiz_comment', 'use_flag', 'reg_date', 'reg_time', 'reg_agent',
                  'udt_date', 'udt_time', 'udt_agent', 'quiz_head', 'quiz_media_file2']


class ScheduleInfoForm(forms.ModelForm):
    class Meta:
        model = ScheduleInfo
        fields = ['member_code', 'title', 'content', 'start_date', 'start_time', 'end_date', 'end_time', 'use_flag',
                  'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']


class TalkMemberForm(forms.ModelForm):
    class Meta:
        model = TalkMember
        fields = ['member_code', 'use_flag']


class TalkMessageForm(forms.ModelForm):
    class Meta:
        model = TalkMessage
        fields = ['talk_room_id', 'message', 'sender_member_code', 'send_date', 'send_time']


class TalkMessageReadForm(forms.ModelForm):
    class Meta:
        model = TalkMessageRead
        fields = ['member_code', 'is_read']


class TalkRoomForm(forms.ModelForm):
    class Meta:
        model = TalkRoom
        fields = ['talk_room_cate_code', 'lecture_code', 'inning_code', 'use_flag']


class TodoInfoForm(forms.ModelForm):
    class Meta:
        model = TodoInfo
        fields = ['chapter_code', 'member_code', 'todo_comment', 'todo_status', 'use_flag', 'reg_date', 'reg_time',
                  'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'teacher_code', 'todo_title', 'start_date',
                  'start_time', 'end_date', 'end_time', 'lecture_code']


class TodoTInfoForm(forms.ModelForm):
    class Meta:
        model = TodoTInfo
        fields = ['todo_code', 'member_code', 'todo_t_flag', 'use_flag', 'reg_date', 'reg_time', 'reg_agent',
                  'udt_date', 'udt_time', 'udt_agent']
