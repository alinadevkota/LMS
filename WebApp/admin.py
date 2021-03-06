from django.contrib import admin
from django import forms
from .models import CenterInfo, MemberInfo, CourseInfo, ChapterInfo, ChapterContentsInfo, ChapterMissonCheckCard, \
    ChapterMissonCheckItem, SessionInfo, InningInfo, QuizInfo, AssignmentInfo, QuestionInfo, AssignAssignmentInfo, \
    AssignAnswerInfo, BoardInfo, \
    BoardContentInfo, InningGroup, ChapterContentMedia, ChapterImgInfo, ChapterMissonCheck, ChapterWrite, GroupMapping, \
    LearningNote, CourseUbtInfo, LessonInfo, LessonLog, MemberGroup, MessageInfo, \
    QExampleInfo, QuizAnswerInfo, \
    QuizExampleInfo, \
    ScheduleInfo, TalkMember, TalkRoom, TalkMessage, TalkMessageRead, TodoInfo, TodoTInfo


# class ProfileAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = Profile
#         fields = '__all__'
#
#
# class ProfileAdmin(admin.ModelAdmin):
#     form = ProfileAdminForm
#
#
# admin.site.register(Profile, ProfileAdmin)
#

class CenterInfoAdminForm(forms.ModelForm):
    class Meta:
        model = CenterInfo
        fields = '__all__'


class CenterInfoAdmin(admin.ModelAdmin):
    form = CenterInfoAdminForm
    list_display = ['Center_Name', 'Center_Address', 'Use_Flag', 'Register_DateTime', 'Register_Agent']
    # readonly_fields = ['Center_Name', 'Center_Address', 'Use_Flag', 'Register_DateTime', 'Register_Agent']


admin.site.register(CenterInfo, CenterInfoAdmin)


class MemberInfoAdminForm(forms.ModelForm):
    class Meta:
        model = MemberInfo
        fields = '__all__'


class MemberInfoAdmin(admin.ModelAdmin):
    form = MemberInfoAdminForm
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'Member_Permanent_Address',
                    'Member_Temporary_Address', 'Member_BirthDate', 'Member_Phone', 'Member_Avatar',
                    'Member_Gender', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent',
                    'Member_Memo']
    list_display_links = ['id', 'username']
    # list_display =  [field.name for field in MemberInfo._meta.get_fields()]
    # readonly_fields = ['Member_ID', 'Member_Name', 'Member_Permanent_Address', 'Member_Temporary_Address', 'Member_BirthDate', 'Member_Email', 'Member_Phone', 'forum_avatar', 'member_Gender', 'Use_Flag', 'Register_DateTime', 'Register_Agent', 'Member_Memo']


admin.site.register(MemberInfo, MemberInfoAdmin)


class CourseInfoAdminForm(forms.ModelForm):
    class Meta:
        model = CourseInfo
        fields = '__all__'


class CourseInfoAdmin(admin.ModelAdmin):
    form = CourseInfoAdminForm
    list_display = ['Course_Name', 'Course_Cover_File', 'Course_Level',
                    'Course_Info', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent',
                    'Course_Provider', 'Center_Code']
    # readonly_fields = ['course_name', 'course_teacher', 'course_cover', 'course_cover_file', 'course_level', 'course_info', 'teacher', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent', 'course_certification', 'course_provider', 'cert_crit_prog', 'cert_crit_post', 'cert_crit_ubt', 'cert_crit_issue']


admin.site.register(CourseInfo, CourseInfoAdmin)


class ChapterInfoAdminForm(forms.ModelForm):
    class Meta:
        model = ChapterInfo
        fields = '__all__'


