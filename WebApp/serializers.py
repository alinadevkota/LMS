from rest_framework import serializers

from . import models


class AssignHomeworkInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AssignHomeworkInfo
        fields = (
            'pk',
            'question_code',
            'subject_code',
            'lecture_code',
            'chapter_code',
            'member_code',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
        )


class AssignQuestionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AssignQuestionInfo
        fields = (
            'pk',
            'question_code',
            'subject_code',
            'lecture_code',
            'chapter_code',
            'question_type',
            'use_flag',
            'reg_date',
            'reg_time',
            'udt_date',
            'udt_time',
            'udt_agent',
        )


class BoardContentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BoardContentInfo
        fields = (
            'pk',
            'board_code',
            'admin_id',
            'title',
            'contents',
            'writer',
            'view_cnt',
            'ref_code',
            'ref_step',
            'ref_level',
            'write_time',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
        )


class BoardInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BoardInfo
        fields = (
            'pk',
            'board_name',
            'board_write_level',
            'board_read_level',
            'board_reply_level',
            'board_new_time',
            'board_create_time',
            'admin_id',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
        )


class CenterInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CenterInfo
        fields = (
            'pk',
            'center_name',
            'center_location',
            'center_tel',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
        )


class ChapterContentMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChapterContentMedia
        fields = (
            'pk',
            'chapter_contents_code',
            'media_type',
            'media_desc',
            'media_filename',
            'use_flag',
            'reg_date',
            'reg_time',
            'udt_date',
            'udt_time',
            'reg_agent',
            'udt_agent',
        )


class ChapterContentsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChapterContentsInfo
        fields = (
            'pk',
            'chapter_code',
            'chapter_contents',
            'chapter_audio',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
            'contents_index',
            'chapter_type',
            'thum_file',
            'vod_file',
            'today',
            'front1_img',
            'front1_text',
            'back1_img',
            'back1_text',
            'pdf_file',
            'front2_img',
            'front3_img',
            'front4_img',
            'front2_text',
            'front3_text',
            'front4_text',
            'back2_img',
            'back3_img',
            'back4_img',
            'back2_text',
            'back3_text',
            'back4_text',
            'c1_audio',
            'c2_audio',
            'c3_audio',
            'c4_audio',
            'vod_size',
            'offline_file',
            'teacher_guide',
            'today_text',
            'contents_text',
            'pbl_allow',
            'pbl_lec_allow',
        )


class ChapterImgInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChapterImgInfo
        fields = (
            'pk',
            'chapter_code',
            'filename',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
        )


class ChapterInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChapterInfo
        fields = (
            'pk',
            'lecture_code',
            'chapter_no',
            'chapter_name',
            'topic',
            'summary',
            'page_num',
            'vod_size',
            'intro',
            'target',
            'top_img',
            'bottom_img1',
            'bottom_img2',
            'bottom_img3',
            'thum_file',
            'vod_file',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
            'today',
            'chapter_type',
            'prologue_type',
            'tabset',
            'chapter_image',
            'chapter_use',
            'offline_file',
            'pre_test_type',
            'post_test_type',
            'level1_avg',
            'level2_avg',
            'level3_avg',
            'level1_hard_avg',
            'level1_medium_avg',
            'level1_easy_avg',
            'level2_hard_avg',
            'level2_medium_avg',
            'level2_easy_avg',
            'level3_hard_avg',
            'level3_medium_avg',
            'level3_easy_avg',
            'homework_count',
            'epilogue_type',
            'epilogue_img',
            'pbl_flag',
            'chapter_use_time',
        )


class ChapterMissonCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChapterMissonCheck
        fields = (
            'pk',
            'check_code',
            'check_item_code',
            'student_code',
            'check_agent_code',
            'is_check_yn',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
            'inning_code',
        )


class ChapterMissonCheckCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChapterMissonCheckCard
        fields = (
            'pk',
            'check_card_code',
            'chapter_code',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
        )


class ChapterMissonCheckItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChapterMissonCheckItem
        fields = (
            'pk',
            'check_item_code',
            'check_card_code',
            'item_text',
            'contents_text',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
            'chapter_contents_code',
        )


class ChapterWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChapterWrite
        fields = (
            'pk',
            'inning_code',
            'chapter_contents_code',
            'student_code',
            'write_content',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
        )


class GroupMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GroupMapping
        fields = (
            'pk',
            'center_code',
            'group_code',
            'member_code',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
        )


class HomeworkInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HomeworkInfo
        fields = (
            'pk',
            'question_code',
            'subject_code',
            'lecture_code',
            'chapter_code',
            'level_score',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'level',
        )


class InningGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InningGroup
        fields = (
            'pk',
            'center_code',
            'inning_code',
            'lecture_code',
            'teacher_code',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
        )


class InningInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InningInfo
        fields = (
            'pk',
            'inning_name',
            'lecture_code',
            'start_date',
            'end_date',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
            'center_code',
        )


class LearningNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LearningNote
        fields = (
            'pk',
            'inning_code',
            'lecture_code',
            'chapter_code',
            'contents_code',
            'note_contents',
            'note_attachment',
        )


class LectureInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LectureInfo
        fields = (
            'pk',
            'lecture_name',
            'lecture_teacher',
            'lecture_cover',
            'lecture_cover_file',
            'lecture_level',
            'lecture_info',
            'teacher',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
            'lecture_certification',
            'lecture_provider',
            'cert_crit_prog',
            'cert_crit_post',
            'cert_crit_ubt',
            'cert_crit_issue',
            'center_code',
        )


class LectureUbtInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LectureUbtInfo
        fields = (
            'pk',
            'quiz_code',
            'lecture_code',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
        )


class LessonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LessonInfo
        fields = (
            'pk',
            'lecture_code',
            'member_code',
            'teacher_code',
            'start_date',
            'end_date',
            'progress',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
            'ubt_start',
            'ubt_end',
            'download_count',
            'download_date',
            'center_code',
            'inning_code',
        )


class LessonLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LessonLog
        fields = (
            'pk',
            'lesson_code',
            'lecture_code',
            'chapter_code',
            'member_code',
            'member_id',
            'member_ip',
            'member_browser',
            'member_os',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            'connect_date',
            'connect_time',
            'connect_count',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
            'study_time',
            'connect_page',
        )


class MemberGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MemberGroup
        fields = (
            'pk',
            'center_code',
            'group_name',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
        )


class MemberInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MemberInfo
        fields = (
            'pk',
            'member_id',
            'member_level',
            'member_pw',
            'member_name',
            'member_jumin',
            'member_birth',
            'member_college',
            'member_email',
            'member_phone',
            'member_post',
            'member_addr1',
            'member_addr2',
            'member_file',
            'member_gender',
            'member_major',
            'member_nation',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
            'center_code',
            'member_fax',
            'member_memo',
        )


class MessageInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MessageInfo
        fields = (
            'pk',
            'teacher_code',
            'member_code',
            'message',
            'message_read',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
        )


class OmrAnswerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OmrAnswerInfo
        fields = (
            'pk',
            'subject_code',
            'lecture_code',
            'chapter_code',
            'member_code',
            'question_code',
            'omr_answer',
            'omr_answer_idx',
            'omr_answer_correct',
            'question_score',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
            'lesson_code',
        )


class OmrAssignInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OmrAssignInfo
        fields = (
            'pk',
            'question_code',
            'subject_code',
            'lecture_code',
            'chapter_code',
            'member_code',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
        )


class OmrExampleInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OmrExampleInfo
        fields = (
            'pk',
            'question_code',
            'omr_example_correct',
            'omr_example_idx',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
        )


class OmrQuestionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OmrQuestionInfo
        fields = (
            'pk',
            'subject_code',
            'lecture_code',
            'chapter_code',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
            'question_level',
            'question_score',
        )


class QAnswerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QAnswerInfo
        fields = (
            'pk',
            'subject_code',
            'lecture_code',
            'chapter_code',
            'member_code',
            'question_code',
            'question_type',
            'question_answer',
            'question_idx',
            'question_correct',
            'question_score',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
            'lesson_code',
        )


class QAnswerLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QAnswerLog
        fields = (
            'pk',
            'lecture_code',
            'member_code',
            'question_code',
            'question_answer',
            'question_idx',
            'question_score',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
        )


class QExampleInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QExampleInfo
        fields = (
            'pk',
            'question_code',
            'q_example',
            'q_example_correct',
            'q_example_idx',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
            'q_example_type',
        )


class QuestionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionInfo
        fields = (
            'pk',
            'subject_code',
            'lecture_code',
            'chapter_code',
            'question_type',
            'question',
            'question_media_type',
            'question_media_file',
            'question_score',
            'question_head',
            'question_essay',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
            'question_media_file2',
            'question_comment',
            'question_level',
            'teacher_contents',
            'student_contents',
        )


class QuizAnswerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuizAnswerInfo
        fields = (
            'pk',
            'subject_code',
            'lecture_code',
            'chapter_code',
            'member_code',
            'quiz_code',
            'quiz_type',
            'quiz_answer',
            'quiz_answer_idx',
            'quiz_correct',
            'quiz_score',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
            'test_type',
        )


class QuizExampleInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuizExampleInfo
        fields = (
            'pk',
            'quiz_code',
            'quiz_example',
            'quiz_example_correct',
            'quiz_example_idx',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
            'quiz_example_type',
        )


class QuizInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuizInfo
        fields = (
            'pk',
            'subject_code',
            'lecture_code',
            'chapter_code',
            'quiz_type',
            'quiz_question',
            'quiz_media_type',
            'quiz_media_file',
            'quiz_score',
            'quiz_comment',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
            'quiz_head',
            'quiz_media_file2',
        )


class ScheduleInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ScheduleInfo
        fields = (
            'pk',
            'member_code',
            'title',
            'content',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
        )


class TalkMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TalkMember
        fields = (
            'pk',
            'member_code',
            'use_flag',
        )


class TalkMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TalkMessage
        fields = (
            'pk',
            'talk_room_id',
            'message',
            'sender_member_code',
            'send_date',
            'send_time',
        )


class TalkMessageReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TalkMessageRead
        fields = (
            'pk',
            'member_code',
            'is_read',
        )


class TalkRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TalkRoom
        fields = (
            'pk',
            'talk_room_cate_code',
            'lecture_code',
            'inning_code',
            'use_flag',
        )


class TodoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TodoInfo
        fields = (
            'pk',
            'chapter_code',
            'member_code',
            'todo_comment',
            'todo_status',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
            'teacher_code',
            'todo_title',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            'lecture_code',
        )


class TodoTInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TodoTInfo
        fields = (
            'pk',
            'todo_code',
            'member_code',
            'todo_t_flag',
            'use_flag',
            'reg_date',
            'reg_time',
            'reg_agent',
            'udt_date',
            'udt_time',
            'udt_agent',
        )
