from datetime import datetime

from django.db.models import ForeignKey, CharField, IntegerField, DateTimeField, TextField, TimeField, BooleanField
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


# class Profile(models.Model):
#
#
#
#     class Meta:
#         ordering = ('-pk',)
#
#     def __unicode__(self):
#         return u'%s' % self.pk
#
#     def get_absolute_url(self):
#         return reverse('WebApp_profile_detail', args=(self.pk,))
#
#
#     def get_update_url(self):
#         return reverse('WebApp_profile_update', args=(self.pk,))


class CenterInfo(models.Model):

    # Fields
    Center_Name = CharField(max_length=500, blank=True, null=True)
    Center_Address = CharField(max_length=500, blank=True, null=True)
    Use_Flag = CharField(max_length=1, blank=True, null=True)
    Register_DateTime = DateTimeField(default=datetime.now(), blank=True)
    Register_Agent = CharField(max_length=200, blank=True, null=True)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_centerinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_centerinfo_update', args=(self.pk,))


class MemberInfo(models.Model):

    # Fields
    Member_ID = CharField(max_length=250, blank=True, null=True)
    Member_Password = CharField(max_length=250, blank=True, null=True)
    Member_Type = IntegerField(blank=True, null=True)
    Member_Name = CharField(max_length=500, blank=True, null=True)
    Member_Permanent_Address = CharField(max_length=500, blank=True, null=True)
    Member_Temporary_Address = CharField(max_length=500, blank=True, null=True)
    Member_BirthDate = CharField(max_length=50, blank=True, null=True)
    Member_Email = CharField(max_length=150, blank=True, null=True)
    Member_Phone = CharField(max_length=150, blank=True, null=True)
    member_Avatar = CharField(max_length=50, blank=True, null=True)
    member_Gender = IntegerField(blank=True, null=True)
    Use_Flag = CharField(max_length=1, blank=True, null=True)
    Register_DateTime = DateTimeField(default=datetime.now(), blank=True)
    Register_Agent = CharField(max_length=200, blank=True, null=True)
    Member_Memo = CharField(max_length=500, blank=True, null=True)

    # Relationship Fields
    center_code = ForeignKey(
        'WebApp.CenterInfo',
         related_name="memberinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_memberinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_memberinfo_update', args=(self.pk,))


class LectureInfo(models.Model):

    # Fields
    lecture_name = CharField(max_length=500, blank=True, null=True)
    lecture_teacher = IntegerField(blank=True, null=True)
    lecture_cover = CharField(max_length=250, blank=True, null=True)
    lecture_cover_file = CharField(max_length=250, blank=True, null=True)
    lecture_level = IntegerField(blank=True, null=True)
    lecture_info = TextField(blank=True, null=True)
    teacher = CharField(max_length=120, blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)
    lecture_certification = CharField(max_length=1, blank=True, null=True)
    lecture_provider = CharField(max_length=250, blank=True, null=True)
    cert_crit_prog = IntegerField(blank=True, null=True)
    cert_crit_post = IntegerField(blank=True, null=True)
    cert_crit_ubt = IntegerField(blank=True, null=True)
    cert_crit_issue = IntegerField(blank=True, null=True)

    # Relationship Fields
    center_code = ForeignKey(
        'WebApp.CenterInfo',
         related_name="lectureinfos", on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_lectureinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_lectureinfo_update', args=(self.pk,))


class ChapterInfo(models.Model):

    # Fields
    chapter_no = IntegerField(blank=True, null=True)
    chapter_name = CharField(max_length=200, blank=True, null=True)
    topic = TextField(blank=True, null=True)
    summary = TextField(blank=True, null=True)
    page_num = IntegerField(blank=True, null=True)
    vod_size = CharField(max_length=200, blank=True, null=True)
    intro = TextField(blank=True, null=True)
    target = TextField(blank=True, null=True)
    top_img = CharField(max_length=200, blank=True, null=True)
    bottom_img1 = CharField(max_length=200, blank=True, null=True)
    bottom_img2 = CharField(max_length=200, blank=True, null=True)
    bottom_img3 = CharField(max_length=200, blank=True, null=True)
    thum_file = CharField(max_length=200, blank=True, null=True)
    vod_file = CharField(max_length=200, blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=100, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=100, blank=True, null=True)
    today = TextField(blank=True, null=True)
    chapter_type = CharField(max_length=50, blank=True, null=True)
    prologue_type = CharField(max_length=50, blank=True, null=True)
    tabset = CharField(max_length=20, blank=True, null=True)
    chapter_image = CharField(max_length=100, blank=True, null=True)
    chapter_use = CharField(max_length=50, blank=True, null=True)
    offline_file = CharField(max_length=250, blank=True, null=True)
    pre_test_type = IntegerField(blank=True, null=True)
    post_test_type = IntegerField(blank=True, null=True)
    level1_avg = IntegerField(blank=True, null=True)
    level2_avg = IntegerField(blank=True, null=True)
    level3_avg = IntegerField(blank=True, null=True)
    level1_hard_avg = IntegerField(blank=True, null=True)
    level1_medium_avg = IntegerField(blank=True, null=True)
    level1_easy_avg = IntegerField(blank=True, null=True)
    level2_hard_avg = IntegerField(blank=True, null=True)
    level2_medium_avg = IntegerField(blank=True, null=True)
    level2_easy_avg = IntegerField(blank=True, null=True)
    level3_hard_avg = IntegerField(blank=True, null=True)
    level3_medium_avg = IntegerField(blank=True, null=True)
    level3_easy_avg = IntegerField(blank=True, null=True)
    homework_count = IntegerField(blank=True, null=True)
    epilogue_type = CharField(max_length=50, blank=True, null=True)
    epilogue_img = CharField(max_length=200, blank=True, null=True)
    pbl_flag = CharField(max_length=1, blank=True, null=True)
    chapter_use_time = TimeField(blank=True, null=True)

    # Relationship Fields
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="chapterinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_chapterinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_chapterinfo_update', args=(self.pk,))


class ChapterContentsInfo(models.Model):

    # Fields
    chapter_contents = CharField(max_length=250, blank=True, null=True)
    chapter_audio = CharField(max_length=250, blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)
    contents_index = IntegerField(blank=True, null=True)
    chapter_type = CharField(max_length=50, blank=True, null=True)
    thum_file = CharField(max_length=250, blank=True, null=True)
    vod_file = CharField(max_length=250, blank=True, null=True)
    today = TextField(blank=True, null=True)
    front1_img = CharField(max_length=150, blank=True, null=True)
    front1_text = TextField(blank=True, null=True)
    back1_img = CharField(max_length=150, blank=True, null=True)
    back1_text = TextField(blank=True, null=True)
    pdf_file = CharField(max_length=150, blank=True, null=True)
    front2_img = CharField(max_length=150, blank=True, null=True)
    front3_img = CharField(max_length=150, blank=True, null=True)
    front4_img = CharField(max_length=150, blank=True, null=True)
    front2_text = TextField(blank=True, null=True)
    front3_text = TextField(blank=True, null=True)
    front4_text = TextField(blank=True, null=True)
    back2_img = CharField(max_length=150, blank=True, null=True)
    back3_img = CharField(max_length=150, blank=True, null=True)
    back4_img = CharField(max_length=150, blank=True, null=True)
    back2_text = TextField(blank=True, null=True)
    back3_text = TextField(blank=True, null=True)
    back4_text = TextField(blank=True, null=True)
    c1_audio = CharField(max_length=150, blank=True, null=True)
    c2_audio = CharField(max_length=150, blank=True, null=True)
    c3_audio = CharField(max_length=150, blank=True, null=True)
    c4_audio = CharField(max_length=150, blank=True, null=True)
    vod_size = IntegerField(blank=True, null=True)
    offline_file = CharField(max_length=250, blank=True, null=True)
    teacher_guide = CharField(max_length=500, blank=True, null=True)
    today_text = CharField(max_length=500, blank=True, null=True)
    contents_text = TextField(blank=True, null=True)
    pbl_allow = CharField(max_length=1, blank=True, null=True)
    pbl_lec_allow = CharField(max_length=1, blank=True, null=True)

    # Relationship Fields
    chapter_code = ForeignKey(
        'WebApp.ChapterInfo',
         related_name="chaptercontentsinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_chaptercontentsinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_chaptercontentsinfo_update', args=(self.pk,))


class ChapterMissonCheckCard(models.Model):

    # Fields
    check_card_code = IntegerField(unique=True)
    use_flag = CharField(max_length=1)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    chapter_code = ForeignKey(
        'WebApp.ChapterInfo',
         related_name="chaptermissoncheckcards", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_chaptermissoncheckcard_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_chaptermissoncheckcard_update', args=(self.pk,))


class ChapterMissonCheckItem(models.Model):

    # Fields
    check_item_code = IntegerField(unique=True)
    item_text = TextField(blank=True, null=True)
    contents_text = TextField(blank=True, null=True)
    use_flag = CharField(max_length=1)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    check_card_code = ForeignKey(
        'WebApp.ChapterMissonCheckCard',
         related_name="chaptermissoncheckitems", on_delete=models.DO_NOTHING
    )
    chapter_contents_code = ForeignKey(
        'WebApp.ChapterContentsInfo',
         related_name="chaptermissoncheckitems", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_chaptermissoncheckitem_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_chaptermissoncheckitem_update', args=(self.pk,))


class InningInfo(models.Model):

    # Fields
    inning_name = CharField(max_length=500, blank=True, null=True)
    start_date = CharField(max_length=150, blank=True, null=True)
    end_date = CharField(max_length=150, blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="inninginfos", on_delete=models.DO_NOTHING
    )
    center_code = ForeignKey(
        'WebApp.CenterInfo',
         related_name="inninginfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_inninginfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_inninginfo_update', args=(self.pk,))


class OmrQuestionInfo(models.Model):

    # Fields
    subject_code = IntegerField(blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)
    question_level = IntegerField(blank=True, null=True)
    question_score = IntegerField(blank=True, null=True)

    # Relationship Fields
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="omrquestioninfos", on_delete=models.DO_NOTHING
    )
    chapter_code = ForeignKey(
        'WebApp.ChapterInfo',
         related_name="omrquestioninfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_omrquestioninfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_omrquestioninfo_update', args=(self.pk,))


class QuizInfo(models.Model):

    # Fields
    subject_code = IntegerField(blank=True, null=True)
    quiz_type = CharField(max_length=50, blank=True, null=True)
    quiz_question = CharField(max_length=1000, blank=True, null=True)
    quiz_media_type = CharField(max_length=10, blank=True, null=True)
    quiz_media_file = CharField(max_length=200, blank=True, null=True)
    quiz_score = IntegerField(blank=True, null=True)
    quiz_comment = CharField(max_length=1000, blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)
    quiz_head = CharField(max_length=1000, blank=True, null=True)
    quiz_media_file2 = CharField(max_length=250, blank=True, null=True)

    # Relationship Fields
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="quizinfos", on_delete=models.DO_NOTHING
    )
    chapter_code = ForeignKey(
        'WebApp.ChapterInfo',
         related_name="quizinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_quizinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_quizinfo_update', args=(self.pk,))


class AssignHomeworkInfo(models.Model):

    # Fields
    subject_code = IntegerField(blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    question_code = ForeignKey(
        'WebApp.OmrQuestionInfo',
         related_name="assignhomeworkinfos", on_delete=models.DO_NOTHING
    )
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="assignhomeworkinfos", on_delete=models.DO_NOTHING
    )
    chapter_code = ForeignKey(
        'WebApp.ChapterInfo',
         related_name="assignhomeworkinfos", on_delete=models.DO_NOTHING
    )
    member_code = ForeignKey(
        'WebApp.MemberInfo',
         related_name="assignhomeworkinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_assignhomeworkinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_assignhomeworkinfo_update', args=(self.pk,))


class AssignQuestionInfo(models.Model):

    # Fields
    subject_code = IntegerField(blank=True, null=True)
    question_type = CharField(max_length=20, blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    question_code = ForeignKey(
        'WebApp.OmrQuestionInfo',
         related_name="assignquestioninfos", on_delete=models.DO_NOTHING
    )
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="assignquestioninfos", on_delete=models.DO_NOTHING
    )
    chapter_code = ForeignKey(
        'WebApp.ChapterInfo',
         related_name="assignquestioninfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_assignquestioninfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_assignquestioninfo_update', args=(self.pk,))


class BoardInfo(models.Model):

    # Fields
    board_name = CharField(max_length=500, blank=True, null=True)
    board_write_level = CharField(max_length=2, blank=True, null=True)
    board_read_level = CharField(max_length=2, blank=True, null=True)
    board_reply_level = CharField(max_length=2, blank=True, null=True)
    board_new_time = IntegerField(blank=True, null=True)
    board_create_time = CharField(max_length=16, blank=True, null=True)
    admin_id = CharField(max_length=20, blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_boardinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_boardinfo_update', args=(self.pk,))


class BoardContentInfo(models.Model):

    # Fields
    admin_id = CharField(max_length=200, blank=True, null=True)
    title = CharField(max_length=5000, blank=True, null=True)
    contents = CharField(max_length=5000, blank=True, null=True)
    writer = CharField(max_length=200, blank=True, null=True)
    view_cnt = IntegerField(blank=True, null=True)
    ref_code = IntegerField(blank=True, null=True)
    ref_step = CharField(max_length=16, blank=True, null=True)
    ref_level = IntegerField(blank=True, null=True)
    write_time = CharField(max_length=18, blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    board_code = ForeignKey(
        'WebApp.BoardInfo',
         related_name="boardcontentinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_boardcontentinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_boardcontentinfo_update', args=(self.pk,))


class InningGroup(models.Model):

    # Fields
    teacher_code = IntegerField(blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    center_code = ForeignKey(
        'WebApp.CenterInfo',
         related_name="inninggroups", on_delete=models.DO_NOTHING
    )
    inning_code = ForeignKey(
        'WebApp.InningInfo',
         related_name="inninggroups", on_delete=models.DO_NOTHING
    )
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="inninggroups", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_inninggroup_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_inninggroup_update', args=(self.pk,))


class ChapterContentMedia(models.Model):

    # Fields
    media_type = CharField(max_length=10)
    media_desc = TextField(blank=True, null=True)
    media_filename = CharField(max_length=255)
    use_flag = CharField(max_length=1)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    chapter_contents_code = ForeignKey(
        'WebApp.ChapterContentsInfo',
         related_name="chaptercontentmedias", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_chaptercontentmedia_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_chaptercontentmedia_update', args=(self.pk,))


class ChapterImgInfo(models.Model):

    # Fields
    filename = CharField(max_length=150, blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    chapter_code = ForeignKey(
        'WebApp.ChapterInfo',
         related_name="chapterimginfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_chapterimginfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_chapterimginfo_update', args=(self.pk,))


class ChapterMissonCheck(models.Model):

    # Fields
    check_code = IntegerField(unique=True)
    student_code = IntegerField()
    check_agent_code = IntegerField()
    is_check_yn = CharField(max_length=1)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    check_item_code = ForeignKey(
        'WebApp.ChapterMissonCheckItem',
         related_name="chaptermissonchecks", on_delete=models.DO_NOTHING
    )
    inning_code = ForeignKey(
        'WebApp.InningInfo',
         related_name="chaptermissonchecks", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_chaptermissoncheck_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_chaptermissoncheck_update', args=(self.pk,))


class ChapterWrite(models.Model):

    # Fields
    student_code = IntegerField(blank=True, null=True)
    write_content = TextField(blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    inning_code = ForeignKey(
        'WebApp.InningInfo',
         related_name="chapterwrites", on_delete=models.DO_NOTHING
    )
    chapter_contents_code = ForeignKey(
        'WebApp.ChapterContentsInfo',
         related_name="chapterwrites", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_chapterwrite_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_chapterwrite_update', args=(self.pk,))


class GroupMapping(models.Model):

    # Fields
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    center_code = ForeignKey(
        'WebApp.CenterInfo',
         related_name="groupmappings", on_delete=models.DO_NOTHING
    )
    group_code = ForeignKey(
        'WebApp.InningGroup',
         related_name="groupmappings", on_delete=models.DO_NOTHING
    )
    member_code = ForeignKey(
        'WebApp.MemberInfo',
         related_name="groupmappings", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_groupmapping_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_groupmapping_update', args=(self.pk,))


class HomeworkInfo(models.Model):

    # Fields
    subject_code = IntegerField(blank=True, null=True)
    level_score = IntegerField(blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    level = IntegerField(blank=True, null=True)

    # Relationship Fields
    question_code = ForeignKey(
        'WebApp.OmrQuestionInfo',
         related_name="homeworkinfos", on_delete=models.DO_NOTHING
    )
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="homeworkinfos", on_delete=models.DO_NOTHING
    )
    chapter_code = ForeignKey(
        'WebApp.ChapterInfo',
         related_name="homeworkinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_homeworkinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_homeworkinfo_update', args=(self.pk,))


class LearningNote(models.Model):

    # Fields
    contents_code = IntegerField()
    note_contents = TextField(blank=True, null=True)
    note_attachment = CharField(max_length=250, blank=True, null=True)

    # Relationship Fields
    inning_code = ForeignKey(
        'WebApp.InningInfo',
         related_name="learningnotes", on_delete=models.DO_NOTHING
    )
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="learningnotes", on_delete=models.DO_NOTHING
    )
    chapter_code = ForeignKey(
        'WebApp.ChapterInfo',
         related_name="learningnotes", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_learningnote_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_learningnote_update', args=(self.pk,))


class LectureUbtInfo(models.Model):

    # Fields
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    quiz_code = ForeignKey(
        'WebApp.QuizInfo',
         related_name="lectureubtinfos", on_delete=models.DO_NOTHING
    )
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="lectureubtinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_lectureubtinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_lectureubtinfo_update', args=(self.pk,))


class LessonInfo(models.Model):

    # Fields
    teacher_code = IntegerField(blank=True, null=True)
    start_date = CharField(max_length=150, blank=True, null=True)
    end_date = CharField(max_length=150, blank=True, null=True)
    progress = CharField(max_length=150, blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)
    ubt_start = CharField(max_length=50, blank=True, null=True)
    ubt_end = CharField(max_length=50, blank=True, null=True)
    download_count = IntegerField(blank=True, null=True)
    download_date = CharField(max_length=19, blank=True, null=True)

    # Relationship Fields
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="lessoninfos", on_delete=models.DO_NOTHING
    )
    member_code = ForeignKey(
        'WebApp.MemberInfo',
         related_name="lessoninfos", on_delete=models.DO_NOTHING
    )
    center_code = ForeignKey(
        'WebApp.CenterInfo',
         related_name="lessoninfos", on_delete=models.DO_NOTHING
    )
    inning_code = ForeignKey(
        'WebApp.InningInfo',
         related_name="lessoninfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_lessoninfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_lessoninfo_update', args=(self.pk,))


class LessonLog(models.Model):

    # Fields
    member_id = CharField(max_length=250, blank=True, null=True)
    member_ip = CharField(max_length=500, blank=True, null=True)
    member_browser = CharField(max_length=150, blank=True, null=True)
    member_os = CharField(max_length=150, blank=True, null=True)
    start_date = CharField(max_length=50, blank=True, null=True)
    start_time = CharField(max_length=50, blank=True, null=True)
    end_date = CharField(max_length=150, blank=True, null=True)
    end_time = CharField(max_length=150, blank=True, null=True)
    connect_date = CharField(max_length=50, blank=True, null=True)
    connect_time = CharField(max_length=50, blank=True, null=True)
    connect_count = IntegerField(blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)
    study_time = IntegerField(blank=True, null=True)
    connect_page = IntegerField(blank=True, null=True)

    # Relationship Fields
    lesson_code = ForeignKey(
        'WebApp.LessonInfo',
         related_name="lessonlogs", on_delete=models.DO_NOTHING
    )
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="lessonlogs", on_delete=models.DO_NOTHING
    )
    chapter_code = ForeignKey(
        'WebApp.ChapterInfo',
         related_name="lessonlogs", on_delete=models.DO_NOTHING
    )
    member_code = ForeignKey(
        'WebApp.MemberInfo',
         related_name="lessonlogs", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_lessonlog_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_lessonlog_update', args=(self.pk,))


class MemberGroup(models.Model):

    # Fields
    group_name = CharField(max_length=500, blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    center_code = ForeignKey(
        'WebApp.CenterInfo',
         related_name="membergroups", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_membergroup_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_membergroup_update', args=(self.pk,))


class MessageInfo(models.Model):

    # Fields
    teacher_code = IntegerField(blank=True, null=True)
    message = CharField(max_length=4000, blank=True, null=True)
    message_read = CharField(max_length=1, blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    member_code = ForeignKey(
        'WebApp.MemberInfo',
         related_name="messageinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_messageinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_messageinfo_update', args=(self.pk,))


class OmrAnswerInfo(models.Model):

    # Fields
    subject_code = IntegerField(blank=True, null=True)
    omr_answer = IntegerField(blank=True, null=True)
    omr_answer_idx = IntegerField(blank=True, null=True)
    omr_answer_correct = CharField(max_length=200, blank=True, null=True)
    question_score = IntegerField(blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="omranswerinfos", on_delete=models.DO_NOTHING
    )
    chapter_code = ForeignKey(
        'WebApp.ChapterInfo',
         related_name="omranswerinfos", on_delete=models.DO_NOTHING
    )
    member_code = ForeignKey(
        'WebApp.MemberInfo',
         related_name="omranswerinfos", on_delete=models.DO_NOTHING
    )
    question_code = ForeignKey(
        'WebApp.OmrQuestionInfo',
         related_name="omranswerinfos", on_delete=models.DO_NOTHING
    )
    lesson_code = ForeignKey(
        'WebApp.LessonInfo',
         related_name="omranswerinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_omranswerinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_omranswerinfo_update', args=(self.pk,))


class OmrAssignInfo(models.Model):

    # Fields
    subject_code = IntegerField(blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    question_code = ForeignKey(
        'WebApp.OmrQuestionInfo',
         related_name="omrassigninfos", on_delete=models.DO_NOTHING
    )
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="omrassigninfos", on_delete=models.DO_NOTHING
    )
    chapter_code = ForeignKey(
        'WebApp.ChapterInfo',
         related_name="omrassigninfos", on_delete=models.DO_NOTHING
    )
    member_code = ForeignKey(
        'WebApp.MemberInfo',
         related_name="omrassigninfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_omrassigninfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_omrassigninfo_update', args=(self.pk,))


class OmrExampleInfo(models.Model):

    # Fields
    omr_example_correct = CharField(max_length=1, blank=True, null=True)
    omr_example_idx = IntegerField(blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    question_code = ForeignKey(
        'WebApp.OmrQuestionInfo',
         related_name="omrexampleinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_omrexampleinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_omrexampleinfo_update', args=(self.pk,))


class QAnswerInfo(models.Model):

    # Fields
    subject_code = IntegerField(blank=True, null=True)
    question_type = CharField(max_length=10, blank=True, null=True)
    question_answer = CharField(max_length=200, blank=True, null=True)
    question_idx = IntegerField(blank=True, null=True)
    question_correct = CharField(max_length=200, blank=True, null=True)
    question_score = IntegerField(blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=10, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=10, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="qanswerinfos", on_delete=models.DO_NOTHING
    )
    chapter_code = ForeignKey(
        'WebApp.ChapterInfo',
         related_name="qanswerinfos", on_delete=models.DO_NOTHING
    )
    member_code = ForeignKey(
        'WebApp.MemberInfo',
         related_name="qanswerinfos", on_delete=models.DO_NOTHING
    )
    question_code = ForeignKey(
        'WebApp.OmrQuestionInfo',
         related_name="qanswerinfos", on_delete=models.DO_NOTHING
    )
    lesson_code = ForeignKey(
        'WebApp.LessonInfo',
         related_name="qanswerinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_qanswerinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_qanswerinfo_update', args=(self.pk,))


class QAnswerLog(models.Model):

    # Fields
    question_answer = CharField(max_length=250, blank=True, null=True)
    question_idx = CharField(max_length=250, blank=True, null=True)
    question_score = IntegerField(blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="qanswerlogs", on_delete=models.DO_NOTHING
    )
    member_code = ForeignKey(
        'WebApp.MemberInfo',
         related_name="qanswerlogs", on_delete=models.DO_NOTHING
    )
    question_code = ForeignKey(
        'WebApp.OmrQuestionInfo',
         related_name="qanswerlogs", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_qanswerlog_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_qanswerlog_update', args=(self.pk,))


class QExampleInfo(models.Model):

    # Fields
    q_example = CharField(max_length=1000, blank=True, null=True)
    q_example_correct = CharField(max_length=10, blank=True, null=True)
    q_example_idx = IntegerField(blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)
    q_example_type = CharField(max_length=50, blank=True, null=True)

    # Relationship Fields
    question_code = ForeignKey(
        'WebApp.OmrQuestionInfo',
         related_name="qexampleinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_qexampleinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_qexampleinfo_update', args=(self.pk,))


class QuestionInfo(models.Model):

    # Fields
    subject_code = IntegerField(blank=True, null=True)
    question_type = CharField(max_length=10, blank=True, null=True)
    question = CharField(max_length=4000, blank=True, null=True)
    question_media_type = CharField(max_length=10, blank=True, null=True)
    question_media_file = CharField(max_length=200, blank=True, null=True)
    question_score = IntegerField(blank=True, null=True)
    question_head = CharField(max_length=2000, blank=True, null=True)
    question_essay = CharField(max_length=500, blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)
    question_media_file2 = CharField(max_length=250, blank=True, null=True)
    question_comment = TextField(blank=True, null=True)
    question_level = IntegerField(blank=True, null=True)
    teacher_contents = CharField(max_length=500, blank=True, null=True)
    student_contents = CharField(max_length=500, blank=True, null=True)

    # Relationship Fields
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="questioninfos", on_delete=models.DO_NOTHING
    )
    chapter_code = ForeignKey(
        'WebApp.ChapterInfo',
         related_name="questioninfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_questioninfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_questioninfo_update', args=(self.pk,))


class QuizAnswerInfo(models.Model):

    # Fields
    subject_code = IntegerField(blank=True, null=True)
    quiz_type = CharField(max_length=50, blank=True, null=True)
    quiz_answer = IntegerField(blank=True, null=True)
    quiz_answer_idx = IntegerField(blank=True, null=True)
    quiz_correct = CharField(max_length=50, blank=True, null=True)
    quiz_score = IntegerField(blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)
    test_type = IntegerField(blank=True, null=True)

    # Relationship Fields
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="quizanswerinfos", on_delete=models.DO_NOTHING
    )
    chapter_code = ForeignKey(
        'WebApp.ChapterInfo',
         related_name="quizanswerinfos", on_delete=models.DO_NOTHING
    )
    member_code = ForeignKey(
        'WebApp.MemberInfo',
         related_name="quizanswerinfos", on_delete=models.DO_NOTHING
    )
    quiz_code = ForeignKey(
        'WebApp.QuizInfo',
         related_name="quizanswerinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_quizanswerinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_quizanswerinfo_update', args=(self.pk,))


class QuizExampleInfo(models.Model):

    # Fields
    quiz_example = CharField(max_length=1000, blank=True, null=True)
    quiz_example_correct = CharField(max_length=10, blank=True, null=True)
    quiz_example_idx = IntegerField(blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)
    quiz_example_type = CharField(max_length=50, blank=True, null=True)

    # Relationship Fields
    quiz_code = ForeignKey(
        'WebApp.QuizInfo',
         related_name="quizexampleinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_quizexampleinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_quizexampleinfo_update', args=(self.pk,))


class ScheduleInfo(models.Model):

    # Fields
    title = CharField(max_length=500, blank=True, null=True)
    content = CharField(max_length=2000, blank=True, null=True)
    start_date = CharField(max_length=10, blank=True, null=True)
    start_time = CharField(max_length=8, blank=True, null=True)
    end_date = CharField(max_length=10, blank=True, null=True)
    end_time = CharField(max_length=8, blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    member_code = ForeignKey(
        'WebApp.MemberInfo',
         related_name="scheduleinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_scheduleinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_scheduleinfo_update', args=(self.pk,))


class TalkMember(models.Model):

    # Fields
    use_flag = BooleanField(blank=True, null=True)

    # Relationship Fieldspro
    member_code = ForeignKey(
        'WebApp.MemberInfo',
         related_name="talkmembers", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_talkmember_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_talkmember_update', args=(self.pk,))


class TalkRoom(models.Model):

    # Fields
    talk_room_cate_code = CharField(max_length=10)
    use_flag = BooleanField(blank=True, null=True)

    # Relationship Fields
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="talkrooms", on_delete=models.DO_NOTHING
    )
    inning_code = ForeignKey(
        'WebApp.InningInfo',
         related_name="talkrooms", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_talkroom_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_talkroom_update', args=(self.pk,))


class TalkMessage(models.Model):

    # Fields
    message = CharField(max_length=5000, blank=True, null=True)
    sender_member_code = IntegerField(blank=True, null=True)
    send_date = CharField(max_length=10, blank=True, null=True)
    send_time = CharField(max_length=8, blank=True, null=True)

    # Relationship Fields
    talk_room_id = ForeignKey(
        'WebApp.TalkRoom',
         related_name="talkmessages", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_talkmessage_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_talkmessage_update', args=(self.pk,))


class TalkMessageRead(models.Model):

    # Fields
    is_read = BooleanField()

    # Relationship Fields
    member_code = ForeignKey(
        'WebApp.MemberInfo',
         related_name="talkmessagereads", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_talkmessageread_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_talkmessageread_update', args=(self.pk,))


class TodoInfo(models.Model):

    # Fields
    todo_comment = CharField(max_length=4000, blank=True, null=True)
    todo_status = CharField(max_length=1, blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)
    teacher_code = IntegerField(blank=True, null=True)
    todo_title = CharField(max_length=500, blank=True, null=True)
    start_date = CharField(max_length=50, blank=True, null=True)
    start_time = CharField(max_length=50, blank=True, null=True)
    end_date = CharField(max_length=50, blank=True, null=True)
    end_time = CharField(max_length=50, blank=True, null=True)

    # Relationship Fields
    chapter_code = ForeignKey(
        'WebApp.ChapterInfo',
         related_name="todoinfos", on_delete=models.DO_NOTHING
    )
    member_code = ForeignKey(
        'WebApp.MemberInfo',
         related_name="todoinfos", on_delete=models.DO_NOTHING
    )
    lecture_code = ForeignKey(
        'WebApp.LectureInfo',
         related_name="todoinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_todoinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_todoinfo_update', args=(self.pk,))


class TodoTInfo(models.Model):

    # Fields
    todo_code = IntegerField(blank=True, null=True)
    todo_t_flag = CharField(max_length=10, blank=True, null=True)
    use_flag = CharField(max_length=1, blank=True, null=True)
    reg_date = CharField(max_length=10, blank=True, null=True)
    reg_time = CharField(max_length=8, blank=True, null=True)
    reg_agent = CharField(max_length=200, blank=True, null=True)
    udt_date = CharField(max_length=10, blank=True, null=True)
    udt_time = CharField(max_length=8, blank=True, null=True)
    udt_agent = CharField(max_length=200, blank=True, null=True)

    # Relationship Fields
    member_code = ForeignKey(
        'WebApp.MemberInfo',
         related_name="todotinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('WebApp_todotinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('WebApp_todotinfo_update', args=(self.pk,))


