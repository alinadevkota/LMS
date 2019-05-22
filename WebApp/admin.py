from django.contrib import admin
from django import forms
from .models import AssignHomeworkInfo, AssignQuestionInfo, BoardContentInfo, BoardInfo, CenterInfo, ChapterContentMedia, ChapterContentsInfo, ChapterImgInfo, ChapterInfo, ChapterMissonCheck, ChapterMissonCheckCard, ChapterMissonCheckItem, ChapterWrite, GroupMapping, HomeworkInfo, InningGroup, InningInfo, LearningNote, LectureInfo, LectureUbtInfo, LessonInfo, LessonLog, MemberGroup, MemberInfo, MessageInfo, OmrAnswerInfo, OmrAssignInfo, OmrExampleInfo, OmrQuestionInfo, QAnswerInfo, QAnswerLog, QExampleInfo, QuestionInfo, QuizAnswerInfo, QuizExampleInfo, QuizInfo, ScheduleInfo, TalkMember, TalkMessage, TalkMessageRead, TalkRoom, TodoInfo, TodoTInfo

class AssignHomeworkInfoAdminForm(forms.ModelForm):

    class Meta:
        model = AssignHomeworkInfo
        fields = '__all__'


class AssignHomeworkInfoAdmin(admin.ModelAdmin):
    form = AssignHomeworkInfoAdminForm
    list_display = ['question_code', 'subject_code', 'lecture_code', 'chapter_code', 'member_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']
    #readonly_fields = ['question_code', 'subject_code', 'lecture_code', 'chapter_code', 'member_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']

admin.site.register(AssignHomeworkInfo, AssignHomeworkInfoAdmin)


class AssignQuestionInfoAdminForm(forms.ModelForm):

    class Meta:
        model = AssignQuestionInfo
        fields = '__all__'


class AssignQuestionInfoAdmin(admin.ModelAdmin):
    form = AssignQuestionInfoAdminForm
    list_display = ['question_code', 'subject_code', 'lecture_code', 'chapter_code', 'question_type', 'use_flag', 'reg_date', 'reg_time', 'udt_date', 'udt_time', 'udt_agent']
    #readonly_fields = ['question_code', 'subject_code', 'lecture_code', 'chapter_code', 'question_type', 'use_flag', 'reg_date', 'reg_time', 'udt_date', 'udt_time', 'udt_agent']

admin.site.register(AssignQuestionInfo, AssignQuestionInfoAdmin)


class BoardContentInfoAdminForm(forms.ModelForm):

    class Meta:
        model = BoardContentInfo
        fields = '__all__'


