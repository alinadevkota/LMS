from . import models

from rest_framework import serializers


# class ProfileSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = models.Profile
#         fields = (
#             'pk',
#         )


class CenterInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CenterInfo
        fields = (
            'pk','Center_Name', 'Center_Address', 'Use_Flag', 'Register_DateTime', 'Register_Agent'
        )


class MemberInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MemberInfo
        fields = (
            'pk','username','first_name','last_name','email','password', 'Member_ID', 'Member_Permanent_Address',
                    'Member_Temporary_Address', 'Member_BirthDate', 'Member_Phone', 'Member_Avatar',
                    'Member_Gender', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent',
                    'Member_Memo','Is_Teacher','Is_Student','Is_CenterAdmin','Is_Parent','Member_Avatar', 'Center_Code'
        )



class LectureInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LectureInfo
        fields = (
            'pk','Lecture_Name', 'Lecture_Description', 'Lecture_Cover_File', 'Lecture_Level',
                    'Lecture_Info', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent',
                    'Lecture_Provider', 'Center_Code'
        )


class ChapterInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ChapterInfo
        fields = (
            'pk','Chapter_No', 'Chapter_Name', 'Summary', 'Page_Num', 'Use_Flag',
                    'Register_DateTime', 'Updated_DateTime', 'Register_Agent', 'Lecture_Code'
        )


class ChapterContentsInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ChapterContentsInfo
        fields = (
            'pk','Chapter_Code', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
                    'Register_Agent', 'Content_Description'
        )


class ChapterMissonCheckCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ChapterMissonCheckCard
        fields = (
            'pk','check_card_code', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent'
        )


class ChapterMissonCheckItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ChapterMissonCheckItem
        fields = (
            'pk','check_item_code', 'item_text', 'contents_text', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime', 'Register_Agent'
        )


class InningInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InningInfo
        fields = (
            'pk','Inning_Name', 'Start_Date', 'End_Date', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime',
                    'Register_Agent', 'Center_Code'
        )


class OmrQuestionInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OmrQuestionInfo
        fields = (
            'pk','Homework_Code', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
            'Register_Agent',
            'Question_Level', 'Question_Score', 'Question_Description'
        )


class QuizInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.QuizInfo
        fields = (
            'pk','subject_code', 'quiz_type', 'quiz_question', 'quiz_media_type', 'quiz_media_file', 'quiz_score',
                    'quiz_comment', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent', 'quiz_head',
                    'quiz_media_file2'
        )


class AssignHomeworkInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AssignHomeworkInfo
        fields = (
            'pk','Homework_Code', 'Inning_Code', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime', 'Register_Agent'
        )


class AssignQuestionInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AssignQuestionInfo
        fields = (
            'pk','subject_code', 'question_type', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
            'Register_Agent'
        )


class BoardInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BoardInfo
        fields = (
            'pk','board_name', 'board_write_level', 'board_read_level', 'board_reply_level', 'board_new_time',
                    'board_create_time', 'admin_id', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
                    'Register_Agent'
        )


class BoardContentInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BoardContentInfo
        fields = (
            'pk','admin_id', 'title', 'contents', 'writer', 'view_cnt', 'ref_code', 'ref_step', 'ref_level',
                    'write_time', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent'
        )


class InningGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InningGroup
        fields = (
            'pk','Teacher_Code', 'Inning_Code', 'Lecture_Code', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime', 'Register_Agent'
        )


class ChapterContentMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ChapterContentMedia
        fields = (
            'pk','media_type', 'media_desc', 'media_filename', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
                    'Register_Agent'
        )


class ChapterImgInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ChapterImgInfo
        fields = (
            'pk','filename', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent'
        )


class ChapterMissonCheckSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ChapterMissonCheck
        fields = (
            'pk','check_code', 'student_code', 'check_agent_code', 'is_check_yn', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime', 'Register_Agent'
        )


class ChapterWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ChapterWrite
        fields = (
            'pk','student_code', 'write_content', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
                    'Register_Agent'
        )


class GroupMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GroupMapping
        fields = (
            'pk','Inning_Code', 'Student_Code', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
                    'Register_Agent'
        )


class HomeworkInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.HomeworkInfo
        fields = (
            'pk','Chapter_Code', 'Homework_Topic', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
                    'Register_Agent'
        )


class LearningNoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LearningNote
        fields = (
            'pk','contents_code', 'note_contents', 'note_attachment'
        )


class LectureUbtInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LectureUbtInfo
        fields = (
            'pk','Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent'
        )


class LessonInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LessonInfo
        fields = (
            'pk','teacher_code', 'start_date', 'end_date', 'progress', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime', 'Register_Agent', 'ubt_start', 'ubt_end', 'download_count', 'download_date'
        )


class LessonLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LessonLog
        fields = (
            'pk', 
            'member_id', 'member_ip', 'member_browser', 'member_os', 'start_date', 'start_time', 'end_date',
                    'end_time', 'connect_date', 'connect_time', 'connect_count', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime', 'Register_Agent', 'study_time', 'connect_page'
        )


class MemberGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MemberGroup
        fields = (
            'pk', 
            'group_name', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent'
        )


class MessageInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MessageInfo
        fields = (
            'pk', 
            'teacher_code', 'message', 'message_read', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
                    'Register_Agent'
        )


class OmrAnswerInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OmrAnswerInfo
        fields = (
            'pk', 
            'Answer_Description', 'Student_Code', 'Question_Code', 'Answer_Score', 'Use_Flag',
                    'Register_DateTime', 'Updated_DateTime'
        )


class OmrAssignInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OmrAssignInfo
        fields = (
            'pk', 
            'subject_code', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent'
        )


class OmrExampleInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OmrExampleInfo
        fields = (
            'pk', 
            'omr_example_correct', 'omr_example_idx', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
                    'Register_Agent'
        )


class QAnswerInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.QAnswerInfo
        fields = (
            'pk', 
            'subject_code', 'question_type', 'question_answer', 'question_idx', 'question_correct',
                    'question_score', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent'
        )


class QAnswerLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.QAnswerLog
        fields = (
            'pk', 
            'question_answer', 'question_idx', 'question_score', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime', 'Register_Agent'
        )


class QExampleInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.QExampleInfo
        fields = (
            'pk', 
            'q_example', 'q_example_correct', 'q_example_idx', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime', 'Register_Agent', 'q_example_type'
        )


class QuestionInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.QuestionInfo
        fields = (
            'pk', 
            'subject_code', 'question_type', 'question', 'question_media_type', 'question_media_file',
                    'question_score', 'question_head', 'question_essay', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime', 'Register_Agent', 'question_media_file2', 'question_comment', 'question_level',
                    'teacher_contents', 'student_contents'
        )


class QuizAnswerInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.QuizAnswerInfo
        fields = (
            'pk', 
            'subject_code', 'quiz_type', 'quiz_answer', 'quiz_answer_idx', 'quiz_correct', 'quiz_score',
                    'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent', 'test_type'
        )


class QuizExampleInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.QuizExampleInfo
        fields = (
            'pk', 
            'quiz_example', 'quiz_example_correct', 'quiz_example_idx', 'Use_Flag', 'Register_DateTime',
                    'Updated_DateTime', 'Register_Agent', 'quiz_example_type'
        )


class ScheduleInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ScheduleInfo
        fields = (
            'pk', 
            'title', 'content', 'start_date', 'start_time', 'end_date', 'end_time', 'Use_Flag',
                    'Register_DateTime', 'Updated_DateTime', 'Register_Agent'
        )


class TalkMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TalkMember
        fields = (
            'pk', 'Use_Flag'
        )


class TalkRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TalkRoom
        fields = (
            'pk',
            'talk_room_cate_code', 'use_flag'
        )


class TalkMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TalkMessage
        fields = (
            'pk', 
            'message', 'sender_member_code', 'send_date', 'send_time'
        )


class TalkMessageReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TalkMessageRead
        fields = (
            'pk', 
            'is_read', 
        )


class TodoInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TodoInfo
        fields = (
            'pk', 
            'todo_comment', 'todo_status', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime',
                    'Register_Agent', 'teacher_code', 'todo_title', 'start_date', 'start_time', 'end_date', 'end_time'
        )


class TodoTInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TodoTInfo
        fields = (
            'pk', 
            'todo_code', 'todo_t_flag', 'Use_Flag', 'Register_DateTime', 'Updated_DateTime', 'Register_Agent'
        )