class ChapterInfoAdmin(admin.ModelAdmin):
    form = ChapterInfoAdminForm
    list_display = ['Chapter_No', 'Chapter_Name', 'Summary', 'Page_Num', 'Use_Flag',
                    'Register_DateTime', 'Updated_DateTime', 'Register_Agent', 'Course_Code']
    # readonly_fields = ['chapter_no', 'chapter_name', 'topic', 'summary', 'page_num', 'vod_size', 'intro', 'target', 'top_img', 'bottom_img1', 'bottom_img2', 'bottom_img3', 'thum_file', 'vod_file', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent', 'today', 'chapter_type', 'prologue_type', 'tabset', 'chapter_image', 'chapter_use', 'offline_file', 'pre_test_type', 'post_test_type', 'level1_avg', 'level2_avg', 'level3_avg', 'level1_hard_avg', 'level1_medium_avg', 'level1_easy_avg', 'level2_hard_avg', 'level2_medium_avg', 'level2_easy_avg', 'level3_hard_avg', 'level3_medium_avg', 'level3_easy_avg', 'homework_count', 'epilogue_type', 'epilogue_img', 'pbl_flag', 'chapter_use_time']


admin.site.register(ChapterInfo, ChapterInfoAdmin)


class ChapterContentsInfoAdminForm(forms.ModelForm):
    class Meta:
        model = ChapterContentsInfo
        fields = '__all__'


class ChapterContentsInfoAdmin(admin.ModelAdmin):
    form = ChapterContentsInfoAdminForm
    list_display = ['Chapter_Code', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
                    'Register_Agent', 'Content_Description']
    # readonly_fields = ['chapter_contents', 'chapter_audio', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent', 'contents_index', 'chapter_type', 'thum_file', 'vod_file', 'today', 'front1_img', 'front1_text', 'back1_img', 'back1_text', 'pdf_file', 'front2_img', 'front3_img', 'front4_img', 'front2_text', 'front3_text', 'front4_text', 'back2_img', 'back3_img', 'back4_img', 'back2_text', 'back3_text', 'back4_text', 'c1_audio', 'c2_audio', 'c3_audio', 'c4_audio', 'vod_size', 'offline_file', 'teacher_guide', 'today_text', 'contents_text', 'pbl_allow', 'pbl_lec_allow']


admin.site.register(ChapterContentsInfo, ChapterContentsInfoAdmin)


class ChapterMissonCheckCardAdminForm(forms.ModelForm):
    class Meta:
        model = ChapterMissonCheckCard
        fields = '__all__'