class BoardContentInfoAdmin(admin.ModelAdmin):
    form = BoardContentInfoAdminForm
    list_display = ['board_code', 'admin_id', 'title', 'contents', 'writer', 'view_cnt', 'ref_code', 'ref_step', 'ref_level', 'write_time', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']
    #readonly_fields = ['board_code', 'admin_id', 'title', 'contents', 'writer', 'view_cnt', 'ref_code', 'ref_step', 'ref_level', 'write_time', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']

admin.site.register(BoardContentInfo, BoardContentInfoAdmin)


class BoardInfoAdminForm(forms.ModelForm):

    class Meta:
        model = BoardInfo
        fields = '__all__'


class BoardInfoAdmin(admin.ModelAdmin):
    form = BoardInfoAdminForm
    list_display = ['board_name', 'board_write_level', 'board_read_level', 'board_reply_level', 'board_new_time', 'board_create_time', 'admin_id', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']
    #readonly_fields = ['board_name', 'board_write_level', 'board_read_level', 'board_reply_level', 'board_new_time', 'board_create_time', 'admin_id', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']

admin.site.register(BoardInfo, BoardInfoAdmin)


class CenterInfoAdminForm(forms.ModelForm):

    class Meta:
        model = CenterInfo
        fields = '__all__'


class CenterInfoAdmin(admin.ModelAdmin):
    form = CenterInfoAdminForm
    list_display = ['center_name', 'center_location', 'center_tel', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']
    #readonly_fields = ['center_name', 'center_location', 'center_tel', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']

admin.site.register(CenterInfo, CenterInfoAdmin)


class ChapterContentMediaAdminForm(forms.ModelForm):

    class Meta:
        model = ChapterContentMedia
        fields = '__all__'


class ChapterContentMediaAdmin(admin.ModelAdmin):
    form = ChapterContentMediaAdminForm
    list_display = ['chapter_contents_code', 'media_type', 'media_desc', 'media_filename', 'use_flag', 'reg_date', 'reg_time', 'udt_date', 'udt_time', 'reg_agent', 'udt_agent']
    #readonly_fields = ['chapter_contents_code', 'media_type', 'media_desc', 'media_filename', 'use_flag', 'reg_date', 'reg_time', 'udt_date', 'udt_time', 'reg_agent', 'udt_agent']

admin.site.register(ChapterContentMedia, ChapterContentMediaAdmin)


class ChapterContentsInfoAdminForm(forms.ModelForm):

    class Meta:
        model = ChapterContentsInfo
        fields = '__all__'


class ChapterContentsInfoAdmin(admin.ModelAdmin):
    form = ChapterContentsInfoAdminForm
    list_display = ['chapter_code', 'chapter_contents', 'chapter_audio', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'contents_index', 'chapter_type', 'thum_file', 'vod_file', 'today', 'front1_img', 'front1_text', 'back1_img', 'back1_text', 'pdf_file', 'front2_img', 'front3_img', 'front4_img', 'front2_text', 'front3_text', 'front4_text', 'back2_img', 'back3_img', 'back4_img', 'back2_text', 'back3_text', 'back4_text', 'c1_audio', 'c2_audio', 'c3_audio', 'c4_audio', 'vod_size', 'offline_file', 'teacher_guide', 'today_text', 'contents_text', 'pbl_allow', 'pbl_lec_allow']
    #readonly_fields = ['chapter_code', 'chapter_contents', 'chapter_audio', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'contents_index', 'chapter_type', 'thum_file', 'vod_file', 'today', 'front1_img', 'front1_text', 'back1_img', 'back1_text', 'pdf_file', 'front2_img', 'front3_img', 'front4_img', 'front2_text', 'front3_text', 'front4_text', 'back2_img', 'back3_img', 'back4_img', 'back2_text', 'back3_text', 'back4_text', 'c1_audio', 'c2_audio', 'c3_audio', 'c4_audio', 'vod_size', 'offline_file', 'teacher_guide', 'today_text', 'contents_text', 'pbl_allow', 'pbl_lec_allow']

admin.site.register(ChapterContentsInfo, ChapterContentsInfoAdmin)


class ChapterImgInfoAdminForm(forms.ModelForm):

    class Meta:
        model = ChapterImgInfo
        fields = '__all__'


class ChapterImgInfoAdmin(admin.ModelAdmin):
    form = ChapterImgInfoAdminForm
    list_display = ['chapter_code', 'filename', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']
    #readonly_fields = ['chapter_code', 'filename', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']

admin.site.register(ChapterImgInfo, ChapterImgInfoAdmin)


class ChapterInfoAdminForm(forms.ModelForm):

    class Meta:
        model = ChapterInfo
        fields = '__all__'


class ChapterInfoAdmin(admin.ModelAdmin):
    form = ChapterInfoAdminForm
    list_display = ['lecture_code', 'chapter_no', 'chapter_name', 'topic', 'summary', 'page_num', 'vod_size', 'intro', 'target', 'top_img', 'bottom_img1', 'bottom_img2', 'bottom_img3', 'thum_file', 'vod_file', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'today', 'chapter_type', 'prologue_type', 'tabset', 'chapter_image', 'chapter_use', 'offline_file', 'pre_test_type', 'post_test_type', 'level1_avg', 'level2_avg', 'level3_avg', 'level1_hard_avg', 'level1_medium_avg', 'level1_easy_avg', 'level2_hard_avg', 'level2_medium_avg', 'level2_easy_avg', 'level3_hard_avg', 'level3_medium_avg', 'level3_easy_avg', 'homework_count', 'epilogue_type', 'epilogue_img', 'pbl_flag', 'chapter_use_time']
    #readonly_fields = ['lecture_code', 'chapter_no', 'chapter_name', 'topic', 'summary', 'page_num', 'vod_size', 'intro', 'target', 'top_img', 'bottom_img1', 'bottom_img2', 'bottom_img3', 'thum_file', 'vod_file', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'today', 'chapter_type', 'prologue_type', 'tabset', 'chapter_image', 'chapter_use', 'offline_file', 'pre_test_type', 'post_test_type', 'level1_avg', 'level2_avg', 'level3_avg', 'level1_hard_avg', 'level1_medium_avg', 'level1_easy_avg', 'level2_hard_avg', 'level2_medium_avg', 'level2_easy_avg', 'level3_hard_avg', 'level3_medium_avg', 'level3_easy_avg', 'homework_count', 'epilogue_type', 'epilogue_img', 'pbl_flag', 'chapter_use_time']

admin.site.register(ChapterInfo, ChapterInfoAdmin)


class ChapterMissonCheckAdminForm(forms.ModelForm):

    class Meta:
        model = ChapterMissonCheck
        fields = '__all__'


class ChapterMissonCheckAdmin(admin.ModelAdmin):
    form = ChapterMissonCheckAdminForm
    list_display = ['check_code', 'check_item_code', 'student_code', 'check_agent_code', 'is_check_yn', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'inning_code']
    #readonly_fields = ['check_code', 'check_item_code', 'student_code', 'check_agent_code', 'is_check_yn', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'inning_code']

admin.site.register(ChapterMissonCheck, ChapterMissonCheckAdmin)


class ChapterMissonCheckCardAdminForm(forms.ModelForm):

    class Meta:
        model = ChapterMissonCheckCard
        fields = '__all__'


class ChapterMissonCheckCardAdmin(admin.ModelAdmin):
    form = ChapterMissonCheckCardAdminForm
    list_display = ['check_card_code', 'chapter_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']
    #readonly_fields = ['check_card_code', 'chapter_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']

admin.site.register(ChapterMissonCheckCard, ChapterMissonCheckCardAdmin)


class ChapterMissonCheckItemAdminForm(forms.ModelForm):

    class Meta:
        model = ChapterMissonCheckItem
        fields = '__all__'


class ChapterMissonCheckItemAdmin(admin.ModelAdmin):
    form = ChapterMissonCheckItemAdminForm
    list_display = ['check_item_code', 'check_card_code', 'item_text', 'contents_text', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'chapter_contents_code']
    #readonly_fields = ['check_item_code', 'check_card_code', 'item_text', 'contents_text', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'chapter_contents_code']

admin.site.register(ChapterMissonCheckItem, ChapterMissonCheckItemAdmin)


class ChapterWriteAdminForm(forms.ModelForm):

    class Meta:
        model = ChapterWrite
        fields = '__all__'


class ChapterWriteAdmin(admin.ModelAdmin):
    form = ChapterWriteAdminForm
    list_display = ['inning_code', 'chapter_contents_code', 'student_code', 'write_content', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']
    #readonly_fields = ['inning_code', 'chapter_contents_code', 'student_code', 'write_content', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']

admin.site.register(ChapterWrite, ChapterWriteAdmin)


class GroupMappingAdminForm(forms.ModelForm):

    class Meta:
        model = GroupMapping
        fields = '__all__'


class GroupMappingAdmin(admin.ModelAdmin):
    form = GroupMappingAdminForm
    list_display = ['center_code', 'group_code', 'member_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']
    #readonly_fields = ['center_code', 'group_code', 'member_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']

admin.site.register(GroupMapping, GroupMappingAdmin)


class HomeworkInfoAdminForm(forms.ModelForm):

    class Meta:
        model = HomeworkInfo
        fields = '__all__'


class HomeworkInfoAdmin(admin.ModelAdmin):
    form = HomeworkInfoAdminForm
    list_display = ['question_code', 'subject_code', 'lecture_code', 'chapter_code', 'level_score', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'level']
    #readonly_fields = ['question_code', 'subject_code', 'lecture_code', 'chapter_code', 'level_score', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'level']

admin.site.register(HomeworkInfo, HomeworkInfoAdmin)


class InningGroupAdminForm(forms.ModelForm):

    class Meta:
        model = InningGroup
        fields = '__all__'


class InningGroupAdmin(admin.ModelAdmin):
    form = InningGroupAdminForm
    list_display = ['center_code', 'inning_code', 'lecture_code', 'teacher_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']
    #readonly_fields = ['center_code', 'inning_code', 'lecture_code', 'teacher_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']

admin.site.register(InningGroup, InningGroupAdmin)


class InningInfoAdminForm(forms.ModelForm):

    class Meta:
        model = InningInfo
        fields = '__all__'


class InningInfoAdmin(admin.ModelAdmin):
    form = InningInfoAdminForm
    list_display = ['inning_name', 'lecture_code', 'start_date', 'end_date', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'center_code']
    #readonly_fields = ['inning_name', 'lecture_code', 'start_date', 'end_date', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'center_code']

admin.site.register(InningInfo, InningInfoAdmin)


class LearningNoteAdminForm(forms.ModelForm):

    class Meta:
        model = LearningNote
        fields = '__all__'


class LearningNoteAdmin(admin.ModelAdmin):
    form = LearningNoteAdminForm
    list_display = ['inning_code', 'lecture_code', 'chapter_code', 'contents_code', 'note_contents', 'note_attachment']
    #readonly_fields = ['inning_code', 'lecture_code', 'chapter_code', 'contents_code', 'note_contents', 'note_attachment']

admin.site.register(LearningNote, LearningNoteAdmin)


class LectureInfoAdminForm(forms.ModelForm):

    class Meta:
        model = LectureInfo
        fields = '__all__'


class LectureInfoAdmin(admin.ModelAdmin):
    form = LectureInfoAdminForm
    list_display = ['lecture_name', 'lecture_teacher', 'lecture_cover', 'lecture_cover_file', 'lecture_level', 'lecture_info', 'teacher', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'lecture_certification', 'lecture_provider', 'cert_crit_prog', 'cert_crit_post', 'cert_crit_ubt', 'cert_crit_issue', 'center_code']
    #readonly_fields = ['lecture_name', 'lecture_teacher', 'lecture_cover', 'lecture_cover_file', 'lecture_level', 'lecture_info', 'teacher', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'lecture_certification', 'lecture_provider', 'cert_crit_prog', 'cert_crit_post', 'cert_crit_ubt', 'cert_crit_issue', 'center_code']

admin.site.register(LectureInfo, LectureInfoAdmin)


class LectureUbtInfoAdminForm(forms.ModelForm):

    class Meta:
        model = LectureUbtInfo
        fields = '__all__'


class LectureUbtInfoAdmin(admin.ModelAdmin):
    form = LectureUbtInfoAdminForm
    list_display = ['quiz_code', 'lecture_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']
    #readonly_fields = ['quiz_code', 'lecture_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']

admin.site.register(LectureUbtInfo, LectureUbtInfoAdmin)


class LessonInfoAdminForm(forms.ModelForm):

    class Meta:
        model = LessonInfo
        fields = '__all__'


class LessonInfoAdmin(admin.ModelAdmin):
    form = LessonInfoAdminForm
    list_display = ['lecture_code', 'member_code', 'teacher_code', 'start_date', 'end_date', 'progress', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'ubt_start', 'ubt_end', 'download_count', 'download_date', 'center_code', 'inning_code']
    #readonly_fields = ['lecture_code', 'member_code', 'teacher_code', 'start_date', 'end_date', 'progress', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'ubt_start', 'ubt_end', 'download_count', 'download_date', 'center_code', 'inning_code']

admin.site.register(LessonInfo, LessonInfoAdmin)


class LessonLogAdminForm(forms.ModelForm):

    class Meta:
        model = LessonLog
        fields = '__all__'


class LessonLogAdmin(admin.ModelAdmin):
    form = LessonLogAdminForm
    list_display = ['lesson_code', 'lecture_code', 'chapter_code', 'member_code', 'member_id', 'member_ip', 'member_browser', 'member_os', 'start_date', 'start_time', 'end_date', 'end_time', 'connect_date', 'connect_time', 'connect_count', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'study_time', 'connect_page']
    #readonly_fields = ['lesson_code', 'lecture_code', 'chapter_code', 'member_code', 'member_id', 'member_ip', 'member_browser', 'member_os', 'start_date', 'start_time', 'end_date', 'end_time', 'connect_date', 'connect_time', 'connect_count', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'study_time', 'connect_page']

admin.site.register(LessonLog, LessonLogAdmin)


class MemberGroupAdminForm(forms.ModelForm):

    class Meta:
        model = MemberGroup
        fields = '__all__'


class MemberGroupAdmin(admin.ModelAdmin):
    form = MemberGroupAdminForm
    list_display = ['center_code', 'group_name', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']
    #readonly_fields = ['center_code', 'group_name', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']

admin.site.register(MemberGroup, MemberGroupAdmin)


class MemberInfoAdminForm(forms.ModelForm):

    class Meta:
        model = MemberInfo
        fields = '__all__'


class MemberInfoAdmin(admin.ModelAdmin):
    form = MemberInfoAdminForm
    list_display = ['member_id', 'member_level', 'member_pw', 'member_name', 'member_jumin', 'member_birth', 'member_college', 'member_email', 'member_phone', 'member_post', 'member_addr1', 'member_addr2', 'member_file', 'member_gender', 'member_major', 'member_nation', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'center_code', 'member_fax', 'member_memo']
    #readonly_fields = ['member_id', 'member_level', 'member_pw', 'member_name', 'member_jumin', 'member_birth', 'member_college', 'member_email', 'member_phone', 'member_post', 'member_addr1', 'member_addr2', 'member_file', 'member_gender', 'member_major', 'member_nation', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'center_code', 'member_fax', 'member_memo']

admin.site.register(MemberInfo, MemberInfoAdmin)


class MessageInfoAdminForm(forms.ModelForm):

    class Meta:
        model = MessageInfo
        fields = '__all__'


class MessageInfoAdmin(admin.ModelAdmin):
    form = MessageInfoAdminForm
    list_display = ['teacher_code', 'member_code', 'message', 'message_read', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']
    #readonly_fields = ['teacher_code', 'member_code', 'message', 'message_read', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']

admin.site.register(MessageInfo, MessageInfoAdmin)


class OmrAnswerInfoAdminForm(forms.ModelForm):

    class Meta:
        model = OmrAnswerInfo
        fields = '__all__'


class OmrAnswerInfoAdmin(admin.ModelAdmin):
    form = OmrAnswerInfoAdminForm
    list_display = ['subject_code', 'lecture_code', 'chapter_code', 'member_code', 'question_code', 'omr_answer', 'omr_answer_idx', 'omr_answer_correct', 'question_score', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'lesson_code']
    #readonly_fields = ['subject_code', 'lecture_code', 'chapter_code', 'member_code', 'question_code', 'omr_answer', 'omr_answer_idx', 'omr_answer_correct', 'question_score', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'lesson_code']

admin.site.register(OmrAnswerInfo, OmrAnswerInfoAdmin)


class OmrAssignInfoAdminForm(forms.ModelForm):

    class Meta:
        model = OmrAssignInfo
        fields = '__all__'


class OmrAssignInfoAdmin(admin.ModelAdmin):
    form = OmrAssignInfoAdminForm
    list_display = ['question_code', 'subject_code', 'lecture_code', 'chapter_code', 'member_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']
    #readonly_fields = ['question_code', 'subject_code', 'lecture_code', 'chapter_code', 'member_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']

admin.site.register(OmrAssignInfo, OmrAssignInfoAdmin)


class OmrExampleInfoAdminForm(forms.ModelForm):

    class Meta:
        model = OmrExampleInfo
        fields = '__all__'


class OmrExampleInfoAdmin(admin.ModelAdmin):
    form = OmrExampleInfoAdminForm
    list_display = ['question_code', 'omr_example_correct', 'omr_example_idx', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']
    #readonly_fields = ['question_code', 'omr_example_correct', 'omr_example_idx', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']

admin.site.register(OmrExampleInfo, OmrExampleInfoAdmin)


class OmrQuestionInfoAdminForm(forms.ModelForm):

    class Meta:
        model = OmrQuestionInfo
        fields = '__all__'


class OmrQuestionInfoAdmin(admin.ModelAdmin):
    form = OmrQuestionInfoAdminForm
    list_display = ['subject_code', 'lecture_code', 'chapter_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'question_level', 'question_score']
    #readonly_fields = ['subject_code', 'lecture_code', 'chapter_code', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'question_level', 'question_score']

admin.site.register(OmrQuestionInfo, OmrQuestionInfoAdmin)


class QAnswerInfoAdminForm(forms.ModelForm):

    class Meta:
        model = QAnswerInfo
        fields = '__all__'


class QAnswerInfoAdmin(admin.ModelAdmin):
    form = QAnswerInfoAdminForm
    list_display = ['subject_code', 'lecture_code', 'chapter_code', 'member_code', 'question_code', 'question_type', 'question_answer', 'question_idx', 'question_correct', 'question_score', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'lesson_code']
    #readonly_fields = ['subject_code', 'lecture_code', 'chapter_code', 'member_code', 'question_code', 'question_type', 'question_answer', 'question_idx', 'question_correct', 'question_score', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'lesson_code']

admin.site.register(QAnswerInfo, QAnswerInfoAdmin)


class QAnswerLogAdminForm(forms.ModelForm):

    class Meta:
        model = QAnswerLog
        fields = '__all__'


class QAnswerLogAdmin(admin.ModelAdmin):
    form = QAnswerLogAdminForm
    list_display = ['lecture_code', 'member_code', 'question_code', 'question_answer', 'question_idx', 'question_score', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']
    #readonly_fields = ['lecture_code', 'member_code', 'question_code', 'question_answer', 'question_idx', 'question_score', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']

admin.site.register(QAnswerLog, QAnswerLogAdmin)


class QExampleInfoAdminForm(forms.ModelForm):

    class Meta:
        model = QExampleInfo
        fields = '__all__'


class QExampleInfoAdmin(admin.ModelAdmin):
    form = QExampleInfoAdminForm
    list_display = ['question_code', 'q_example', 'q_example_correct', 'q_example_idx', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'q_example_type']
    #readonly_fields = ['question_code', 'q_example', 'q_example_correct', 'q_example_idx', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'q_example_type']

admin.site.register(QExampleInfo, QExampleInfoAdmin)


class QuestionInfoAdminForm(forms.ModelForm):

    class Meta:
        model = QuestionInfo
        fields = '__all__'


class QuestionInfoAdmin(admin.ModelAdmin):
    form = QuestionInfoAdminForm
    list_display = ['subject_code', 'lecture_code', 'chapter_code', 'question_type', 'question', 'question_media_type', 'question_media_file', 'question_score', 'question_head', 'question_essay', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'question_media_file2', 'question_comment', 'question_level', 'teacher_contents', 'student_contents']
    #readonly_fields = ['subject_code', 'lecture_code', 'chapter_code', 'question_type', 'question', 'question_media_type', 'question_media_file', 'question_score', 'question_head', 'question_essay', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'question_media_file2', 'question_comment', 'question_level', 'teacher_contents', 'student_contents']

admin.site.register(QuestionInfo, QuestionInfoAdmin)


class QuizAnswerInfoAdminForm(forms.ModelForm):

    class Meta:
        model = QuizAnswerInfo
        fields = '__all__'


class QuizAnswerInfoAdmin(admin.ModelAdmin):
    form = QuizAnswerInfoAdminForm
    list_display = ['subject_code', 'lecture_code', 'chapter_code', 'member_code', 'quiz_code', 'quiz_type', 'quiz_answer', 'quiz_answer_idx', 'quiz_correct', 'quiz_score', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'test_type']
    #readonly_fields = ['subject_code', 'lecture_code', 'chapter_code', 'member_code', 'quiz_code', 'quiz_type', 'quiz_answer', 'quiz_answer_idx', 'quiz_correct', 'quiz_score', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'test_type']

admin.site.register(QuizAnswerInfo, QuizAnswerInfoAdmin)


class QuizExampleInfoAdminForm(forms.ModelForm):

    class Meta:
        model = QuizExampleInfo
        fields = '__all__'


class QuizExampleInfoAdmin(admin.ModelAdmin):
    form = QuizExampleInfoAdminForm
    list_display = ['quiz_code', 'quiz_example', 'quiz_example_correct', 'quiz_example_idx', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'quiz_example_type']
    #readonly_fields = ['quiz_code', 'quiz_example', 'quiz_example_correct', 'quiz_example_idx', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'quiz_example_type']

admin.site.register(QuizExampleInfo, QuizExampleInfoAdmin)


class QuizInfoAdminForm(forms.ModelForm):

    class Meta:
        model = QuizInfo
        fields = '__all__'


class QuizInfoAdmin(admin.ModelAdmin):
    form = QuizInfoAdminForm
    list_display = ['subject_code', 'lecture_code', 'chapter_code', 'quiz_type', 'quiz_question', 'quiz_media_type', 'quiz_media_file', 'quiz_score', 'quiz_comment', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'quiz_head', 'quiz_media_file2']
    #readonly_fields = ['subject_code', 'lecture_code', 'chapter_code', 'quiz_type', 'quiz_question', 'quiz_media_type', 'quiz_media_file', 'quiz_score', 'quiz_comment', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'quiz_head', 'quiz_media_file2']

admin.site.register(QuizInfo, QuizInfoAdmin)


class ScheduleInfoAdminForm(forms.ModelForm):

    class Meta:
        model = ScheduleInfo
        fields = '__all__'


class ScheduleInfoAdmin(admin.ModelAdmin):
    form = ScheduleInfoAdminForm
    list_display = ['member_code', 'title', 'content', 'start_date', 'start_time', 'end_date', 'end_time', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']
    #readonly_fields = ['member_code', 'title', 'content', 'start_date', 'start_time', 'end_date', 'end_time', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']

admin.site.register(ScheduleInfo, ScheduleInfoAdmin)


class TalkMemberAdminForm(forms.ModelForm):

    class Meta:
        model = TalkMember
        fields = '__all__'


class TalkMemberAdmin(admin.ModelAdmin):
    form = TalkMemberAdminForm
    list_display = ['member_code', 'use_flag']
    #readonly_fields = ['member_code', 'use_flag']

admin.site.register(TalkMember, TalkMemberAdmin)


class TalkMessageAdminForm(forms.ModelForm):

    class Meta:
        model = TalkMessage
        fields = '__all__'


class TalkMessageAdmin(admin.ModelAdmin):
    form = TalkMessageAdminForm
    list_display = ['talk_room_id', 'message', 'sender_member_code', 'send_date', 'send_time']
    #readonly_fields = ['talk_room_id', 'message', 'sender_member_code', 'send_date', 'send_time']

admin.site.register(TalkMessage, TalkMessageAdmin)


class TalkMessageReadAdminForm(forms.ModelForm):

    class Meta:
        model = TalkMessageRead
        fields = '__all__'


class TalkMessageReadAdmin(admin.ModelAdmin):
    form = TalkMessageReadAdminForm
    list_display = ['member_code', 'is_read']
    #readonly_fields = ['member_code', 'is_read']

admin.site.register(TalkMessageRead, TalkMessageReadAdmin)


class TalkRoomAdminForm(forms.ModelForm):

    class Meta:
        model = TalkRoom
        fields = '__all__'


class TalkRoomAdmin(admin.ModelAdmin):
    form = TalkRoomAdminForm
    list_display = ['talk_room_cate_code', 'lecture_code', 'inning_code', 'use_flag']
    #readonly_fields = ['talk_room_cate_code', 'lecture_code', 'inning_code', 'use_flag']

admin.site.register(TalkRoom, TalkRoomAdmin)


class TodoInfoAdminForm(forms.ModelForm):

    class Meta:
        model = TodoInfo
        fields = '__all__'


class TodoInfoAdmin(admin.ModelAdmin):
    form = TodoInfoAdminForm
    list_display = ['chapter_code', 'member_code', 'todo_comment', 'todo_status', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'teacher_code', 'todo_title', 'start_date', 'start_time', 'end_date', 'end_time', 'lecture_code']
    #readonly_fields = ['chapter_code', 'member_code', 'todo_comment', 'todo_status', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent', 'teacher_code', 'todo_title', 'start_date', 'start_time', 'end_date', 'end_time', 'lecture_code']

admin.site.register(TodoInfo, TodoInfoAdmin)


class TodoTInfoAdminForm(forms.ModelForm):

    class Meta:
        model = TodoTInfo
        fields = '__all__'


class TodoTInfoAdmin(admin.ModelAdmin):
    form = TodoTInfoAdminForm
    list_display = ['todo_code', 'member_code', 'todo_t_flag', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']
    #readonly_fields = ['todo_code', 'member_code', 'todo_t_flag', 'use_flag', 'reg_date', 'reg_time', 'reg_agent', 'udt_date', 'udt_time', 'udt_agent']

admin.site.register(TodoTInfo, TodoTInfoAdmin)


