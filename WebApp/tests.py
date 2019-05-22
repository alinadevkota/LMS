import unittest
from django.urls import reverse
from django.test import Client
from .models import AssignHomeworkInfo, AssignQuestionInfo, BoardContentInfo, BoardInfo, CenterInfo, ChapterContentMedia, ChapterContentsInfo, ChapterImgInfo, ChapterInfo, ChapterMissonCheck, ChapterMissonCheckCard, ChapterMissonCheckItem, ChapterWrite, GroupMapping, HomeworkInfo, InningGroup, InningInfo, LearningNote, LectureInfo, LectureUbtInfo, LessonInfo, LessonLog, MemberGroup, MemberInfo, MessageInfo, OmrAnswerInfo, OmrAssignInfo, OmrExampleInfo, OmrQuestionInfo, QAnswerInfo, QAnswerLog, QExampleInfo, QuestionInfo, QuizAnswerInfo, QuizExampleInfo, QuizInfo, ScheduleInfo, TalkMember, TalkMessage, TalkMessageRead, TalkRoom, TodoInfo, TodoTInfo
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_assignhomeworkinfo(**kwargs):
    defaults = {}
    defaults["question_code"] = "question_code"
    defaults["subject_code"] = "subject_code"
    defaults["lecture_code"] = "lecture_code"
    defaults["chapter_code"] = "chapter_code"
    defaults["member_code"] = "member_code"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return AssignHomeworkInfo.objects.create(**defaults)


def create_assignquestioninfo(**kwargs):
    defaults = {}
    defaults["question_code"] = "question_code"
    defaults["subject_code"] = "subject_code"
    defaults["lecture_code"] = "lecture_code"
    defaults["chapter_code"] = "chapter_code"
    defaults["question_type"] = "question_type"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return AssignQuestionInfo.objects.create(**defaults)


def create_boardcontentinfo(**kwargs):
    defaults = {}
    defaults["board_code"] = "board_code"
    defaults["admin_id"] = "admin_id"
    defaults["title"] = "title"
    defaults["contents"] = "contents"
    defaults["writer"] = "writer"
    defaults["view_cnt"] = "view_cnt"
    defaults["ref_code"] = "ref_code"
    defaults["ref_step"] = "ref_step"
    defaults["ref_level"] = "ref_level"
    defaults["write_time"] = "write_time"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return BoardContentInfo.objects.create(**defaults)


def create_boardinfo(**kwargs):
    defaults = {}
    defaults["board_name"] = "board_name"
    defaults["board_write_level"] = "board_write_level"
    defaults["board_read_level"] = "board_read_level"
    defaults["board_reply_level"] = "board_reply_level"
    defaults["board_new_time"] = "board_new_time"
    defaults["board_create_time"] = "board_create_time"
    defaults["admin_id"] = "admin_id"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return BoardInfo.objects.create(**defaults)


def create_centerinfo(**kwargs):
    defaults = {}
    defaults["center_name"] = "center_name"
    defaults["center_location"] = "center_location"
    defaults["center_tel"] = "center_tel"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return CenterInfo.objects.create(**defaults)


def create_chaptercontentmedia(**kwargs):
    defaults = {}
    defaults["chapter_contents_code"] = "chapter_contents_code"
    defaults["media_type"] = "media_type"
    defaults["media_desc"] = "media_desc"
    defaults["media_filename"] = "media_filename"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return ChapterContentMedia.objects.create(**defaults)


def create_chaptercontentsinfo(**kwargs):
    defaults = {}
    defaults["chapter_code"] = "chapter_code"
    defaults["chapter_contents"] = "chapter_contents"
    defaults["chapter_audio"] = "chapter_audio"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults["contents_index"] = "contents_index"
    defaults["chapter_type"] = "chapter_type"
    defaults["thum_file"] = "thum_file"
    defaults["vod_file"] = "vod_file"
    defaults["today"] = "today"
    defaults["front1_img"] = "front1_img"
    defaults["front1_text"] = "front1_text"
    defaults["back1_img"] = "back1_img"
    defaults["back1_text"] = "back1_text"
    defaults["pdf_file"] = "pdf_file"
    defaults["front2_img"] = "front2_img"
    defaults["front3_img"] = "front3_img"
    defaults["front4_img"] = "front4_img"
    defaults["front2_text"] = "front2_text"
    defaults["front3_text"] = "front3_text"
    defaults["front4_text"] = "front4_text"
    defaults["back2_img"] = "back2_img"
    defaults["back3_img"] = "back3_img"
    defaults["back4_img"] = "back4_img"
    defaults["back2_text"] = "back2_text"
    defaults["back3_text"] = "back3_text"
    defaults["back4_text"] = "back4_text"
    defaults["c1_audio"] = "c1_audio"
    defaults["c2_audio"] = "c2_audio"
    defaults["c3_audio"] = "c3_audio"
    defaults["c4_audio"] = "c4_audio"
    defaults["vod_size"] = "vod_size"
    defaults["offline_file"] = "offline_file"
    defaults["teacher_guide"] = "teacher_guide"
    defaults["today_text"] = "today_text"
    defaults["contents_text"] = "contents_text"
    defaults["pbl_allow"] = "pbl_allow"
    defaults["pbl_lec_allow"] = "pbl_lec_allow"
    defaults.update(**kwargs)
    return ChapterContentsInfo.objects.create(**defaults)


def create_chapterimginfo(**kwargs):
    defaults = {}
    defaults["chapter_code"] = "chapter_code"
    defaults["filename"] = "filename"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return ChapterImgInfo.objects.create(**defaults)


def create_chapterinfo(**kwargs):
    defaults = {}
    defaults["lecture_code"] = "lecture_code"
    defaults["chapter_no"] = "chapter_no"
    defaults["chapter_name"] = "chapter_name"
    defaults["topic"] = "topic"
    defaults["summary"] = "summary"
    defaults["page_num"] = "page_num"
    defaults["vod_size"] = "vod_size"
    defaults["intro"] = "intro"
    defaults["target"] = "target"
    defaults["top_img"] = "top_img"
    defaults["bottom_img1"] = "bottom_img1"
    defaults["bottom_img2"] = "bottom_img2"
    defaults["bottom_img3"] = "bottom_img3"
    defaults["thum_file"] = "thum_file"
    defaults["vod_file"] = "vod_file"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults["today"] = "today"
    defaults["chapter_type"] = "chapter_type"
    defaults["prologue_type"] = "prologue_type"
    defaults["tabset"] = "tabset"
    defaults["chapter_image"] = "chapter_image"
    defaults["chapter_use"] = "chapter_use"
    defaults["offline_file"] = "offline_file"
    defaults["pre_test_type"] = "pre_test_type"
    defaults["post_test_type"] = "post_test_type"
    defaults["level1_avg"] = "level1_avg"
    defaults["level2_avg"] = "level2_avg"
    defaults["level3_avg"] = "level3_avg"
    defaults["level1_hard_avg"] = "level1_hard_avg"
    defaults["level1_medium_avg"] = "level1_medium_avg"
    defaults["level1_easy_avg"] = "level1_easy_avg"
    defaults["level2_hard_avg"] = "level2_hard_avg"
    defaults["level2_medium_avg"] = "level2_medium_avg"
    defaults["level2_easy_avg"] = "level2_easy_avg"
    defaults["level3_hard_avg"] = "level3_hard_avg"
    defaults["level3_medium_avg"] = "level3_medium_avg"
    defaults["level3_easy_avg"] = "level3_easy_avg"
    defaults["homework_count"] = "homework_count"
    defaults["epilogue_type"] = "epilogue_type"
    defaults["epilogue_img"] = "epilogue_img"
    defaults["pbl_flag"] = "pbl_flag"
    defaults["chapter_use_time"] = "chapter_use_time"
    defaults.update(**kwargs)
    return ChapterInfo.objects.create(**defaults)


def create_chaptermissoncheck(**kwargs):
    defaults = {}
    defaults["check_code"] = "check_code"
    defaults["check_item_code"] = "check_item_code"
    defaults["student_code"] = "student_code"
    defaults["check_agent_code"] = "check_agent_code"
    defaults["is_check_yn"] = "is_check_yn"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults["inning_code"] = "inning_code"
    defaults.update(**kwargs)
    return ChapterMissonCheck.objects.create(**defaults)


def create_chaptermissoncheckcard(**kwargs):
    defaults = {}
    defaults["check_card_code"] = "check_card_code"
    defaults["chapter_code"] = "chapter_code"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return ChapterMissonCheckCard.objects.create(**defaults)


def create_chaptermissoncheckitem(**kwargs):
    defaults = {}
    defaults["check_item_code"] = "check_item_code"
    defaults["check_card_code"] = "check_card_code"
    defaults["item_text"] = "item_text"
    defaults["contents_text"] = "contents_text"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults["chapter_contents_code"] = "chapter_contents_code"
    defaults.update(**kwargs)
    return ChapterMissonCheckItem.objects.create(**defaults)


def create_chapterwrite(**kwargs):
    defaults = {}
    defaults["inning_code"] = "inning_code"
    defaults["chapter_contents_code"] = "chapter_contents_code"
    defaults["student_code"] = "student_code"
    defaults["write_content"] = "write_content"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return ChapterWrite.objects.create(**defaults)