class ChapterMissonCheckCardAdmin(admin.ModelAdmin):
    form = ChapterMissonCheckCardAdminForm
    list_display = ['check_card_code', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']
    # readonly_fields = ['check_card_code', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']


admin.site.register(ChapterMissonCheckCard, ChapterMissonCheckCardAdmin)


class ChapterMissonCheckItemAdminForm(forms.ModelForm):
    class Meta:
        model = ChapterMissonCheckItem
        fields = '__all__'


class ChapterMissonCheckItemAdmin(admin.ModelAdmin):
    form = ChapterMissonCheckItemAdminForm
    list_display = ['check_item_code', 'item_text', 'contents_text', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime', 'Register_Agent']
    # readonly_fields = ['check_item_code', 'item_text', 'contents_text', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']


admin.site.register(ChapterMissonCheckItem, ChapterMissonCheckItemAdmin)


#
# class OmrQuestionInfoAdminForm(forms.ModelForm):
#     class Meta:
#         model = OmrQuestionInfo
#         fields = '__all__'


# class OmrQuestionInfoAdmin(admin.ModelAdmin):
#     form = OmrQuestionInfoAdminForm
#     list_display = ['Homework_Code', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
#                     'Register_Agent',
#                     'Question_Level', 'Question_Score', 'Question_Description']
#     # readonly_fields = ['subject_code', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent', 'question_level', 'question_score']
#
#
# admin.site.register(OmrQuestionInfo, OmrQuestionInfoAdmin)


class QuizInfoAdminForm(forms.ModelForm):
    class Meta:
        model = QuizInfo
        fields = '__all__'


class QuizInfoAdmin(admin.ModelAdmin):
    form = QuizInfoAdminForm
    list_display = ['subject_code', 'quiz_type', 'quiz_question', 'quiz_media_type', 'quiz_media_file', 'quiz_score',
                    'quiz_comment', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent', 'quiz_head',
                    'quiz_media_file2']
    # readonly_fields = ['subject_code', 'quiz_type', 'quiz_question', 'quiz_media_type', 'quiz_media_file', 'quiz_score', 'quiz_comment', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent', 'quiz_head', 'quiz_media_file2']


admin.site.register(QuizInfo, QuizInfoAdmin)


# AssignmentInfoModels
class AssignmentInfoAdminForm(forms.ModelForm):
    class Meta:
        model = AssignmentInfo
        fields = '__all__'


class AssignmentInfoAdmin(admin.ModelAdmin):
    form = AssignmentInfoAdminForm
    list_display = ['Course_Code', 'Chapter_Code', 'Assignment_Topic', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime', 'Assignment_Deadline', 'Register_Agent']
    # readonly_fields = ['subject_code', 'level_score', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'level']


admin.site.register(AssignmentInfo, AssignmentInfoAdmin)


class QuestionInfoAdminForm(forms.ModelForm):
    class Meta:
        model = QuestionInfo
        fields = '__all__'


class QuestionInfoAdmin(admin.ModelAdmin):
    form = QuestionInfoAdminForm
    list_display = ['Question_Title', 'Question_Score', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
                    'Register_Agent', 'Question_Media_File', 'Question_Description', 'Assignment_Code',
                    'Answer_Choices', 'Answer_Type']
    # readonly_fields = ['subject_code', 'question_type', 'use_flag', 'reg_date', 'reg_time', 'udt_date', 'udt_time', 'udt_agent']


admin.site.register(QuestionInfo, QuestionInfoAdmin)


class AssignAssignmentInfoAdminForm(forms.ModelForm):
    class Meta:
        model = AssignAssignmentInfo
        fields = '__all__'


class AssignAssignmentInfoAdmin(admin.ModelAdmin):
    form = AssignAssignmentInfoAdminForm
    list_display = ['Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Inning_Code', 'Assignment_Code',
                    'Assigned_By']
    # readonly_fields = ['subject_code', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']


admin.site.register(AssignAssignmentInfo, AssignAssignmentInfoAdmin)


#
# class AssignQuestionInfoAdminForm(forms.ModelForm):
#     class Meta:
#         model = AssignQuestionInfo
#         fields = '__all__'
#
#
# class AssignQuestionInfoAdmin(admin.ModelAdmin):
#     form = AssignQuestionInfoAdminForm
#     list_display = ['Question_Code', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
#                     'Register_Agent', 'Assignment_Code']
#     # readonly_fields = ['subject_code', 'question_type', 'use_flag', 'reg_date', 'reg_time', 'udt_date', 'udt_time', 'udt_agent']
#
#
# admin.site.register(AssignQuestionInfo, AssignQuestionInfoAdmin)


class AssignAnswerInfoAdminForm(forms.ModelForm):
    class Meta:
        model = AssignAnswerInfo
        fields = '__all__'


class AssignAnswerInfoAdmin(admin.ModelAdmin):
    form = AssignAnswerInfoAdminForm
    list_display = ['Assignment_Score', 'Question_Code',
                    'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Assignment_Answer', 'Student_Code']
    # readonly_fields = ['subject_code', 'question_type', 'question_answer', 'question_idx', 'question_correct', 'question_score', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']


admin.site.register(AssignAnswerInfo, AssignAnswerInfoAdmin)


class BoardInfoAdminForm(forms.ModelForm):
    class Meta:
        model = BoardInfo
        fields = '__all__'


class BoardInfoAdmin(admin.ModelAdmin):
    form = BoardInfoAdminForm
    list_display = ['board_name', 'board_write_level', 'board_read_level', 'board_reply_level', 'board_new_time',
                    'board_create_time', 'admin_id', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
                    'Register_Agent']
    # readonly_fields = ['board_name', 'board_write_level', 'board_read_level', 'board_reply_level', 'board_new_time', 'board_create_time', 'admin_id', 'use_flag', 'reg_date', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']


admin.site.register(BoardInfo, BoardInfoAdmin)


class BoardContentInfoAdminForm(forms.ModelForm):
    class Meta:
        model = BoardContentInfo
        fields = '__all__'


class BoardContentInfoAdmin(admin.ModelAdmin):
    form = BoardContentInfoAdminForm
    list_display = ['admin_id', 'title', 'contents', 'writer', 'view_cnt', 'ref_code', 'ref_step', 'ref_level',
                    'write_time', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']
    # readonly_fields = ['admin_id', 'title', 'contents', 'writer', 'view_cnt', 'ref_code', 'ref_step', 'ref_level', 'write_time', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']


admin.site.register(BoardContentInfo, BoardContentInfoAdmin)


class SessionInfoAdminForm(forms.ModelForm):
    class Meta:
        model = SessionInfo
        fields = '__all__'


class SessionInfoAdmin(admin.ModelAdmin):
    form = SessionInfoAdminForm
    list_display = ['Session_Name', 'Description', 'Use_Flag', 'Center_Code']
    # readonly_fields = ['inning_name', 'start_date', 'end_date', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']


admin.site.register(SessionInfo, SessionInfoAdmin)


class InningGroupAdminForm(forms.ModelForm):
    class Meta:
        model = InningGroup
        fields = '__all__'


class InningGroupAdmin(admin.ModelAdmin):
    form = InningGroupAdminForm
    list_display = ['InningGroup_Name', 'Course_Code', 'Center_Code', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime', 'Register_Agent']
    # readonly_fields = ['teacher_code', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']


admin.site.register(InningGroup, InningGroupAdmin)


class InningInfoAdminForm(forms.ModelForm):
    class Meta:
        model = InningInfo
        fields = '__all__'


class InningInfoAdmin(admin.ModelAdmin):
    form = InningInfoAdminForm
    list_display = ['Inning_Name', 'Start_Date', 'End_Date', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime',
                    'Register_Agent', 'Center_Code', 'Groups']
    # readonly_fields = ['inning_name', 'start_date', 'end_date', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']


admin.site.register(InningInfo, InningInfoAdmin)


class GroupMappingAdminForm(forms.ModelForm):
    class Meta:
        model = GroupMapping
        fields = '__all__'


class GroupMappingAdmin(admin.ModelAdmin):
    form = GroupMappingAdminForm
    list_display = ['GroupMapping_Name', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
                    'Register_Agent', 'Center_Code']
    # readonly_fields = ['use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']


admin.site.register(GroupMapping, GroupMappingAdmin)


class ChapterContentMediaAdminForm(forms.ModelForm):
    class Meta:
        model = ChapterContentMedia
        fields = '__all__'


class ChapterContentMediaAdmin(admin.ModelAdmin):
    form = ChapterContentMediaAdminForm
    list_display = ['media_type', 'media_desc', 'media_filename', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
                    'Register_Agent']
    # readonly_fields = ['media_type', 'media_desc', 'media_filename', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']


admin.site.register(ChapterContentMedia, ChapterContentMediaAdmin)


class ChapterImgInfoAdminForm(forms.ModelForm):
    class Meta:
        model = ChapterImgInfo
        fields = '__all__'


class ChapterImgInfoAdmin(admin.ModelAdmin):
    form = ChapterImgInfoAdminForm
    list_display = ['filename', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']
    # readonly_fields = ['filename', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']


admin.site.register(ChapterImgInfo, ChapterImgInfoAdmin)


class ChapterMissonCheckAdminForm(forms.ModelForm):
    class Meta:
        model = ChapterMissonCheck
        fields = '__all__'


class ChapterMissonCheckAdmin(admin.ModelAdmin):
    form = ChapterMissonCheckAdminForm
    list_display = ['check_code', 'student_code', 'check_agent_code', 'is_check_yn', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime', 'Register_Agent']
    # readonly_fields = ['check_code', 'student_code', 'check_agent_code', 'is_check_yn', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']


admin.site.register(ChapterMissonCheck, ChapterMissonCheckAdmin)


class ChapterWriteAdminForm(forms.ModelForm):
    class Meta:
        model = ChapterWrite
        fields = '__all__'


class ChapterWriteAdmin(admin.ModelAdmin):
    form = ChapterWriteAdminForm
    list_display = ['student_code', 'write_content', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
                    'Register_Agent']
    # readonly_fields = ['student_code', 'write_content', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']


admin.site.register(ChapterWrite, ChapterWriteAdmin)


class LearningNoteAdminForm(forms.ModelForm):
    class Meta:
        model = LearningNote
        fields = '__all__'


class LearningNoteAdmin(admin.ModelAdmin):
    form = LearningNoteAdminForm
    list_display = ['contents_code', 'note_contents', 'note_attachment']
    # readonly_fields = ['contents_code', 'note_contents', 'note_attachment']


admin.site.register(LearningNote, LearningNoteAdmin)


class CourseUbtInfoAdminForm(forms.ModelForm):
    class Meta:
        model = CourseUbtInfo
        fields = '__all__'


class CourseUbtInfoAdmin(admin.ModelAdmin):
    form = CourseUbtInfoAdminForm
    list_display = ['Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']
    # readonly_fields = ['use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']


admin.site.register(CourseUbtInfo, CourseUbtInfoAdmin)


class LessonInfoAdminForm(forms.ModelForm):
    class Meta:
        model = LessonInfo
        fields = '__all__'


class LessonInfoAdmin(admin.ModelAdmin):
    form = LessonInfoAdminForm
    list_display = ['teacher_code', 'start_date', 'end_date', 'progress', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime', 'Register_Agent', 'ubt_start', 'ubt_end', 'download_count', 'download_date']
    # readonly_fields = ['teacher_code', 'start_date', 'end_date', 'progress', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent', 'ubt_start', 'ubt_end', 'download_count', 'download_date']


admin.site.register(LessonInfo, LessonInfoAdmin)


class LessonLogAdminForm(forms.ModelForm):
    class Meta:
        model = LessonLog
        fields = '__all__'


class LessonLogAdmin(admin.ModelAdmin):
    form = LessonLogAdminForm
    list_display = ['member_id', 'member_ip', 'member_browser', 'member_os', 'start_date', 'start_time', 'end_date',
                    'end_time', 'connect_date', 'connect_time', 'connect_count', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime', 'Register_Agent', 'study_time', 'connect_page']
    # readonly_fields = ['member_id', 'member_ip', 'member_browser', 'member_os', 'start_date', 'start_time', 'end_date', 'end_time', 'connect_date', 'connect_time', 'connect_count', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent', 'study_time', 'connect_page']


admin.site.register(LessonLog, LessonLogAdmin)


class MemberGroupAdminForm(forms.ModelForm):
    class Meta:
        model = MemberGroup
        fields = '__all__'


class MemberGroupAdmin(admin.ModelAdmin):
    form = MemberGroupAdminForm
    list_display = ['group_name', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']
    # readonly_fields = ['group_name', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']


admin.site.register(MemberGroup, MemberGroupAdmin)


class MessageInfoAdminForm(forms.ModelForm):
    class Meta:
        model = MessageInfo
        fields = '__all__'


class MessageInfoAdmin(admin.ModelAdmin):
    form = MessageInfoAdminForm
    list_display = ['teacher_code', 'message', 'message_read', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
                    'Register_Agent']
    # readonly_fields = ['teacher_code', 'message', 'message_read', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']


admin.site.register(MessageInfo, MessageInfoAdmin)


# class OmrAnswerInfoAdminForm(forms.ModelForm):
#     class Meta:
#         model = OmrAnswerInfo
#         fields = '__all__'
#
#
# class OmrAnswerInfoAdmin(admin.ModelAdmin):
#     form = OmrAnswerInfoAdminForm
#     list_display = ['Answer_Description', 'Student_Code', 'Question_Code', 'Answer_Score', 'Use_Flag',
#                     'Register_DateTime', 'Updated_DateTime']
#     # readonly_fields = ['subject_code', 'omr_answer', 'omr_answer_idx', 'omr_answer_correct', 'question_score', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']
#
#
# admin.site.register(OmrAnswerInfo, OmrAnswerInfoAdmin)


# class OmrAssignInfoAdminForm(forms.ModelForm):
#     class Meta:
#         model = OmrAssignInfo
#         fields = '__all__'
#
#
# class OmrAssignInfoAdmin(admin.ModelAdmin):
#     form = OmrAssignInfoAdminForm
#     list_display = ['subject_code', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']
#     # readonly_fields = ['subject_code', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']
#
#
# admin.site.register(OmrAssignInfo, OmrAssignInfoAdmin)
#
#
# class OmrExampleInfoAdminForm(forms.ModelForm):
#     class Meta:
#         model = OmrExampleInfo
#         fields = '__all__'
#
#
# class OmrExampleInfoAdmin(admin.ModelAdmin):
#     form = OmrExampleInfoAdminForm
#     list_display = ['omr_example_correct', 'omr_example_idx', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
#                     'Register_Agent']
#     # readonly_fields = ['omr_example_correct', 'omr_example_idx', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']
#
#
# admin.site.register(OmrExampleInfo, OmrExampleInfoAdmin)


# class QAnswerLogAdminForm(forms.ModelForm):
#     class Meta:
#         model = QAnswerLog
#         fields = '__all__'


# class QAnswerLogAdmin(admin.ModelAdmin):
#     form = QAnswerLogAdminForm
#     list_display = ['question_answer', 'question_idx', 'question_score', 'Use_Flag', 'Register_DateTime',
#                     'Updated_DateTime', 'Register_Agent']
#     # readonly_fields = ['question_answer', 'question_idx', 'question_score', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']
#
#
# admin.site.register(QAnswerLog, QAnswerLogAdmin)


class QExampleInfoAdminForm(forms.ModelForm):
    class Meta:
        model = QExampleInfo
        fields = '__all__'


class QExampleInfoAdmin(admin.ModelAdmin):
    form = QExampleInfoAdminForm
    list_display = ['q_example', 'q_example_correct', 'q_example_idx', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime', 'Register_Agent', 'q_example_type']
    # readonly_fields = ['q_example', 'q_example_correct', 'q_example_idx', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent', 'q_example_type']


admin.site.register(QExampleInfo, QExampleInfoAdmin)


class QuizAnswerInfoAdminForm(forms.ModelForm):
    class Meta:
        model = QuizAnswerInfo
        fields = '__all__'


class QuizAnswerInfoAdmin(admin.ModelAdmin):
    form = QuizAnswerInfoAdminForm
    list_display = ['subject_code', 'quiz_type', 'quiz_answer', 'quiz_answer_idx', 'quiz_correct', 'quiz_score',
                    'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent', 'test_type']
    # readonly_fields = ['subject_code', 'quiz_type', 'quiz_answer', 'quiz_answer_idx', 'quiz_correct', 'quiz_score', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent', 'test_type']


admin.site.register(QuizAnswerInfo, QuizAnswerInfoAdmin)


class QuizExampleInfoAdminForm(forms.ModelForm):
    class Meta:
        model = QuizExampleInfo
        fields = '__all__'


class QuizExampleInfoAdmin(admin.ModelAdmin):
    form = QuizExampleInfoAdminForm
    list_display = ['quiz_example', 'quiz_example_correct', 'quiz_example_idx', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime', 'Register_Agent', 'quiz_example_type']
    # readonly_fields = ['quiz_example', 'quiz_example_correct', 'quiz_example_idx', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent', 'quiz_example_type']


admin.site.register(QuizExampleInfo, QuizExampleInfoAdmin)


class ScheduleInfoAdminForm(forms.ModelForm):
    class Meta:
        model = ScheduleInfo
        fields = '__all__'


class ScheduleInfoAdmin(admin.ModelAdmin):
    form = ScheduleInfoAdminForm
    list_display = ['title', 'content', 'start_date', 'start_time', 'end_date', 'end_time', 'Use_Flag',
                    'Register_DateTime', 'Updated_DateTime', 'Register_Agent']
    # readonly_fields = ['title', 'content', 'start_date', 'start_time', 'end_date', 'end_time', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']


admin.site.register(ScheduleInfo, ScheduleInfoAdmin)


class TalkMemberAdminForm(forms.ModelForm):
    class Meta:
        model = TalkMember
        fields = '__all__'


class TalkMemberAdmin(admin.ModelAdmin):
    form = TalkMemberAdminForm
    list_display = ['use_flag']
    # readonly_fields = ['use_flag']


admin.site.register(TalkMember, TalkMemberAdmin)


class TalkRoomAdminForm(forms.ModelForm):
    class Meta:
        model = TalkRoom
        fields = '__all__'


class TalkRoomAdmin(admin.ModelAdmin):
    form = TalkRoomAdminForm
    list_display = ['talk_room_cate_code', 'use_flag']
    # readonly_fields = ['talk_room_cate_code', 'use_flag']


admin.site.register(TalkRoom, TalkRoomAdmin)


class TalkMessageAdminForm(forms.ModelForm):
    class Meta:
        model = TalkMessage
        fields = '__all__'


class TalkMessageAdmin(admin.ModelAdmin):
    form = TalkMessageAdminForm
    list_display = ['message', 'sender_member_code', 'send_date', 'send_time']
    # readonly_fields = ['message', 'sender_member_code', 'send_date', 'send_time']


admin.site.register(TalkMessage, TalkMessageAdmin)


class TalkMessageReadAdminForm(forms.ModelForm):
    class Meta:
        model = TalkMessageRead
        fields = '__all__'


class TalkMessageReadAdmin(admin.ModelAdmin):
    form = TalkMessageReadAdminForm
    list_display = ['is_read']
    # readonly_fields = ['is_read']


admin.site.register(TalkMessageRead, TalkMessageReadAdmin)


class TodoInfoAdminForm(forms.ModelForm):
    class Meta:
        model = TodoInfo
        fields = '__all__'


class TodoInfoAdmin(admin.ModelAdmin):
    form = TodoInfoAdminForm
    list_display = ['todo_comment', 'todo_status', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
                    'Register_Agent', 'teacher_code', 'todo_title', 'start_date', 'start_time', 'end_date', 'end_time']
    # readonly_fields = ['todo_comment', 'todo_status', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent', 'teacher_code', 'todo_title', 'start_date', 'start_time', 'end_date', 'end_time']


admin.site.register(TodoInfo, TodoInfoAdmin)


class TodoTInfoAdminForm(forms.ModelForm):
    class Meta:
        model = TodoTInfo
        fields = '__all__'


class TodoTInfoAdmin(admin.ModelAdmin):
    form = TodoTInfoAdminForm
    list_display = ['todo_code', 'todo_t_flag', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']
    # readonly_fields = ['todo_code', 'todo_t_flag', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent']


admin.site.register(TodoTInfo, TodoTInfoAdmin)