def create_groupmapping(**kwargs):
    defaults = {}
    defaults["center_code"] = "center_code"
    defaults["group_code"] = "group_code"
    defaults["member_code"] = "member_code"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return GroupMapping.objects.create(**defaults)


def create_homeworkinfo(**kwargs):
    defaults = {}
    defaults["question_code"] = "question_code"
    defaults["subject_code"] = "subject_code"
    defaults["lecture_code"] = "lecture_code"
    defaults["chapter_code"] = "chapter_code"
    defaults["level_score"] = "level_score"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["level"] = "level"
    defaults.update(**kwargs)
    return HomeworkInfo.objects.create(**defaults)


def create_inninggroup(**kwargs):
    defaults = {}
    defaults["center_code"] = "center_code"
    defaults["inning_code"] = "inning_code"
    defaults["lecture_code"] = "lecture_code"
    defaults["teacher_code"] = "teacher_code"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return InningGroup.objects.create(**defaults)


def create_inninginfo(**kwargs):
    defaults = {}
    defaults["inning_name"] = "inning_name"
    defaults["lecture_code"] = "lecture_code"
    defaults["start_date"] = "start_date"
    defaults["end_date"] = "end_date"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults["center_code"] = "center_code"
    defaults.update(**kwargs)
    return InningInfo.objects.create(**defaults)


def create_learningnote(**kwargs):
    defaults = {}
    defaults["inning_code"] = "inning_code"
    defaults["lecture_code"] = "lecture_code"
    defaults["chapter_code"] = "chapter_code"
    defaults["contents_code"] = "contents_code"
    defaults["note_contents"] = "note_contents"
    defaults["note_attachment"] = "note_attachment"
    defaults.update(**kwargs)
    return LearningNote.objects.create(**defaults)


def create_lectureinfo(**kwargs):
    defaults = {}
    defaults["lecture_name"] = "lecture_name"
    defaults["lecture_teacher"] = "lecture_teacher"
    defaults["lecture_cover"] = "lecture_cover"
    defaults["lecture_cover_file"] = "lecture_cover_file"
    defaults["lecture_level"] = "lecture_level"
    defaults["lecture_info"] = "lecture_info"
    defaults["teacher"] = "teacher"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults["lecture_certification"] = "lecture_certification"
    defaults["lecture_provider"] = "lecture_provider"
    defaults["cert_crit_prog"] = "cert_crit_prog"
    defaults["cert_crit_post"] = "cert_crit_post"
    defaults["cert_crit_ubt"] = "cert_crit_ubt"
    defaults["cert_crit_issue"] = "cert_crit_issue"
    defaults["center_code"] = "center_code"
    defaults.update(**kwargs)
    return LectureInfo.objects.create(**defaults)


def create_lectureubtinfo(**kwargs):
    defaults = {}
    defaults["quiz_code"] = "quiz_code"
    defaults["lecture_code"] = "lecture_code"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return LectureUbtInfo.objects.create(**defaults)


def create_lessoninfo(**kwargs):
    defaults = {}
    defaults["lecture_code"] = "lecture_code"
    defaults["member_code"] = "member_code"
    defaults["teacher_code"] = "teacher_code"
    defaults["start_date"] = "start_date"
    defaults["end_date"] = "end_date"
    defaults["progress"] = "progress"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults["ubt_start"] = "ubt_start"
    defaults["ubt_end"] = "ubt_end"
    defaults["download_count"] = "download_count"
    defaults["download_date"] = "download_date"
    defaults["center_code"] = "center_code"
    defaults["inning_code"] = "inning_code"
    defaults.update(**kwargs)
    return LessonInfo.objects.create(**defaults)


def create_lessonlog(**kwargs):
    defaults = {}
    defaults["lesson_code"] = "lesson_code"
    defaults["lecture_code"] = "lecture_code"
    defaults["chapter_code"] = "chapter_code"
    defaults["member_code"] = "member_code"
    defaults["member_id"] = "member_id"
    defaults["member_ip"] = "member_ip"
    defaults["member_browser"] = "member_browser"
    defaults["member_os"] = "member_os"
    defaults["start_date"] = "start_date"
    defaults["start_time"] = "start_time"
    defaults["end_date"] = "end_date"
    defaults["end_time"] = "end_time"
    defaults["connect_date"] = "connect_date"
    defaults["connect_time"] = "connect_time"
    defaults["connect_count"] = "connect_count"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults["study_time"] = "study_time"
    defaults["connect_page"] = "connect_page"
    defaults.update(**kwargs)
    return LessonLog.objects.create(**defaults)


def create_membergroup(**kwargs):
    defaults = {}
    defaults["center_code"] = "center_code"
    defaults["group_name"] = "group_name"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return MemberGroup.objects.create(**defaults)


def create_memberinfo(**kwargs):
    defaults = {}
    defaults["member_id"] = "member_id"
    defaults["member_level"] = "member_level"
    defaults["member_pw"] = "member_pw"
    defaults["member_name"] = "member_name"
    defaults["member_jumin"] = "member_jumin"
    defaults["member_birth"] = "member_birth"
    defaults["member_college"] = "member_college"
    defaults["member_email"] = "member_email"
    defaults["member_phone"] = "member_phone"
    defaults["member_post"] = "member_post"
    defaults["member_addr1"] = "member_addr1"
    defaults["member_addr2"] = "member_addr2"
    defaults["member_file"] = "member_file"
    defaults["member_gender"] = "member_gender"
    defaults["member_major"] = "member_major"
    defaults["member_nation"] = "member_nation"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults["center_code"] = "center_code"
    defaults["member_fax"] = "member_fax"
    defaults["member_memo"] = "member_memo"
    defaults.update(**kwargs)
    return MemberInfo.objects.create(**defaults)


def create_messageinfo(**kwargs):
    defaults = {}
    defaults["teacher_code"] = "teacher_code"
    defaults["member_code"] = "member_code"
    defaults["message"] = "message"
    defaults["message_read"] = "message_read"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return MessageInfo.objects.create(**defaults)


def create_omranswerinfo(**kwargs):
    defaults = {}
    defaults["subject_code"] = "subject_code"
    defaults["lecture_code"] = "lecture_code"
    defaults["chapter_code"] = "chapter_code"
    defaults["member_code"] = "member_code"
    defaults["question_code"] = "question_code"
    defaults["omr_answer"] = "omr_answer"
    defaults["omr_answer_idx"] = "omr_answer_idx"
    defaults["omr_answer_correct"] = "omr_answer_correct"
    defaults["question_score"] = "question_score"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults["lesson_code"] = "lesson_code"
    defaults.update(**kwargs)
    return OmrAnswerInfo.objects.create(**defaults)


def create_omrassigninfo(**kwargs):
    defaults = {}
    defaults["question_code"] = "question_code"
    defaults["subject_code"] = "subject_code"
    defaults["lecture_code"] = "lecture_code"
    defaults["chapter_code"] = "chapter_code"
    defaults["member_code"] = "member_code"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return OmrAssignInfo.objects.create(**defaults)


def create_omrexampleinfo(**kwargs):
    defaults = {}
    defaults["question_code"] = "question_code"
    defaults["omr_example_correct"] = "omr_example_correct"
    defaults["omr_example_idx"] = "omr_example_idx"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return OmrExampleInfo.objects.create(**defaults)


def create_omrquestioninfo(**kwargs):
    defaults = {}
    defaults["subject_code"] = "subject_code"
    defaults["lecture_code"] = "lecture_code"
    defaults["chapter_code"] = "chapter_code"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults["question_level"] = "question_level"
    defaults["question_score"] = "question_score"
    defaults.update(**kwargs)
    return OmrQuestionInfo.objects.create(**defaults)


def create_qanswerinfo(**kwargs):
    defaults = {}
    defaults["subject_code"] = "subject_code"
    defaults["lecture_code"] = "lecture_code"
    defaults["chapter_code"] = "chapter_code"
    defaults["member_code"] = "member_code"
    defaults["question_code"] = "question_code"
    defaults["question_type"] = "question_type"
    defaults["question_answer"] = "question_answer"
    defaults["question_idx"] = "question_idx"
    defaults["question_correct"] = "question_correct"
    defaults["question_score"] = "question_score"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults["lesson_code"] = "lesson_code"
    defaults.update(**kwargs)
    return QAnswerInfo.objects.create(**defaults)


def create_qanswerlog(**kwargs):
    defaults = {}
    defaults["lecture_code"] = "lecture_code"
    defaults["member_code"] = "member_code"
    defaults["question_code"] = "question_code"
    defaults["question_answer"] = "question_answer"
    defaults["question_idx"] = "question_idx"
    defaults["question_score"] = "question_score"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return QAnswerLog.objects.create(**defaults)


def create_qexampleinfo(**kwargs):
    defaults = {}
    defaults["question_code"] = "question_code"
    defaults["q_example"] = "q_example"
    defaults["q_example_correct"] = "q_example_correct"
    defaults["q_example_idx"] = "q_example_idx"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults["q_example_type"] = "q_example_type"
    defaults.update(**kwargs)
    return QExampleInfo.objects.create(**defaults)


def create_questioninfo(**kwargs):
    defaults = {}
    defaults["subject_code"] = "subject_code"
    defaults["lecture_code"] = "lecture_code"
    defaults["chapter_code"] = "chapter_code"
    defaults["question_type"] = "question_type"
    defaults["question"] = "question"
    defaults["question_media_type"] = "question_media_type"
    defaults["question_media_file"] = "question_media_file"
    defaults["question_score"] = "question_score"
    defaults["question_head"] = "question_head"
    defaults["question_essay"] = "question_essay"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults["question_media_file2"] = "question_media_file2"
    defaults["question_comment"] = "question_comment"
    defaults["question_level"] = "question_level"
    defaults["teacher_contents"] = "teacher_contents"
    defaults["student_contents"] = "student_contents"
    defaults.update(**kwargs)
    return QuestionInfo.objects.create(**defaults)


def create_quizanswerinfo(**kwargs):
    defaults = {}
    defaults["subject_code"] = "subject_code"
    defaults["lecture_code"] = "lecture_code"
    defaults["chapter_code"] = "chapter_code"
    defaults["member_code"] = "member_code"
    defaults["quiz_code"] = "quiz_code"
    defaults["quiz_type"] = "quiz_type"
    defaults["quiz_answer"] = "quiz_answer"
    defaults["quiz_answer_idx"] = "quiz_answer_idx"
    defaults["quiz_correct"] = "quiz_correct"
    defaults["quiz_score"] = "quiz_score"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults["test_type"] = "test_type"
    defaults.update(**kwargs)
    return QuizAnswerInfo.objects.create(**defaults)


def create_quizexampleinfo(**kwargs):
    defaults = {}
    defaults["quiz_code"] = "quiz_code"
    defaults["quiz_example"] = "quiz_example"
    defaults["quiz_example_correct"] = "quiz_example_correct"
    defaults["quiz_example_idx"] = "quiz_example_idx"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults["quiz_example_type"] = "quiz_example_type"
    defaults.update(**kwargs)
    return QuizExampleInfo.objects.create(**defaults)


def create_quizinfo(**kwargs):
    defaults = {}
    defaults["subject_code"] = "subject_code"
    defaults["lecture_code"] = "lecture_code"
    defaults["chapter_code"] = "chapter_code"
    defaults["quiz_type"] = "quiz_type"
    defaults["quiz_question"] = "quiz_question"
    defaults["quiz_media_type"] = "quiz_media_type"
    defaults["quiz_media_file"] = "quiz_media_file"
    defaults["quiz_score"] = "quiz_score"
    defaults["quiz_comment"] = "quiz_comment"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults["quiz_head"] = "quiz_head"
    defaults["quiz_media_file2"] = "quiz_media_file2"
    defaults.update(**kwargs)
    return QuizInfo.objects.create(**defaults)


def create_scheduleinfo(**kwargs):
    defaults = {}
    defaults["member_code"] = "member_code"
    defaults["title"] = "title"
    defaults["content"] = "content"
    defaults["start_date"] = "start_date"
    defaults["start_time"] = "start_time"
    defaults["end_date"] = "end_date"
    defaults["end_time"] = "end_time"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return ScheduleInfo.objects.create(**defaults)


def create_talkmember(**kwargs):
    defaults = {}
    defaults["member_code"] = "member_code"
    defaults["use_flag"] = "use_flag"
    defaults.update(**kwargs)
    return TalkMember.objects.create(**defaults)


def create_talkmessage(**kwargs):
    defaults = {}
    defaults["talk_room_id"] = "talk_room_id"
    defaults["message"] = "message"
    defaults["sender_member_code"] = "sender_member_code"
    defaults["send_date"] = "send_date"
    defaults["send_time"] = "send_time"
    defaults.update(**kwargs)
    return TalkMessage.objects.create(**defaults)


def create_talkmessageread(**kwargs):
    defaults = {}
    defaults["member_code"] = "member_code"
    defaults["is_read"] = "is_read"
    defaults.update(**kwargs)
    return TalkMessageRead.objects.create(**defaults)


def create_talkroom(**kwargs):
    defaults = {}
    defaults["talk_room_cate_code"] = "talk_room_cate_code"
    defaults["lecture_code"] = "lecture_code"
    defaults["inning_code"] = "inning_code"
    defaults["use_flag"] = "use_flag"
    defaults.update(**kwargs)
    return TalkRoom.objects.create(**defaults)


def create_todoinfo(**kwargs):
    defaults = {}
    defaults["chapter_code"] = "chapter_code"
    defaults["member_code"] = "member_code"
    defaults["todo_comment"] = "todo_comment"
    defaults["todo_status"] = "todo_status"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults["teacher_code"] = "teacher_code"
    defaults["todo_title"] = "todo_title"
    defaults["start_date"] = "start_date"
    defaults["start_time"] = "start_time"
    defaults["end_date"] = "end_date"
    defaults["end_time"] = "end_time"
    defaults["lecture_code"] = "lecture_code"
    defaults.update(**kwargs)
    return TodoInfo.objects.create(**defaults)


def create_todotinfo(**kwargs):
    defaults = {}
    defaults["todo_code"] = "todo_code"
    defaults["member_code"] = "member_code"
    defaults["todo_t_flag"] = "todo_t_flag"
    defaults["use_flag"] = "use_flag"
    defaults["reg_date"] = "reg_date"
    defaults["reg_time"] = "reg_time"
    defaults["reg_agent"] = "reg_agent"
    defaults["udt_date"] = "udt_date"
    defaults["udt_time"] = "udt_time"
    defaults["udt_agent"] = "udt_agent"
    defaults.update(**kwargs)
    return TodoTInfo.objects.create(**defaults)


class AssignHomeworkInfoViewTest(unittest.TestCase):
    '''
    Tests for AssignHomeworkInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_assignhomeworkinfo(self):
        url = reverse('WebApp_assignhomeworkinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_assignhomeworkinfo(self):
        url = reverse('WebApp_assignhomeworkinfo_create')
        data = {
            "question_code": "question_code",
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "member_code": "member_code",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_assignhomeworkinfo(self):
        assignhomeworkinfo = create_assignhomeworkinfo()
        url = reverse('WebApp_assignhomeworkinfo_detail', args=[assignhomeworkinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_assignhomeworkinfo(self):
        assignhomeworkinfo = create_assignhomeworkinfo()
        data = {
            "question_code": "question_code",
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "member_code": "member_code",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_assignhomeworkinfo_update', args=[assignhomeworkinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AssignQuestionInfoViewTest(unittest.TestCase):
    '''
    Tests for AssignQuestionInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_assignquestioninfo(self):
        url = reverse('WebApp_assignquestioninfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_assignquestioninfo(self):
        url = reverse('WebApp_assignquestioninfo_create')
        data = {
            "question_code": "question_code",
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "question_type": "question_type",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_assignquestioninfo(self):
        assignquestioninfo = create_assignquestioninfo()
        url = reverse('WebApp_assignquestioninfo_detail', args=[assignquestioninfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_assignquestioninfo(self):
        assignquestioninfo = create_assignquestioninfo()
        data = {
            "question_code": "question_code",
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "question_type": "question_type",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_assignquestioninfo_update', args=[assignquestioninfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class BoardContentInfoViewTest(unittest.TestCase):
    '''
    Tests for BoardContentInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_boardcontentinfo(self):
        url = reverse('WebApp_boardcontentinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_boardcontentinfo(self):
        url = reverse('WebApp_boardcontentinfo_create')
        data = {
            "board_code": "board_code",
            "admin_id": "admin_id",
            "title": "title",
            "contents": "contents",
            "writer": "writer",
            "view_cnt": "view_cnt",
            "ref_code": "ref_code",
            "ref_step": "ref_step",
            "ref_level": "ref_level",
            "write_time": "write_time",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_boardcontentinfo(self):
        boardcontentinfo = create_boardcontentinfo()
        url = reverse('WebApp_boardcontentinfo_detail', args=[boardcontentinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_boardcontentinfo(self):
        boardcontentinfo = create_boardcontentinfo()
        data = {
            "board_code": "board_code",
            "admin_id": "admin_id",
            "title": "title",
            "contents": "contents",
            "writer": "writer",
            "view_cnt": "view_cnt",
            "ref_code": "ref_code",
            "ref_step": "ref_step",
            "ref_level": "ref_level",
            "write_time": "write_time",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_boardcontentinfo_update', args=[boardcontentinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class BoardInfoViewTest(unittest.TestCase):
    '''
    Tests for BoardInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_boardinfo(self):
        url = reverse('WebApp_boardinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_boardinfo(self):
        url = reverse('WebApp_boardinfo_create')
        data = {
            "board_name": "board_name",
            "board_write_level": "board_write_level",
            "board_read_level": "board_read_level",
            "board_reply_level": "board_reply_level",
            "board_new_time": "board_new_time",
            "board_create_time": "board_create_time",
            "admin_id": "admin_id",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_boardinfo(self):
        boardinfo = create_boardinfo()
        url = reverse('WebApp_boardinfo_detail', args=[boardinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_boardinfo(self):
        boardinfo = create_boardinfo()
        data = {
            "board_name": "board_name",
            "board_write_level": "board_write_level",
            "board_read_level": "board_read_level",
            "board_reply_level": "board_reply_level",
            "board_new_time": "board_new_time",
            "board_create_time": "board_create_time",
            "admin_id": "admin_id",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_boardinfo_update', args=[boardinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CenterInfoViewTest(unittest.TestCase):
    '''
    Tests for CenterInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_centerinfo(self):
        url = reverse('WebApp_centerinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_centerinfo(self):
        url = reverse('WebApp_centerinfo_create')
        data = {
            "center_name": "center_name",
            "center_location": "center_location",
            "center_tel": "center_tel",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_centerinfo(self):
        centerinfo = create_centerinfo()
        url = reverse('WebApp_centerinfo_detail', args=[centerinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_centerinfo(self):
        centerinfo = create_centerinfo()
        data = {
            "center_name": "center_name",
            "center_location": "center_location",
            "center_tel": "center_tel",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_centerinfo_update', args=[centerinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ChapterContentMediaViewTest(unittest.TestCase):
    '''
    Tests for ChapterContentMedia
    '''
    def setUp(self):
        self.client = Client()

    def test_list_chaptercontentmedia(self):
        url = reverse('WebApp_chaptercontentmedia_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_chaptercontentmedia(self):
        url = reverse('WebApp_chaptercontentmedia_create')
        data = {
            "chapter_contents_code": "chapter_contents_code",
            "media_type": "media_type",
            "media_desc": "media_desc",
            "media_filename": "media_filename",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "reg_agent": "reg_agent",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_chaptercontentmedia(self):
        chaptercontentmedia = create_chaptercontentmedia()
        url = reverse('WebApp_chaptercontentmedia_detail', args=[chaptercontentmedia.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_chaptercontentmedia(self):
        chaptercontentmedia = create_chaptercontentmedia()
        data = {
            "chapter_contents_code": "chapter_contents_code",
            "media_type": "media_type",
            "media_desc": "media_desc",
            "media_filename": "media_filename",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "reg_agent": "reg_agent",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_chaptercontentmedia_update', args=[chaptercontentmedia.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ChapterContentsInfoViewTest(unittest.TestCase):
    '''
    Tests for ChapterContentsInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_chaptercontentsinfo(self):
        url = reverse('WebApp_chaptercontentsinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_chaptercontentsinfo(self):
        url = reverse('WebApp_chaptercontentsinfo_create')
        data = {
            "chapter_code": "chapter_code",
            "chapter_contents": "chapter_contents",
            "chapter_audio": "chapter_audio",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "contents_index": "contents_index",
            "chapter_type": "chapter_type",
            "thum_file": "thum_file",
            "vod_file": "vod_file",
            "today": "today",
            "front1_img": "front1_img",
            "front1_text": "front1_text",
            "back1_img": "back1_img",
            "back1_text": "back1_text",
            "pdf_file": "pdf_file",
            "front2_img": "front2_img",
            "front3_img": "front3_img",
            "front4_img": "front4_img",
            "front2_text": "front2_text",
            "front3_text": "front3_text",
            "front4_text": "front4_text",
            "back2_img": "back2_img",
            "back3_img": "back3_img",
            "back4_img": "back4_img",
            "back2_text": "back2_text",
            "back3_text": "back3_text",
            "back4_text": "back4_text",
            "c1_audio": "c1_audio",
            "c2_audio": "c2_audio",
            "c3_audio": "c3_audio",
            "c4_audio": "c4_audio",
            "vod_size": "vod_size",
            "offline_file": "offline_file",
            "teacher_guide": "teacher_guide",
            "today_text": "today_text",
            "contents_text": "contents_text",
            "pbl_allow": "pbl_allow",
            "pbl_lec_allow": "pbl_lec_allow",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_chaptercontentsinfo(self):
        chaptercontentsinfo = create_chaptercontentsinfo()
        url = reverse('WebApp_chaptercontentsinfo_detail', args=[chaptercontentsinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_chaptercontentsinfo(self):
        chaptercontentsinfo = create_chaptercontentsinfo()
        data = {
            "chapter_code": "chapter_code",
            "chapter_contents": "chapter_contents",
            "chapter_audio": "chapter_audio",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "contents_index": "contents_index",
            "chapter_type": "chapter_type",
            "thum_file": "thum_file",
            "vod_file": "vod_file",
            "today": "today",
            "front1_img": "front1_img",
            "front1_text": "front1_text",
            "back1_img": "back1_img",
            "back1_text": "back1_text",
            "pdf_file": "pdf_file",
            "front2_img": "front2_img",
            "front3_img": "front3_img",
            "front4_img": "front4_img",
            "front2_text": "front2_text",
            "front3_text": "front3_text",
            "front4_text": "front4_text",
            "back2_img": "back2_img",
            "back3_img": "back3_img",
            "back4_img": "back4_img",
            "back2_text": "back2_text",
            "back3_text": "back3_text",
            "back4_text": "back4_text",
            "c1_audio": "c1_audio",
            "c2_audio": "c2_audio",
            "c3_audio": "c3_audio",
            "c4_audio": "c4_audio",
            "vod_size": "vod_size",
            "offline_file": "offline_file",
            "teacher_guide": "teacher_guide",
            "today_text": "today_text",
            "contents_text": "contents_text",
            "pbl_allow": "pbl_allow",
            "pbl_lec_allow": "pbl_lec_allow",
        }
        url = reverse('WebApp_chaptercontentsinfo_update', args=[chaptercontentsinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ChapterImgInfoViewTest(unittest.TestCase):
    '''
    Tests for ChapterImgInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_chapterimginfo(self):
        url = reverse('WebApp_chapterimginfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_chapterimginfo(self):
        url = reverse('WebApp_chapterimginfo_create')
        data = {
            "chapter_code": "chapter_code",
            "filename": "filename",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_chapterimginfo(self):
        chapterimginfo = create_chapterimginfo()
        url = reverse('WebApp_chapterimginfo_detail', args=[chapterimginfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_chapterimginfo(self):
        chapterimginfo = create_chapterimginfo()
        data = {
            "chapter_code": "chapter_code",
            "filename": "filename",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_chapterimginfo_update', args=[chapterimginfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ChapterInfoViewTest(unittest.TestCase):
    '''
    Tests for ChapterInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_chapterinfo(self):
        url = reverse('WebApp_chapterinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_chapterinfo(self):
        url = reverse('WebApp_chapterinfo_create')
        data = {
            "lecture_code": "lecture_code",
            "chapter_no": "chapter_no",
            "chapter_name": "chapter_name",
            "topic": "topic",
            "summary": "summary",
            "page_num": "page_num",
            "vod_size": "vod_size",
            "intro": "intro",
            "target": "target",
            "top_img": "top_img",
            "bottom_img1": "bottom_img1",
            "bottom_img2": "bottom_img2",
            "bottom_img3": "bottom_img3",
            "thum_file": "thum_file",
            "vod_file": "vod_file",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "today": "today",
            "chapter_type": "chapter_type",
            "prologue_type": "prologue_type",
            "tabset": "tabset",
            "chapter_image": "chapter_image",
            "chapter_use": "chapter_use",
            "offline_file": "offline_file",
            "pre_test_type": "pre_test_type",
            "post_test_type": "post_test_type",
            "level1_avg": "level1_avg",
            "level2_avg": "level2_avg",
            "level3_avg": "level3_avg",
            "level1_hard_avg": "level1_hard_avg",
            "level1_medium_avg": "level1_medium_avg",
            "level1_easy_avg": "level1_easy_avg",
            "level2_hard_avg": "level2_hard_avg",
            "level2_medium_avg": "level2_medium_avg",
            "level2_easy_avg": "level2_easy_avg",
            "level3_hard_avg": "level3_hard_avg",
            "level3_medium_avg": "level3_medium_avg",
            "level3_easy_avg": "level3_easy_avg",
            "homework_count": "homework_count",
            "epilogue_type": "epilogue_type",
            "epilogue_img": "epilogue_img",
            "pbl_flag": "pbl_flag",
            "chapter_use_time": "chapter_use_time",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_chapterinfo(self):
        chapterinfo = create_chapterinfo()
        url = reverse('WebApp_chapterinfo_detail', args=[chapterinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_chapterinfo(self):
        chapterinfo = create_chapterinfo()
        data = {
            "lecture_code": "lecture_code",
            "chapter_no": "chapter_no",
            "chapter_name": "chapter_name",
            "topic": "topic",
            "summary": "summary",
            "page_num": "page_num",
            "vod_size": "vod_size",
            "intro": "intro",
            "target": "target",
            "top_img": "top_img",
            "bottom_img1": "bottom_img1",
            "bottom_img2": "bottom_img2",
            "bottom_img3": "bottom_img3",
            "thum_file": "thum_file",
            "vod_file": "vod_file",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "today": "today",
            "chapter_type": "chapter_type",
            "prologue_type": "prologue_type",
            "tabset": "tabset",
            "chapter_image": "chapter_image",
            "chapter_use": "chapter_use",
            "offline_file": "offline_file",
            "pre_test_type": "pre_test_type",
            "post_test_type": "post_test_type",
            "level1_avg": "level1_avg",
            "level2_avg": "level2_avg",
            "level3_avg": "level3_avg",
            "level1_hard_avg": "level1_hard_avg",
            "level1_medium_avg": "level1_medium_avg",
            "level1_easy_avg": "level1_easy_avg",
            "level2_hard_avg": "level2_hard_avg",
            "level2_medium_avg": "level2_medium_avg",
            "level2_easy_avg": "level2_easy_avg",
            "level3_hard_avg": "level3_hard_avg",
            "level3_medium_avg": "level3_medium_avg",
            "level3_easy_avg": "level3_easy_avg",
            "homework_count": "homework_count",
            "epilogue_type": "epilogue_type",
            "epilogue_img": "epilogue_img",
            "pbl_flag": "pbl_flag",
            "chapter_use_time": "chapter_use_time",
        }
        url = reverse('WebApp_chapterinfo_update', args=[chapterinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ChapterMissonCheckViewTest(unittest.TestCase):
    '''
    Tests for ChapterMissonCheck
    '''
    def setUp(self):
        self.client = Client()

    def test_list_chaptermissoncheck(self):
        url = reverse('WebApp_chaptermissoncheck_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_chaptermissoncheck(self):
        url = reverse('WebApp_chaptermissoncheck_create')
        data = {
            "check_code": "check_code",
            "check_item_code": "check_item_code",
            "student_code": "student_code",
            "check_agent_code": "check_agent_code",
            "is_check_yn": "is_check_yn",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "inning_code": "inning_code",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_chaptermissoncheck(self):
        chaptermissoncheck = create_chaptermissoncheck()
        url = reverse('WebApp_chaptermissoncheck_detail', args=[chaptermissoncheck.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_chaptermissoncheck(self):
        chaptermissoncheck = create_chaptermissoncheck()
        data = {
            "check_code": "check_code",
            "check_item_code": "check_item_code",
            "student_code": "student_code",
            "check_agent_code": "check_agent_code",
            "is_check_yn": "is_check_yn",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "inning_code": "inning_code",
        }
        url = reverse('WebApp_chaptermissoncheck_update', args=[chaptermissoncheck.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ChapterMissonCheckCardViewTest(unittest.TestCase):
    '''
    Tests for ChapterMissonCheckCard
    '''
    def setUp(self):
        self.client = Client()

    def test_list_chaptermissoncheckcard(self):
        url = reverse('WebApp_chaptermissoncheckcard_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_chaptermissoncheckcard(self):
        url = reverse('WebApp_chaptermissoncheckcard_create')
        data = {
            "check_card_code": "check_card_code",
            "chapter_code": "chapter_code",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_chaptermissoncheckcard(self):
        chaptermissoncheckcard = create_chaptermissoncheckcard()
        url = reverse('WebApp_chaptermissoncheckcard_detail', args=[chaptermissoncheckcard.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_chaptermissoncheckcard(self):
        chaptermissoncheckcard = create_chaptermissoncheckcard()
        data = {
            "check_card_code": "check_card_code",
            "chapter_code": "chapter_code",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_chaptermissoncheckcard_update', args=[chaptermissoncheckcard.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ChapterMissonCheckItemViewTest(unittest.TestCase):
    '''
    Tests for ChapterMissonCheckItem
    '''
    def setUp(self):
        self.client = Client()

    def test_list_chaptermissoncheckitem(self):
        url = reverse('WebApp_chaptermissoncheckitem_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_chaptermissoncheckitem(self):
        url = reverse('WebApp_chaptermissoncheckitem_create')
        data = {
            "check_item_code": "check_item_code",
            "check_card_code": "check_card_code",
            "item_text": "item_text",
            "contents_text": "contents_text",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "chapter_contents_code": "chapter_contents_code",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_chaptermissoncheckitem(self):
        chaptermissoncheckitem = create_chaptermissoncheckitem()
        url = reverse('WebApp_chaptermissoncheckitem_detail', args=[chaptermissoncheckitem.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_chaptermissoncheckitem(self):
        chaptermissoncheckitem = create_chaptermissoncheckitem()
        data = {
            "check_item_code": "check_item_code",
            "check_card_code": "check_card_code",
            "item_text": "item_text",
            "contents_text": "contents_text",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "chapter_contents_code": "chapter_contents_code",
        }
        url = reverse('WebApp_chaptermissoncheckitem_update', args=[chaptermissoncheckitem.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ChapterWriteViewTest(unittest.TestCase):
    '''
    Tests for ChapterWrite
    '''
    def setUp(self):
        self.client = Client()

    def test_list_chapterwrite(self):
        url = reverse('WebApp_chapterwrite_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_chapterwrite(self):
        url = reverse('WebApp_chapterwrite_create')
        data = {
            "inning_code": "inning_code",
            "chapter_contents_code": "chapter_contents_code",
            "student_code": "student_code",
            "write_content": "write_content",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_chapterwrite(self):
        chapterwrite = create_chapterwrite()
        url = reverse('WebApp_chapterwrite_detail', args=[chapterwrite.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_chapterwrite(self):
        chapterwrite = create_chapterwrite()
        data = {
            "inning_code": "inning_code",
            "chapter_contents_code": "chapter_contents_code",
            "student_code": "student_code",
            "write_content": "write_content",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_chapterwrite_update', args=[chapterwrite.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class GroupMappingViewTest(unittest.TestCase):
    '''
    Tests for GroupMapping
    '''
    def setUp(self):
        self.client = Client()

    def test_list_groupmapping(self):
        url = reverse('WebApp_groupmapping_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_groupmapping(self):
        url = reverse('WebApp_groupmapping_create')
        data = {
            "center_code": "center_code",
            "group_code": "group_code",
            "member_code": "member_code",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_groupmapping(self):
        groupmapping = create_groupmapping()
        url = reverse('WebApp_groupmapping_detail', args=[groupmapping.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_groupmapping(self):
        groupmapping = create_groupmapping()
        data = {
            "center_code": "center_code",
            "group_code": "group_code",
            "member_code": "member_code",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_groupmapping_update', args=[groupmapping.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class HomeworkInfoViewTest(unittest.TestCase):
    '''
    Tests for HomeworkInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_homeworkinfo(self):
        url = reverse('WebApp_homeworkinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_homeworkinfo(self):
        url = reverse('WebApp_homeworkinfo_create')
        data = {
            "question_code": "question_code",
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "level_score": "level_score",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "level": "level",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_homeworkinfo(self):
        homeworkinfo = create_homeworkinfo()
        url = reverse('WebApp_homeworkinfo_detail', args=[homeworkinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_homeworkinfo(self):
        homeworkinfo = create_homeworkinfo()
        data = {
            "question_code": "question_code",
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "level_score": "level_score",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "level": "level",
        }
        url = reverse('WebApp_homeworkinfo_update', args=[homeworkinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class InningGroupViewTest(unittest.TestCase):
    '''
    Tests for InningGroup
    '''
    def setUp(self):
        self.client = Client()

    def test_list_inninggroup(self):
        url = reverse('WebApp_inninggroup_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_inninggroup(self):
        url = reverse('WebApp_inninggroup_create')
        data = {
            "center_code": "center_code",
            "inning_code": "inning_code",
            "lecture_code": "lecture_code",
            "teacher_code": "teacher_code",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_inninggroup(self):
        inninggroup = create_inninggroup()
        url = reverse('WebApp_inninggroup_detail', args=[inninggroup.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_inninggroup(self):
        inninggroup = create_inninggroup()
        data = {
            "center_code": "center_code",
            "inning_code": "inning_code",
            "lecture_code": "lecture_code",
            "teacher_code": "teacher_code",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_inninggroup_update', args=[inninggroup.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class InningInfoViewTest(unittest.TestCase):
    '''
    Tests for InningInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_inninginfo(self):
        url = reverse('WebApp_inninginfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_inninginfo(self):
        url = reverse('WebApp_inninginfo_create')
        data = {
            "inning_name": "inning_name",
            "lecture_code": "lecture_code",
            "start_date": "start_date",
            "end_date": "end_date",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "center_code": "center_code",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_inninginfo(self):
        inninginfo = create_inninginfo()
        url = reverse('WebApp_inninginfo_detail', args=[inninginfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_inninginfo(self):
        inninginfo = create_inninginfo()
        data = {
            "inning_name": "inning_name",
            "lecture_code": "lecture_code",
            "start_date": "start_date",
            "end_date": "end_date",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "center_code": "center_code",
        }
        url = reverse('WebApp_inninginfo_update', args=[inninginfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LearningNoteViewTest(unittest.TestCase):
    '''
    Tests for LearningNote
    '''
    def setUp(self):
        self.client = Client()

    def test_list_learningnote(self):
        url = reverse('WebApp_learningnote_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_learningnote(self):
        url = reverse('WebApp_learningnote_create')
        data = {
            "inning_code": "inning_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "contents_code": "contents_code",
            "note_contents": "note_contents",
            "note_attachment": "note_attachment",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_learningnote(self):
        learningnote = create_learningnote()
        url = reverse('WebApp_learningnote_detail', args=[learningnote.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_learningnote(self):
        learningnote = create_learningnote()
        data = {
            "inning_code": "inning_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "contents_code": "contents_code",
            "note_contents": "note_contents",
            "note_attachment": "note_attachment",
        }
        url = reverse('WebApp_learningnote_update', args=[learningnote.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LectureInfoViewTest(unittest.TestCase):
    '''
    Tests for LectureInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_lectureinfo(self):
        url = reverse('WebApp_lectureinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_lectureinfo(self):
        url = reverse('WebApp_lectureinfo_create')
        data = {
            "lecture_name": "lecture_name",
            "lecture_teacher": "lecture_teacher",
            "lecture_cover": "lecture_cover",
            "lecture_cover_file": "lecture_cover_file",
            "lecture_level": "lecture_level",
            "lecture_info": "lecture_info",
            "teacher": "teacher",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "lecture_certification": "lecture_certification",
            "lecture_provider": "lecture_provider",
            "cert_crit_prog": "cert_crit_prog",
            "cert_crit_post": "cert_crit_post",
            "cert_crit_ubt": "cert_crit_ubt",
            "cert_crit_issue": "cert_crit_issue",
            "center_code": "center_code",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_lectureinfo(self):
        lectureinfo = create_lectureinfo()
        url = reverse('WebApp_lectureinfo_detail', args=[lectureinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_lectureinfo(self):
        lectureinfo = create_lectureinfo()
        data = {
            "lecture_name": "lecture_name",
            "lecture_teacher": "lecture_teacher",
            "lecture_cover": "lecture_cover",
            "lecture_cover_file": "lecture_cover_file",
            "lecture_level": "lecture_level",
            "lecture_info": "lecture_info",
            "teacher": "teacher",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "lecture_certification": "lecture_certification",
            "lecture_provider": "lecture_provider",
            "cert_crit_prog": "cert_crit_prog",
            "cert_crit_post": "cert_crit_post",
            "cert_crit_ubt": "cert_crit_ubt",
            "cert_crit_issue": "cert_crit_issue",
            "center_code": "center_code",
        }
        url = reverse('WebApp_lectureinfo_update', args=[lectureinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LectureUbtInfoViewTest(unittest.TestCase):
    '''
    Tests for LectureUbtInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_lectureubtinfo(self):
        url = reverse('WebApp_lectureubtinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_lectureubtinfo(self):
        url = reverse('WebApp_lectureubtinfo_create')
        data = {
            "quiz_code": "quiz_code",
            "lecture_code": "lecture_code",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_lectureubtinfo(self):
        lectureubtinfo = create_lectureubtinfo()
        url = reverse('WebApp_lectureubtinfo_detail', args=[lectureubtinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_lectureubtinfo(self):
        lectureubtinfo = create_lectureubtinfo()
        data = {
            "quiz_code": "quiz_code",
            "lecture_code": "lecture_code",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_lectureubtinfo_update', args=[lectureubtinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LessonInfoViewTest(unittest.TestCase):
    '''
    Tests for LessonInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_lessoninfo(self):
        url = reverse('WebApp_lessoninfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_lessoninfo(self):
        url = reverse('WebApp_lessoninfo_create')
        data = {
            "lecture_code": "lecture_code",
            "member_code": "member_code",
            "teacher_code": "teacher_code",
            "start_date": "start_date",
            "end_date": "end_date",
            "progress": "progress",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "ubt_start": "ubt_start",
            "ubt_end": "ubt_end",
            "download_count": "download_count",
            "download_date": "download_date",
            "center_code": "center_code",
            "inning_code": "inning_code",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_lessoninfo(self):
        lessoninfo = create_lessoninfo()
        url = reverse('WebApp_lessoninfo_detail', args=[lessoninfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_lessoninfo(self):
        lessoninfo = create_lessoninfo()
        data = {
            "lecture_code": "lecture_code",
            "member_code": "member_code",
            "teacher_code": "teacher_code",
            "start_date": "start_date",
            "end_date": "end_date",
            "progress": "progress",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "ubt_start": "ubt_start",
            "ubt_end": "ubt_end",
            "download_count": "download_count",
            "download_date": "download_date",
            "center_code": "center_code",
            "inning_code": "inning_code",
        }
        url = reverse('WebApp_lessoninfo_update', args=[lessoninfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LessonLogViewTest(unittest.TestCase):
    '''
    Tests for LessonLog
    '''
    def setUp(self):
        self.client = Client()

    def test_list_lessonlog(self):
        url = reverse('WebApp_lessonlog_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_lessonlog(self):
        url = reverse('WebApp_lessonlog_create')
        data = {
            "lesson_code": "lesson_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "member_code": "member_code",
            "member_id": "member_id",
            "member_ip": "member_ip",
            "member_browser": "member_browser",
            "member_os": "member_os",
            "start_date": "start_date",
            "start_time": "start_time",
            "end_date": "end_date",
            "end_time": "end_time",
            "connect_date": "connect_date",
            "connect_time": "connect_time",
            "connect_count": "connect_count",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "study_time": "study_time",
            "connect_page": "connect_page",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_lessonlog(self):
        lessonlog = create_lessonlog()
        url = reverse('WebApp_lessonlog_detail', args=[lessonlog.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_lessonlog(self):
        lessonlog = create_lessonlog()
        data = {
            "lesson_code": "lesson_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "member_code": "member_code",
            "member_id": "member_id",
            "member_ip": "member_ip",
            "member_browser": "member_browser",
            "member_os": "member_os",
            "start_date": "start_date",
            "start_time": "start_time",
            "end_date": "end_date",
            "end_time": "end_time",
            "connect_date": "connect_date",
            "connect_time": "connect_time",
            "connect_count": "connect_count",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "study_time": "study_time",
            "connect_page": "connect_page",
        }
        url = reverse('WebApp_lessonlog_update', args=[lessonlog.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class MemberGroupViewTest(unittest.TestCase):
    '''
    Tests for MemberGroup
    '''
    def setUp(self):
        self.client = Client()

    def test_list_membergroup(self):
        url = reverse('WebApp_membergroup_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_membergroup(self):
        url = reverse('WebApp_membergroup_create')
        data = {
            "center_code": "center_code",
            "group_name": "group_name",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_membergroup(self):
        membergroup = create_membergroup()
        url = reverse('WebApp_membergroup_detail', args=[membergroup.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_membergroup(self):
        membergroup = create_membergroup()
        data = {
            "center_code": "center_code",
            "group_name": "group_name",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_membergroup_update', args=[membergroup.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class MemberInfoViewTest(unittest.TestCase):
    '''
    Tests for MemberInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_memberinfo(self):
        url = reverse('WebApp_memberinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_memberinfo(self):
        url = reverse('WebApp_memberinfo_create')
        data = {
            "member_id": "member_id",
            "member_level": "member_level",
            "member_pw": "member_pw",
            "member_name": "member_name",
            "member_jumin": "member_jumin",
            "member_birth": "member_birth",
            "member_college": "member_college",
            "member_email": "member_email",
            "member_phone": "member_phone",
            "member_post": "member_post",
            "member_addr1": "member_addr1",
            "member_addr2": "member_addr2",
            "member_file": "member_file",
            "member_gender": "member_gender",
            "member_major": "member_major",
            "member_nation": "member_nation",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "center_code": "center_code",
            "member_fax": "member_fax",
            "member_memo": "member_memo",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_memberinfo(self):
        memberinfo = create_memberinfo()
        url = reverse('WebApp_memberinfo_detail', args=[memberinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_memberinfo(self):
        memberinfo = create_memberinfo()
        data = {
            "member_id": "member_id",
            "member_level": "member_level",
            "member_pw": "member_pw",
            "member_name": "member_name",
            "member_jumin": "member_jumin",
            "member_birth": "member_birth",
            "member_college": "member_college",
            "member_email": "member_email",
            "member_phone": "member_phone",
            "member_post": "member_post",
            "member_addr1": "member_addr1",
            "member_addr2": "member_addr2",
            "member_file": "member_file",
            "member_gender": "member_gender",
            "member_major": "member_major",
            "member_nation": "member_nation",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "center_code": "center_code",
            "member_fax": "member_fax",
            "member_memo": "member_memo",
        }
        url = reverse('WebApp_memberinfo_update', args=[memberinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class MessageInfoViewTest(unittest.TestCase):
    '''
    Tests for MessageInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_messageinfo(self):
        url = reverse('WebApp_messageinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_messageinfo(self):
        url = reverse('WebApp_messageinfo_create')
        data = {
            "teacher_code": "teacher_code",
            "member_code": "member_code",
            "message": "message",
            "message_read": "message_read",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_messageinfo(self):
        messageinfo = create_messageinfo()
        url = reverse('WebApp_messageinfo_detail', args=[messageinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_messageinfo(self):
        messageinfo = create_messageinfo()
        data = {
            "teacher_code": "teacher_code",
            "member_code": "member_code",
            "message": "message",
            "message_read": "message_read",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_messageinfo_update', args=[messageinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class OmrAnswerInfoViewTest(unittest.TestCase):
    '''
    Tests for OmrAnswerInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_omranswerinfo(self):
        url = reverse('WebApp_omranswerinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_omranswerinfo(self):
        url = reverse('WebApp_omranswerinfo_create')
        data = {
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "member_code": "member_code",
            "question_code": "question_code",
            "omr_answer": "omr_answer",
            "omr_answer_idx": "omr_answer_idx",
            "omr_answer_correct": "omr_answer_correct",
            "question_score": "question_score",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "lesson_code": "lesson_code",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_omranswerinfo(self):
        omranswerinfo = create_omranswerinfo()
        url = reverse('WebApp_omranswerinfo_detail', args=[omranswerinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_omranswerinfo(self):
        omranswerinfo = create_omranswerinfo()
        data = {
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "member_code": "member_code",
            "question_code": "question_code",
            "omr_answer": "omr_answer",
            "omr_answer_idx": "omr_answer_idx",
            "omr_answer_correct": "omr_answer_correct",
            "question_score": "question_score",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "lesson_code": "lesson_code",
        }
        url = reverse('WebApp_omranswerinfo_update', args=[omranswerinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class OmrAssignInfoViewTest(unittest.TestCase):
    '''
    Tests for OmrAssignInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_omrassigninfo(self):
        url = reverse('WebApp_omrassigninfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_omrassigninfo(self):
        url = reverse('WebApp_omrassigninfo_create')
        data = {
            "question_code": "question_code",
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "member_code": "member_code",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_omrassigninfo(self):
        omrassigninfo = create_omrassigninfo()
        url = reverse('WebApp_omrassigninfo_detail', args=[omrassigninfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_omrassigninfo(self):
        omrassigninfo = create_omrassigninfo()
        data = {
            "question_code": "question_code",
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "member_code": "member_code",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_omrassigninfo_update', args=[omrassigninfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class OmrExampleInfoViewTest(unittest.TestCase):
    '''
    Tests for OmrExampleInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_omrexampleinfo(self):
        url = reverse('WebApp_omrexampleinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_omrexampleinfo(self):
        url = reverse('WebApp_omrexampleinfo_create')
        data = {
            "question_code": "question_code",
            "omr_example_correct": "omr_example_correct",
            "omr_example_idx": "omr_example_idx",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_omrexampleinfo(self):
        omrexampleinfo = create_omrexampleinfo()
        url = reverse('WebApp_omrexampleinfo_detail', args=[omrexampleinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_omrexampleinfo(self):
        omrexampleinfo = create_omrexampleinfo()
        data = {
            "question_code": "question_code",
            "omr_example_correct": "omr_example_correct",
            "omr_example_idx": "omr_example_idx",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_omrexampleinfo_update', args=[omrexampleinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class OmrQuestionInfoViewTest(unittest.TestCase):
    '''
    Tests for OmrQuestionInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_omrquestioninfo(self):
        url = reverse('WebApp_omrquestioninfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_omrquestioninfo(self):
        url = reverse('WebApp_omrquestioninfo_create')
        data = {
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "question_level": "question_level",
            "question_score": "question_score",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_omrquestioninfo(self):
        omrquestioninfo = create_omrquestioninfo()
        url = reverse('WebApp_omrquestioninfo_detail', args=[omrquestioninfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_omrquestioninfo(self):
        omrquestioninfo = create_omrquestioninfo()
        data = {
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "question_level": "question_level",
            "question_score": "question_score",
        }
        url = reverse('WebApp_omrquestioninfo_update', args=[omrquestioninfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class QAnswerInfoViewTest(unittest.TestCase):
    '''
    Tests for QAnswerInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_qanswerinfo(self):
        url = reverse('WebApp_qanswerinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_qanswerinfo(self):
        url = reverse('WebApp_qanswerinfo_create')
        data = {
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "member_code": "member_code",
            "question_code": "question_code",
            "question_type": "question_type",
            "question_answer": "question_answer",
            "question_idx": "question_idx",
            "question_correct": "question_correct",
            "question_score": "question_score",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "lesson_code": "lesson_code",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_qanswerinfo(self):
        qanswerinfo = create_qanswerinfo()
        url = reverse('WebApp_qanswerinfo_detail', args=[qanswerinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_qanswerinfo(self):
        qanswerinfo = create_qanswerinfo()
        data = {
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "member_code": "member_code",
            "question_code": "question_code",
            "question_type": "question_type",
            "question_answer": "question_answer",
            "question_idx": "question_idx",
            "question_correct": "question_correct",
            "question_score": "question_score",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "lesson_code": "lesson_code",
        }
        url = reverse('WebApp_qanswerinfo_update', args=[qanswerinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class QAnswerLogViewTest(unittest.TestCase):
    '''
    Tests for QAnswerLog
    '''
    def setUp(self):
        self.client = Client()

    def test_list_qanswerlog(self):
        url = reverse('WebApp_qanswerlog_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_qanswerlog(self):
        url = reverse('WebApp_qanswerlog_create')
        data = {
            "lecture_code": "lecture_code",
            "member_code": "member_code",
            "question_code": "question_code",
            "question_answer": "question_answer",
            "question_idx": "question_idx",
            "question_score": "question_score",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_qanswerlog(self):
        qanswerlog = create_qanswerlog()
        url = reverse('WebApp_qanswerlog_detail', args=[qanswerlog.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_qanswerlog(self):
        qanswerlog = create_qanswerlog()
        data = {
            "lecture_code": "lecture_code",
            "member_code": "member_code",
            "question_code": "question_code",
            "question_answer": "question_answer",
            "question_idx": "question_idx",
            "question_score": "question_score",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_qanswerlog_update', args=[qanswerlog.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class QExampleInfoViewTest(unittest.TestCase):
    '''
    Tests for QExampleInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_qexampleinfo(self):
        url = reverse('WebApp_qexampleinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_qexampleinfo(self):
        url = reverse('WebApp_qexampleinfo_create')
        data = {
            "question_code": "question_code",
            "q_example": "q_example",
            "q_example_correct": "q_example_correct",
            "q_example_idx": "q_example_idx",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "q_example_type": "q_example_type",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_qexampleinfo(self):
        qexampleinfo = create_qexampleinfo()
        url = reverse('WebApp_qexampleinfo_detail', args=[qexampleinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_qexampleinfo(self):
        qexampleinfo = create_qexampleinfo()
        data = {
            "question_code": "question_code",
            "q_example": "q_example",
            "q_example_correct": "q_example_correct",
            "q_example_idx": "q_example_idx",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "q_example_type": "q_example_type",
        }
        url = reverse('WebApp_qexampleinfo_update', args=[qexampleinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class QuestionInfoViewTest(unittest.TestCase):
    '''
    Tests for QuestionInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_questioninfo(self):
        url = reverse('WebApp_questioninfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_questioninfo(self):
        url = reverse('WebApp_questioninfo_create')
        data = {
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "question_type": "question_type",
            "question": "question",
            "question_media_type": "question_media_type",
            "question_media_file": "question_media_file",
            "question_score": "question_score",
            "question_head": "question_head",
            "question_essay": "question_essay",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "question_media_file2": "question_media_file2",
            "question_comment": "question_comment",
            "question_level": "question_level",
            "teacher_contents": "teacher_contents",
            "student_contents": "student_contents",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_questioninfo(self):
        questioninfo = create_questioninfo()
        url = reverse('WebApp_questioninfo_detail', args=[questioninfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_questioninfo(self):
        questioninfo = create_questioninfo()
        data = {
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "question_type": "question_type",
            "question": "question",
            "question_media_type": "question_media_type",
            "question_media_file": "question_media_file",
            "question_score": "question_score",
            "question_head": "question_head",
            "question_essay": "question_essay",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "question_media_file2": "question_media_file2",
            "question_comment": "question_comment",
            "question_level": "question_level",
            "teacher_contents": "teacher_contents",
            "student_contents": "student_contents",
        }
        url = reverse('WebApp_questioninfo_update', args=[questioninfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class QuizAnswerInfoViewTest(unittest.TestCase):
    '''
    Tests for QuizAnswerInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_quizanswerinfo(self):
        url = reverse('WebApp_quizanswerinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_quizanswerinfo(self):
        url = reverse('WebApp_quizanswerinfo_create')
        data = {
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "member_code": "member_code",
            "quiz_code": "quiz_code",
            "quiz_type": "quiz_type",
            "quiz_answer": "quiz_answer",
            "quiz_answer_idx": "quiz_answer_idx",
            "quiz_correct": "quiz_correct",
            "quiz_score": "quiz_score",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "test_type": "test_type",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_quizanswerinfo(self):
        quizanswerinfo = create_quizanswerinfo()
        url = reverse('WebApp_quizanswerinfo_detail', args=[quizanswerinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_quizanswerinfo(self):
        quizanswerinfo = create_quizanswerinfo()
        data = {
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "member_code": "member_code",
            "quiz_code": "quiz_code",
            "quiz_type": "quiz_type",
            "quiz_answer": "quiz_answer",
            "quiz_answer_idx": "quiz_answer_idx",
            "quiz_correct": "quiz_correct",
            "quiz_score": "quiz_score",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "test_type": "test_type",
        }
        url = reverse('WebApp_quizanswerinfo_update', args=[quizanswerinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class QuizExampleInfoViewTest(unittest.TestCase):
    '''
    Tests for QuizExampleInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_quizexampleinfo(self):
        url = reverse('WebApp_quizexampleinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_quizexampleinfo(self):
        url = reverse('WebApp_quizexampleinfo_create')
        data = {
            "quiz_code": "quiz_code",
            "quiz_example": "quiz_example",
            "quiz_example_correct": "quiz_example_correct",
            "quiz_example_idx": "quiz_example_idx",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "quiz_example_type": "quiz_example_type",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_quizexampleinfo(self):
        quizexampleinfo = create_quizexampleinfo()
        url = reverse('WebApp_quizexampleinfo_detail', args=[quizexampleinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_quizexampleinfo(self):
        quizexampleinfo = create_quizexampleinfo()
        data = {
            "quiz_code": "quiz_code",
            "quiz_example": "quiz_example",
            "quiz_example_correct": "quiz_example_correct",
            "quiz_example_idx": "quiz_example_idx",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "quiz_example_type": "quiz_example_type",
        }
        url = reverse('WebApp_quizexampleinfo_update', args=[quizexampleinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class QuizInfoViewTest(unittest.TestCase):
    '''
    Tests for QuizInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_quizinfo(self):
        url = reverse('WebApp_quizinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_quizinfo(self):
        url = reverse('WebApp_quizinfo_create')
        data = {
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "quiz_type": "quiz_type",
            "quiz_question": "quiz_question",
            "quiz_media_type": "quiz_media_type",
            "quiz_media_file": "quiz_media_file",
            "quiz_score": "quiz_score",
            "quiz_comment": "quiz_comment",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "quiz_head": "quiz_head",
            "quiz_media_file2": "quiz_media_file2",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_quizinfo(self):
        quizinfo = create_quizinfo()
        url = reverse('WebApp_quizinfo_detail', args=[quizinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_quizinfo(self):
        quizinfo = create_quizinfo()
        data = {
            "subject_code": "subject_code",
            "lecture_code": "lecture_code",
            "chapter_code": "chapter_code",
            "quiz_type": "quiz_type",
            "quiz_question": "quiz_question",
            "quiz_media_type": "quiz_media_type",
            "quiz_media_file": "quiz_media_file",
            "quiz_score": "quiz_score",
            "quiz_comment": "quiz_comment",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "quiz_head": "quiz_head",
            "quiz_media_file2": "quiz_media_file2",
        }
        url = reverse('WebApp_quizinfo_update', args=[quizinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ScheduleInfoViewTest(unittest.TestCase):
    '''
    Tests for ScheduleInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_scheduleinfo(self):
        url = reverse('WebApp_scheduleinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_scheduleinfo(self):
        url = reverse('WebApp_scheduleinfo_create')
        data = {
            "member_code": "member_code",
            "title": "title",
            "content": "content",
            "start_date": "start_date",
            "start_time": "start_time",
            "end_date": "end_date",
            "end_time": "end_time",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_scheduleinfo(self):
        scheduleinfo = create_scheduleinfo()
        url = reverse('WebApp_scheduleinfo_detail', args=[scheduleinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_scheduleinfo(self):
        scheduleinfo = create_scheduleinfo()
        data = {
            "member_code": "member_code",
            "title": "title",
            "content": "content",
            "start_date": "start_date",
            "start_time": "start_time",
            "end_date": "end_date",
            "end_time": "end_time",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_scheduleinfo_update', args=[scheduleinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TalkMemberViewTest(unittest.TestCase):
    '''
    Tests for TalkMember
    '''
    def setUp(self):
        self.client = Client()

    def test_list_talkmember(self):
        url = reverse('WebApp_talkmember_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_talkmember(self):
        url = reverse('WebApp_talkmember_create')
        data = {
            "member_code": "member_code",
            "use_flag": "use_flag",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_talkmember(self):
        talkmember = create_talkmember()
        url = reverse('WebApp_talkmember_detail', args=[talkmember.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_talkmember(self):
        talkmember = create_talkmember()
        data = {
            "member_code": "member_code",
            "use_flag": "use_flag",
        }
        url = reverse('WebApp_talkmember_update', args=[talkmember.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TalkMessageViewTest(unittest.TestCase):
    '''
    Tests for TalkMessage
    '''
    def setUp(self):
        self.client = Client()

    def test_list_talkmessage(self):
        url = reverse('WebApp_talkmessage_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_talkmessage(self):
        url = reverse('WebApp_talkmessage_create')
        data = {
            "talk_room_id": "talk_room_id",
            "message": "message",
            "sender_member_code": "sender_member_code",
            "send_date": "send_date",
            "send_time": "send_time",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_talkmessage(self):
        talkmessage = create_talkmessage()
        url = reverse('WebApp_talkmessage_detail', args=[talkmessage.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_talkmessage(self):
        talkmessage = create_talkmessage()
        data = {
            "talk_room_id": "talk_room_id",
            "message": "message",
            "sender_member_code": "sender_member_code",
            "send_date": "send_date",
            "send_time": "send_time",
        }
        url = reverse('WebApp_talkmessage_update', args=[talkmessage.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TalkMessageReadViewTest(unittest.TestCase):
    '''
    Tests for TalkMessageRead
    '''
    def setUp(self):
        self.client = Client()

    def test_list_talkmessageread(self):
        url = reverse('WebApp_talkmessageread_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_talkmessageread(self):
        url = reverse('WebApp_talkmessageread_create')
        data = {
            "member_code": "member_code",
            "is_read": "is_read",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_talkmessageread(self):
        talkmessageread = create_talkmessageread()
        url = reverse('WebApp_talkmessageread_detail', args=[talkmessageread.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_talkmessageread(self):
        talkmessageread = create_talkmessageread()
        data = {
            "member_code": "member_code",
            "is_read": "is_read",
        }
        url = reverse('WebApp_talkmessageread_update', args=[talkmessageread.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TalkRoomViewTest(unittest.TestCase):
    '''
    Tests for TalkRoom
    '''
    def setUp(self):
        self.client = Client()

    def test_list_talkroom(self):
        url = reverse('WebApp_talkroom_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_talkroom(self):
        url = reverse('WebApp_talkroom_create')
        data = {
            "talk_room_cate_code": "talk_room_cate_code",
            "lecture_code": "lecture_code",
            "inning_code": "inning_code",
            "use_flag": "use_flag",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_talkroom(self):
        talkroom = create_talkroom()
        url = reverse('WebApp_talkroom_detail', args=[talkroom.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_talkroom(self):
        talkroom = create_talkroom()
        data = {
            "talk_room_cate_code": "talk_room_cate_code",
            "lecture_code": "lecture_code",
            "inning_code": "inning_code",
            "use_flag": "use_flag",
        }
        url = reverse('WebApp_talkroom_update', args=[talkroom.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TodoInfoViewTest(unittest.TestCase):
    '''
    Tests for TodoInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_todoinfo(self):
        url = reverse('WebApp_todoinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_todoinfo(self):
        url = reverse('WebApp_todoinfo_create')
        data = {
            "chapter_code": "chapter_code",
            "member_code": "member_code",
            "todo_comment": "todo_comment",
            "todo_status": "todo_status",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "teacher_code": "teacher_code",
            "todo_title": "todo_title",
            "start_date": "start_date",
            "start_time": "start_time",
            "end_date": "end_date",
            "end_time": "end_time",
            "lecture_code": "lecture_code",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_todoinfo(self):
        todoinfo = create_todoinfo()
        url = reverse('WebApp_todoinfo_detail', args=[todoinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_todoinfo(self):
        todoinfo = create_todoinfo()
        data = {
            "chapter_code": "chapter_code",
            "member_code": "member_code",
            "todo_comment": "todo_comment",
            "todo_status": "todo_status",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
            "teacher_code": "teacher_code",
            "todo_title": "todo_title",
            "start_date": "start_date",
            "start_time": "start_time",
            "end_date": "end_date",
            "end_time": "end_time",
            "lecture_code": "lecture_code",
        }
        url = reverse('WebApp_todoinfo_update', args=[todoinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TodoTInfoViewTest(unittest.TestCase):
    '''
    Tests for TodoTInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_todotinfo(self):
        url = reverse('WebApp_todotinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_todotinfo(self):
        url = reverse('WebApp_todotinfo_create')
        data = {
            "todo_code": "todo_code",
            "member_code": "member_code",
            "todo_t_flag": "todo_t_flag",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_todotinfo(self):
        todotinfo = create_todotinfo()
        url = reverse('WebApp_todotinfo_detail', args=[todotinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_todotinfo(self):
        todotinfo = create_todotinfo()
        data = {
            "todo_code": "todo_code",
            "member_code": "member_code",
            "todo_t_flag": "todo_t_flag",
            "use_flag": "use_flag",
            "reg_date": "reg_date",
            "reg_time": "reg_time",
            "reg_agent": "reg_agent",
            "udt_date": "udt_date",
            "udt_time": "udt_time",
            "udt_agent": "udt_agent",
        }
        url = reverse('WebApp_todotinfo_update', args=[todotinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


