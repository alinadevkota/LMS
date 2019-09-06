from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.contenttypes.models import ContentType
from django.core.files.storage import FileSystemStorage
from django.db import models as models
from django.db.models import ForeignKey, CharField, IntegerField, DateTimeField, TextField, BooleanField, \
    ImageField, FileField
from django.urls import reverse
from django.utils.translation import gettext as _

fs = FileSystemStorage(location='LMS')


class CenterInfo(models.Model):
    # Fields
    Center_Name = CharField(max_length=500, blank=True, null=True)
    Center_Address = CharField(max_length=500, blank=True, null=True)
    Use_Flag = BooleanField(default=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.Center_Name

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('centerinfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('centerinfo_update', args=(self.pk,))

    def get_delete_url(self):
        return reverse('centerinfo_delete', args=(self.pk,))


USER_ROLES = (
    ('CenterAdmin', 'CenterAdmin'),
    ('Teacher', 'Teacher'),
    ('Student', 'Student'),
    ('Parent', 'Parent'),
)


class MemberInfo(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=True,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    is_superuser = models.BooleanField(
        _('is_superuser status'),
        default=True,
        help_text=_('Designates whether the user is superuser'),
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    # Fields
    # Member_ID = models.CharField(max_length=250, blank=True, null=True)
    password = models.CharField(_('password'), max_length=128)
    # remove this password field
    # Member_Password = models.CharField(max_length=250, blank=True, null=True)
    # Member_Type = models.IntegerField(blank=True, null=True)
    # Member_Name = models.CharField(max_length=500, blank=True, null=True)
    Member_Permanent_Address = models.CharField(max_length=500, blank=True, null=True)
    Member_Temporary_Address = models.CharField(max_length=500, blank=True, null=True)
    Member_BirthDate = models.DateTimeField(blank=True, null=True)
    # Member_Email = models.CharField(max_length=150, blank=True, null=True)
    Member_Phone = models.CharField(max_length=150, blank=True, null=True)
    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Member_Memo = models.CharField(max_length=500, blank=True, null=True)
    Member_Avatar = models.ImageField(upload_to="Member_images/", blank=True, null=True, default='Images/ubl_logo.jpg')

    Is_Teacher = models.BooleanField(default=False)
    Is_Student = models.BooleanField(default=False)
    Is_CenterAdmin = models.BooleanField(default=False)
    Is_Parent = models.BooleanField(default=False)
    Gender_Choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    Member_Gender = models.CharField(max_length=1, choices=Gender_Choices)


    # Member_Role = models.CharField(max_length=30, default="Student")

    # Relationship Fields
    Center_Code = ForeignKey(
        'CenterInfo',
        related_name="memberinfos", on_delete=models.DO_NOTHING, null=True
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('memberinfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('memberinfo_update', args=(self.pk,))

    # def create_user(self, username, email=None, password=None, **extra_fields):
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    #     return self._create_user(username, email, password, **extra_fields)


class LectureInfo(models.Model):
    # Fields
    Lecture_Name = CharField(max_length=500, blank=True, null=True)
    Lecture_Description = TextField(blank=True, null=True)
    Lecture_Cover_File = ImageField(upload_to="Lecture_images/", blank=True, null=True, default='Images/course.jpg')
    Lecture_Level = IntegerField(blank=True, null=True)
    Lecture_Info = TextField(blank=True, null=True)
    # teacher = CharField(max_length=120, blank=True, null=True)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    # Lecture_Certification = CharField(max_length=1, blank=True, null=True)
    Lecture_Provider = CharField(max_length=250, blank=True, null=True)
    # cert_crit_prog = IntegerField(blank=True, null=True)
    # cert_crit_post = IntegerField(blank=True, null=True)
    # cert_crit_ubt = IntegerField(blank=True, null=True)
    # cert_crit_issue = IntegerField(blank=True, null=True)

    # Relationship Fields
    Center_Code = ForeignKey(
        'CenterInfo',
        related_name="lectureinfos", on_delete=models.DO_NOTHING)

    # Teacher_Code = ForeignKey(
    #     'MemberInfo',
    #     related_name="lectureinfos", on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def student_get_absolute_url(self):
        return reverse('student_lectureinfo_detail', args=(self.pk,))

    def get_absolute_url(self):
        return reverse('lectureinfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('lectureinfo_update', args=(self.pk,))

    def __str__(self):
        return self.Lecture_Name


class ChapterInfo(models.Model):
    # Fields
    Chapter_No = IntegerField(blank=True, null=True)
    Chapter_Name = CharField(max_length=200, blank=True, null=True)
    # topic = TextField(blank=True, null=True)
    Summary = TextField(blank=True, null=True)
    Page_Num = IntegerField(blank=True, null=True)
    # vod_size = CharField(max_length=200, blank=True, null=True)
    # intro = TextField(blank=True, null=True)
    # target = TextField(blank=True, null=True)
    # top_img = CharField(max_length=200, blank=True, null=True)
    # bottom_img1 = CharField(max_length=200, blank=True, null=True)
    # bottom_img2 = CharField(max_length=200, blank=True, null=True)
    # bottom_img3 = CharField(max_length=200, blank=True, null=True)
    # thum_file = CharField(max_length=200, blank=True, null=True)
    # vod_file = CharField(max_length=200, blank=True, null=True)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    # today = TextField(blank=True, null=True)
    # chapter_type = CharField(max_length=50, blank=True, null=True)
    # prologue_type = CharField(max_length=50, blank=True, null=True)
    # tabset = CharField(max_length=20, blank=True, null=True)
    # chapter_image = CharField(max_length=100, blank=True, null=True)
    # chapter_use = CharField(max_length=50, blank=True, null=True)
    # offline_file = CharField(max_length=250, blank=True, null=True)
    # pre_test_type = IntegerField(blank=True, null=True)
    # post_test_type = IntegerField(blank=True, null=True)
    # level1_avg = IntegerField(blank=True, null=True)
    # level2_avg = IntegerField(blank=True, null=True)
    # level3_avg = IntegerField(blank=True, null=True)
    # level1_hard_avg = IntegerField(blank=True, null=True)
    # level1_medium_avg = IntegerField(blank=True, null=True)
    # level1_easy_avg = IntegerField(blank=True, null=True)
    # level2_hard_avg = IntegerField(blank=True, null=True)
    # level2_medium_avg = IntegerField(blank=True, null=True)
    # level2_easy_avg = IntegerField(blank=True, null=True)
    # level3_hard_avg = IntegerField(blank=True, null=True)
    # level3_medium_avg = IntegerField(blank=True, null=True)
    # level3_easy_avg = IntegerField(blank=True, null=True)
    # homework_count = IntegerField(blank=True, null=True)
    # epilogue_type = CharField(max_length=50, blank=True, null=True)
    # epilogue_img = CharField(max_length=200, blank=True, null=True)
    # pbl_flag = CharField(max_length=1, blank=True, null=True)
    # chapter_use_time = TimeField(blank=True, null=True)

    # Relationship Fields
    Lecture_Code = ForeignKey(
        'LectureInfo',
        related_name="chapterinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def student_get_absolute_url(self):
        return reverse('student_chapterinfo_detail', args=(self.Lecture_Code.id, self.pk,))

    def get_absolute_url(self):
        return reverse('chapterinfo_detail', args=(self.Lecture_Code.id, self.pk,))

    def get_update_url(self):
        return reverse('chapterinfo_update', args=(self.Lecture_Code.id, self.pk,))

    def __str__(self):
        return self.Chapter_Name


class ChapterContentsInfo(models.Model):
    # Fields
    # chapter_contents = CharField(max_length=250, blank=True, null=True)
    # chapter_audio = CharField(max_length=250, blank=True, null=True)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)
    Content_Description = TextField(blank=True, null=True)
    # contents_index = IntegerField(blank=True, null=True)
    # chapter_type = CharField(max_length=50, blank=True, null=True)
    # thum_file = CharField(max_length=250, blank=True, null=True)
    # vod_file = CharField(max_length=250, blank=True, null=True)
    # today = TextField(blank=True, null=True)
    # front1_img = CharField(max_length=150, blank=True, null=True)
    # front1_text = TextField(blank=True, null=True)
    # back1_img = CharField(max_length=150, blank=True, null=True)
    # back1_text = TextField(blank=True, null=True)
    # pdf_file = CharField(max_length=150, blank=True, null=True)
    # front2_img = CharField(max_length=150, blank=True, null=True)
    # front3_img = CharField(max_length=150, blank=True, null=True)
    # front4_img = CharField(max_length=150, blank=True, null=True)
    # front2_text = TextField(blank=True, null=True)
    # front3_text = TextField(blank=True, null=True)
    # front4_text = TextField(blank=True, null=True)
    # back2_img = CharField(max_length=150, blank=True, null=True)
    # back3_img = CharField(max_length=150, blank=True, null=True)
    # back4_img = CharField(max_length=150, blank=True, null=True)
    # back2_text = TextField(blank=True, null=True)
    # back3_text = TextField(blank=True, null=True)
    # back4_text = TextField(blank=True, null=True)
    # c1_audio = CharField(max_length=150, blank=True, null=True)
    # c2_audio = CharField(max_length=150, blank=True, null=True)
    # c3_audio = CharField(max_length=150, blank=True, null=True)
    # c4_audio = CharField(max_length=150, blank=True, null=True)
    # vod_size = IntegerField(blank=True, null=True)
    # offline_file = CharField(max_length=250, blank=True, null=True)
    # teacher_guide = CharField(max_length=500, blank=True, null=True)
    # today_text = CharField(max_length=500, blank=True, null=True)
    # contents_text = TextField(blank=True, null=True)
    # pbl_allow = CharField(max_length=1, blank=True, null=True)
    # pbl_lec_allow = CharField(max_length=1, blank=True, null=True)

    # Relationship Fields
    Chapter_Code = ForeignKey(
        'ChapterInfo',
        related_name="chaptercontentsinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('chaptercontentsinfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('chaptercontentsinfo_update', args=(self.pk,))


# class HomeworkInfo(models.Model):
#     Homework_Topic = CharField(max_length=500, blank=True, null=True)
#     Use_Flag = BooleanField(default=True)
#     Register_DateTime = DateTimeField(auto_now_add=True)
#     Updated_DateTime = DateTimeField(auto_now=True)
#     Register_Agent = CharField(max_length=500, blank=True, null=True)
#
#     Chapter_Code = ForeignKey(
#         'ChapterInfo',
#         related_name="homeworkinfos", on_delete=models.DO_NOTHING
#     )
#
#     def __str__(self):
#         return self.Homework_Topic


# AssignmentModels
class AssignmentInfo(models.Model):
    Assignment_Topic = CharField(max_length=500, blank=True, null=True)
    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Assignment_Deadline = DateTimeField(null=True, blank=True)
    Lecture_Code = ForeignKey(
        'LectureInfo',
        related_name="assignmentinfos", on_delete=models.DO_NOTHING
    )
    Chapter_Code = ForeignKey(
        'ChapterInfo',
        related_name="assignmentinfos", on_delete=models.DO_NOTHING
    )
    Register_Agent = ForeignKey(
        'MemberInfo',
        related_name="assignmentinfos", on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.Assignment_Topic

    def student_get_absolute_url(self):
        return reverse('student_assignmentinfo_detail', args=(self.Lecture_Code.id, self.Chapter_Code.id, self.pk,))

    def get_absolute_url(self):
        return reverse('assignmentinfo_detail', args=(self.Lecture_Code.id, self.Chapter_Code.id, self.pk,))

    def get_update_url(self):
        return reverse('assignmentinfo_update', args=(self.Lecture_Code.id, self.Chapter_Code.id, self.pk,))


def upload_to(instance, filename):
    return 'questions/{0}/{1}'.format(instance.id, filename)


class QuestionInfo(models.Model):
    # Fields
    # subject_code = IntegerField(blank=True, null=True)
    # question_type = CharField(max_length=10, blank=True, null=True)
    Question_Title = CharField(max_length=4000)
    # question_media_type = CharField(max_length=10, blank=True, null=True)
    # question_media_file = CharField(max_length=200, blank=True, null=True)
    Question_Score = IntegerField(blank=True, null=True)
    # question_head = CharField(max_length=2000, blank=True, null=True)
    # question_essay = CharField(max_length=500, blank=True, null=True)
    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)

    Question_Media_File = FileField(upload_to=upload_to, blank=True, null=True)
    Question_Description = TextField()
    Answer_Choices = (
        ('S', 'Short Answer'),
        ('F', 'File Upload'),
    )
    Answer_Type = CharField(max_length=1, choices=Answer_Choices)

    # question_level = IntegerField(blank=True, null=True)
    # teacher_contents = CharField(max_length=500, blank=True, null=True)
    # student_contents = CharField(max_length=500, blank=True, null=True)

    # Relationship Fields
    # Lecture_Code = ForeignKey(
    #     'LectureInfo',
    #     related_name="questioninfos", on_delete=models.DO_NOTHING
    # )
    # Chapter_Code = ForeignKey(
    #     'ChapterInfo',
    #     related_name="questioninfos", on_delete=models.DO_NOTHING
    # )
    #
    Assignment_Code = ForeignKey(
        'AssignmentInfo',
        related_name="questioninfos", on_delete=models.DO_NOTHING
    )

    Register_Agent = ForeignKey(
        'MemberInfo',
        related_name="questioninfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('questioninfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('questioninfo_update', args=(self.pk,))


class AssignAssignmentInfo(models.Model):
    # Fields
    # Subject_code = IntegerField(blank=True, null=True)
    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)

    # Relationship Fields
    Inning_Code = ForeignKey(
        'InningInfo',
        related_name="assignassignmentinfos", on_delete=models.DO_NOTHING
    )
    Assignment_Code = ForeignKey(
        'AssignmentInfo',
        related_name="assignassignmentinfos", on_delete=models.DO_NOTHING
    )
    Assigned_By = ForeignKey(
        'MemberInfo',
        related_name="assignassignmentinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('assignassignmentinfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('assignassignmentinfo_update', args=(self.pk,))


# class AssignQuestionInfo(models.Model):
#     # Fields
#     # subject_code = IntegerField(blank=True, null=True)
#     # question_type = CharField(max_length=20, blank=True, null=True)
#     Use_Flag = BooleanField(default=True)
#     Register_DateTime = DateTimeField(auto_now_add=True)
#     Updated_DateTime = DateTimeField(auto_now=True)
#     # Register_Agent = CharField(max_length=500, blank=True, null=True)
#
#     # Relationship Fields
#     Question_Code = ForeignKey(
#         'QuestionInfo',
#         related_name="assignquestioninfos", on_delete=models.DO_NOTHING
#     )
#     Assignment_Code = ForeignKey(
#         'AssignmentInfo',
#         related_name="assignquestioninfos", on_delete=models.DO_NOTHING
#     )
#
#     Register_Agent = ForeignKey(
#         'MemberInfo',
#         related_name="assignquestioninfos", on_delete=models.DO_NOTHING
#     )
#
#     class Meta:
#         ordering = ('-pk',)
#
#     def __unicode__(self):
#         return u'%s' % self.pk
#
#     def get_absolute_url(self):
#         return reverse('assignquestioninfo_detail', args=(self.pk,))
#
#     def get_update_url(self):
#         return reverse('assignquestioninfo_update', args=(self.pk,))
#
#
def assignment_upload(instance, filename):
    return 'assignments/{0}/{1}'.format(instance.Assignment_Code.id, filename)


class AssignAnswerInfo(models.Model):
    # Fields
    # subject_code = IntegerField(blank=True, null=True)

    Assignment_Score = IntegerField(blank=True, null=True)
    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Assignment_Answer = TextField(null=True, blank=True)
    Assignment_File = FileField(upload_to=assignment_upload, null=True, blank=True)

    # Relationship Fields
    # Assignment_Code = ForeignKey(
    #     'AssignmentInfo',
    #     related_name="assignanswerinfos", on_delete=models.DO_NOTHING
    # )
    Question_Code = ForeignKey(
        'QuestionInfo',
        related_name="assignanswerinfos", on_delete=models.DO_NOTHING
    )
    Student_Code = ForeignKey(
        'MemberInfo',
        related_name="assignanswerinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('assignanswerinfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('assignanswerinfo_update', args=(self.pk,))


# class OmrQuestionInfo(models.Model):
#     # Fields
#     # subject_code = IntegerField(blank=True, null=True)
#
#     Use_Flag = BooleanField(default=True)
#     Register_DateTime = DateTimeField(auto_now_add=True)
#     Updated_DateTime = DateTimeField(auto_now=True)
#     Register_Agent = CharField(max_length=500, blank=True, null=True)
#
#     Question_Level = IntegerField(blank=True, null=True)
#     Question_Score = IntegerField(blank=True, null=True)
#     Question_Description = TextField(blank=True, null=True)
#     # Relationship Fields
#     Homework_Code = ForeignKey(
#         'HomeworkInfo',
#         related_name="omrquestioninfos", on_delete=models.DO_NOTHING
#     )
#
#     class Meta:
#         ordering = ('-pk',)
#
#     def __unicode__(self):
#         return u'%s' % self.pk
#
#     def get_absolute_url(self):
#         return reverse('omrquestioninfo_detail', args=(self.pk,))
#
#     def get_update_url(self):
#         return reverse('omrquestioninfo_update', args=(self.pk,))


# class OmrAnswerInfo(models.Model):
#     # Fields
#     # subject_code = IntegerField(blank=True, null=True)
#     # omr_answer = IntegerField(blank=True, null=True)
#     # omr_answer_idx = IntegerField(blank=True, null=True)
#     # omr_answer_correct = CharField(max_length=200, blank=True, null=True)
#     # question_score = IntegerField(blank=True, null=True)
#
#     Use_Flag = BooleanField(default=True)
#     Register_DateTime = DateTimeField(auto_now_add=True)
#     Updated_DateTime = DateTimeField(auto_now=True)
#     Answer_Description = models.TextField(blank=True, null=True)
#     Answer_Score = IntegerField(blank=True, null=True)
#     # Relationship Fields
#     # lecture_code = ForeignKey(
#     #     'LectureInfo',
#     #      related_name="omranswerinfos", on_delete=models.DO_NOTHING
#     # )
#     # chapter_code = ForeignKey(
#     #     'ChapterInfo',
#     #      related_name="omranswerinfos", on_delete=models.DO_NOTHING
#     # )
#     Student_Code = ForeignKey(
#         'MemberInfo',
#         related_name="omranswerinfos", on_delete=models.DO_NOTHING
#     )
#     Question_Code = ForeignKey(
#         'OmrQuestionInfo',
#         related_name="omranswerinfos", on_delete=models.DO_NOTHING
#     )
#
#     # lesson_code = ForeignKey(
#     #     'LessonInfo',
#     #      related_name="omranswerinfos", on_delete=models.DO_NOTHING
#     # )
#
#     class Meta:
#         ordering = ('-pk',)
#
#     def __unicode__(self):
#         return u'%s' % self.pk
#
#     def get_absolute_url(self):
#         return reverse('omranswerinfo_detail', args=(self.pk,))
#
#     def get_update_url(self):
#         return reverse('omranswerinfo_update', args=(self.pk,))

class SessionInfo(models.Model):
    Session_Name = CharField(max_length=500, blank=True, null=True)
    Description = TextField(blank=True, null=True)
    Use_Flag = BooleanField(default=True)

    Center_Code = ForeignKey(
        'CenterInfo',
        related_name="sessioninfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('sessioninfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('sessioninfo_update', args=(self.pk,))

    def __str__(self):
        return self.Session_Name


class GroupMapping(models.Model):
    # Fields
    GroupMapping_Name = CharField(max_length=500, blank=True, null=True)
    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    # Relationship Fields
    # Inning_Code = ForeignKey(
    #     'InningInfo',
    #     on_delete=models.DO_NOTHING
    # )
    Students = models.ManyToManyField(
        'MemberInfo'
    )

    Center_Code = ForeignKey(
        'CenterInfo',
        related_name="groupmappings", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.GroupMapping_Name

    def __str__(self):
        return u'%s' % self.GroupMapping_Name

    def get_absolute_url(self):
        return reverse('groupmapping_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('groupmapping_update', args=(self.pk,))


class InningGroup(models.Model):
    # Fields

    InningGroup_Name = CharField(max_length=500, blank=True, null=True)
    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    # Relationship Fields
    # Inning_Code = ForeignKey(
    #     'InningInfo',
    #     related_name="inninggroups", on_delete=models.DO_NOTHING
    # )
    Lecture_Code = ForeignKey(
        'LectureInfo',
        related_name="inninggroups", on_delete=models.DO_NOTHING
    )

    Teacher_Code = models.ManyToManyField(
        'MemberInfo'
    )

    Center_Code = ForeignKey(
        'CenterInfo',
        related_name="inninggroups", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.InningGroup_Name

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('inninggroup_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('inninggroup_update', args=(self.pk,))


class InningInfo(models.Model):
    # Fields

    Start_Date = DateTimeField(auto_now=False, auto_now_add=False)
    End_Date = DateTimeField(auto_now=False, auto_now_add=False)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    # Relationship Fields
    Inning_Name = ForeignKey(
        'SessionInfo',
        related_name="inninginfos", on_delete=models.DO_NOTHING
    )

    Center_Code = ForeignKey(
        'CenterInfo',
        related_name="inninginfos", on_delete=models.DO_NOTHING
    )

    Groups = ForeignKey(
        'GroupMapping',
        related_name="inninginfos", on_delete=models.DO_NOTHING
    )

    Course_Group = models.ManyToManyField(
        'InningGroup'
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('inninginfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('inninginfo_update', args=(self.pk,))

    # def __str__(self):
    #     return self.Inning_Name


class ChapterMissonCheckCard(models.Model):
    # Fields
    check_card_code = IntegerField(unique=True)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    # Relationship Fields
    chapter_code = ForeignKey(
        'ChapterInfo',
        related_name="chaptermissoncheckcards", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('chaptermissoncheckcard_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('chaptermissoncheckcard_update', args=(self.pk,))


class ChapterMissonCheckItem(models.Model):
    # Fields
    check_item_code = IntegerField(unique=True)
    item_text = TextField(blank=True, null=True)
    contents_text = TextField(blank=True, null=True)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    # Relationship Fields
    check_card_code = ForeignKey(
        'ChapterMissonCheckCard',
        related_name="chaptermissoncheckitems", on_delete=models.DO_NOTHING
    )
    chapter_contents_code = ForeignKey(
        'ChapterContentsInfo',
        related_name="chaptermissoncheckitems", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('chaptermissoncheckitem_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('chaptermissoncheckitem_update', args=(self.pk,))


class QuizInfo(models.Model):
    # Fields
    subject_code = IntegerField(blank=True, null=True)
    quiz_type = CharField(max_length=50, blank=True, null=True)
    quiz_question = CharField(max_length=1000, blank=True, null=True)
    quiz_media_type = CharField(max_length=10, blank=True, null=True)
    quiz_media_file = CharField(max_length=200, blank=True, null=True)
    quiz_score = IntegerField(blank=True, null=True)
    quiz_comment = CharField(max_length=1000, blank=True, null=True)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)
    quiz_head = CharField(max_length=1000, blank=True, null=True)
    quiz_media_file2 = CharField(max_length=250, blank=True, null=True)

    # Relationship Fields
    lecture_code = ForeignKey(
        'LectureInfo',
        related_name="quizinfos", on_delete=models.DO_NOTHING
    )
    chapter_code = ForeignKey(
        'ChapterInfo',
        related_name="quizinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('quizinfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('quizinfo_update', args=(self.pk,))


class BoardInfo(models.Model):
    # Fields
    board_name = CharField(max_length=500, blank=True, null=True)
    board_write_level = CharField(max_length=2, blank=True, null=True)
    board_read_level = CharField(max_length=2, blank=True, null=True)
    board_reply_level = CharField(max_length=2, blank=True, null=True)
    board_new_time = IntegerField(blank=True, null=True)
    board_create_time = CharField(max_length=16, blank=True, null=True)
    admin_id = CharField(max_length=20, blank=True, null=True)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('boardinfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('boardinfo_update', args=(self.pk,))


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

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    # Relationship Fields
    board_code = ForeignKey(
        'BoardInfo',
        related_name="boardcontentinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('boardcontentinfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('boardcontentinfo_update', args=(self.pk,))


class ChapterContentMedia(models.Model):
    # Fields
    media_type = CharField(max_length=10)
    media_desc = TextField(blank=True, null=True)
    media_filename = CharField(max_length=255)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    # Relationship Fields
    chapter_contents_code = ForeignKey(
        'ChapterContentsInfo',
        related_name="chaptercontentmedias", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('chaptercontentmedia_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('chaptercontentmedia_update', args=(self.pk,))


class ChapterImgInfo(models.Model):
    # Fields
    filename = CharField(max_length=150, blank=True, null=True)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    # Relationship Fields
    chapter_code = ForeignKey(
        'ChapterInfo',
        related_name="chapterimginfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('chapterimginfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('chapterimginfo_update', args=(self.pk,))


class ChapterMissonCheck(models.Model):
    # Fields
    check_code = IntegerField(unique=True)
    student_code = IntegerField()
    check_agent_code = IntegerField()
    is_check_yn = CharField(max_length=1)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    # Relationship Fields
    check_item_code = ForeignKey(
        'ChapterMissonCheckItem',
        related_name="chaptermissonchecks", on_delete=models.DO_NOTHING
    )
    inning_code = ForeignKey(
        'InningInfo',
        related_name="chaptermissonchecks", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('chaptermissoncheck_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('chaptermissoncheck_update', args=(self.pk,))


class ChapterWrite(models.Model):
    # Fields
    student_code = IntegerField(blank=True, null=True)
    write_content = TextField(blank=True, null=True)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    # Relationship Fields
    inning_code = ForeignKey(
        'InningInfo',
        related_name="chapterwrites", on_delete=models.DO_NOTHING
    )
    chapter_contents_code = ForeignKey(
        'ChapterContentsInfo',
        related_name="chapterwrites", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('chapterwrite_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('chapterwrite_update', args=(self.pk,))


class LearningNote(models.Model):
    # Fields
    contents_code = IntegerField()
    note_contents = TextField(blank=True, null=True)
    note_attachment = CharField(max_length=250, blank=True, null=True)

    # Relationship Fields
    inning_code = ForeignKey(
        'InningInfo',
        related_name="learningnotes", on_delete=models.DO_NOTHING
    )
    lecture_code = ForeignKey(
        'LectureInfo',
        related_name="learningnotes", on_delete=models.DO_NOTHING
    )
    chapter_code = ForeignKey(
        'ChapterInfo',
        related_name="learningnotes", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('learningnote_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('learningnote_update', args=(self.pk,))


class LectureUbtInfo(models.Model):
    # Fields
    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)
    # Relationship Fields
    quiz_code = ForeignKey(
        'QuizInfo',
        related_name="lectureubtinfos", on_delete=models.DO_NOTHING
    )
    lecture_code = ForeignKey(
        'LectureInfo',
        related_name="lectureubtinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('lectureubtinfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('lectureubtinfo_update', args=(self.pk,))


class LessonInfo(models.Model):
    # Fields
    teacher_code = IntegerField(blank=True, null=True)
    start_date = CharField(max_length=150, blank=True, null=True)
    end_date = CharField(max_length=150, blank=True, null=True)
    progress = CharField(max_length=150, blank=True, null=True)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    ubt_start = CharField(max_length=50, blank=True, null=True)
    ubt_end = CharField(max_length=50, blank=True, null=True)
    download_count = IntegerField(blank=True, null=True)
    download_date = CharField(max_length=19, blank=True, null=True)

    # Relationship Fields
    lecture_code = ForeignKey(
        'LectureInfo',
        related_name="lessoninfos", on_delete=models.DO_NOTHING
    )
    member_code = ForeignKey(
        'MemberInfo',
        related_name="lessoninfos", on_delete=models.DO_NOTHING
    )
    center_code = ForeignKey(
        'CenterInfo',
        related_name="lessoninfos", on_delete=models.DO_NOTHING
    )
    inning_code = ForeignKey(
        'InningInfo',
        related_name="lessoninfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('lessoninfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('lessoninfo_update', args=(self.pk,))


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

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)
    study_time = IntegerField(blank=True, null=True)
    connect_page = IntegerField(blank=True, null=True)

    # Relationship Fields
    lesson_code = ForeignKey(
        'LessonInfo',
        related_name="lessonlogs", on_delete=models.DO_NOTHING
    )
    lecture_code = ForeignKey(
        'LectureInfo',
        related_name="lessonlogs", on_delete=models.DO_NOTHING
    )
    chapter_code = ForeignKey(
        'ChapterInfo',
        related_name="lessonlogs", on_delete=models.DO_NOTHING
    )
    member_code = ForeignKey(
        'MemberInfo',
        related_name="lessonlogs", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('lessonlog_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('lessonlog_update', args=(self.pk,))


class MemberGroup(models.Model):
    # Fields
    group_name = CharField(max_length=500, blank=True, null=True)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    # Relationship Fields
    center_code = ForeignKey(
        'CenterInfo',
        related_name="membergroups", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('membergroup_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('membergroup_update', args=(self.pk,))


class MessageInfo(models.Model):
    # Fields
    teacher_code = IntegerField(blank=True, null=True)
    message = CharField(max_length=4000, blank=True, null=True)
    message_read = CharField(max_length=1, blank=True, null=True)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    # Relationship Fields
    member_code = ForeignKey(
        'MemberInfo',
        related_name="messageinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('messageinfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('messageinfo_update', args=(self.pk,))


# class OmrAssignInfo(models.Model):
#     # Fields
#     subject_code = IntegerField(blank=True, null=True)
#
#     Use_Flag = BooleanField(default=True)
#     Register_DateTime = DateTimeField(auto_now_add=True)
#     Updated_DateTime = DateTimeField(auto_now=True)
#     Register_Agent = CharField(max_length=500, blank=True, null=True)
#
#     # Relationship Fields
#     question_code = ForeignKey(
#         'OmrQuestionInfo',
#         related_name="omrassigninfos", on_delete=models.DO_NOTHING
#     )
#     lecture_code = ForeignKey(
#         'LectureInfo',
#         related_name="omrassigninfos", on_delete=models.DO_NOTHING
#     )
#     chapter_code = ForeignKey(
#         'ChapterInfo',
#         related_name="omrassigninfos", on_delete=models.DO_NOTHING
#     )
#     member_code = ForeignKey(
#         'MemberInfo',
#         related_name="omrassigninfos", on_delete=models.DO_NOTHING
#     )
#
#     class Meta:
#         ordering = ('-pk',)
#
#     def __unicode__(self):
#         return u'%s' % self.pk
#
#     def get_absolute_url(self):
#         return reverse('omrassigninfo_detail', args=(self.pk,))
#
#     def get_update_url(self):
#         return reverse('omrassigninfo_update', args=(self.pk,))
#
#
# class OmrExampleInfo(models.Model):
#     # Fields
#     omr_example_correct = CharField(max_length=1, blank=True, null=True)
#     omr_example_idx = IntegerField(blank=True, null=True)
#
#     Use_Flag = BooleanField(default=True)
#     Register_DateTime = DateTimeField(auto_now_add=True)
#     Updated_DateTime = DateTimeField(auto_now=True)
#     Register_Agent = CharField(max_length=500, blank=True, null=True)
#
#     # Relationship Fields
#     question_code = ForeignKey(
#         'OmrQuestionInfo',
#         related_name="omrexampleinfos", on_delete=models.DO_NOTHING
#     )
#
#     class Meta:
#         ordering = ('-pk',)
#
#     def __unicode__(self):
#         return u'%s' % self.pk
#
#     def get_absolute_url(self):
#         return reverse('omrexampleinfo_detail', args=(self.pk,))
#
#     def get_update_url(self):
#         return reverse('omrexampleinfo_update', args=(self.pk,))


# class QAnswerLog(models.Model):
#     # Fields
#     question_answer = CharField(max_length=250, blank=True, null=True)
#     question_idx = CharField(max_length=250, blank=True, null=True)
#     question_score = IntegerField(blank=True, null=True)
#     Use_Flag = BooleanField(default=True)
#     Register_DateTime = DateTimeField(auto_now_add=True)
#     Updated_DateTime = DateTimeField(auto_now=True)
#     Register_Agent = CharField(max_length=500, blank=True, null=True)
#     # Relationship Fields
#     lecture_code = ForeignKey(
#         'LectureInfo',
#         related_name="qanswerlogs", on_delete=models.DO_NOTHING
#     )
#     member_code = ForeignKey(
#         'MemberInfo',
#         related_name="qanswerlogs", on_delete=models.DO_NOTHING
#     )
#     # question_code = ForeignKey(
#     #     'OmrQuestionInfo',
#     #     related_name="qanswerlogs", on_delete=models.DO_NOTHING
#     # )
#
#     class Meta:
#         ordering = ('-pk',)
#
#     def __unicode__(self):
#         return u'%s' % self.pk
#
#     def get_absolute_url(self):
#         return reverse('qanswerlog_detail', args=(self.pk,))
#
#     def get_update_url(self):
#         return reverse('qanswerlog_update', args=(self.pk,))


class QExampleInfo(models.Model):
    # Fields
    q_example = CharField(max_length=1000, blank=True, null=True)
    q_example_correct = CharField(max_length=10, blank=True, null=True)
    q_example_idx = IntegerField(blank=True, null=True)
    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)
    q_example_type = CharField(max_length=50, blank=True, null=True)

    # Relationship Fields
    # question_code = ForeignKey(
    #     'OmrQuestionInfo',
    #     related_name="qexampleinfos", on_delete=models.DO_NOTHING
    # )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('qexampleinfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('qexampleinfo_update', args=(self.pk,))


class QuizAnswerInfo(models.Model):
    # Fields
    subject_code = IntegerField(blank=True, null=True)
    quiz_type = CharField(max_length=50, blank=True, null=True)
    quiz_answer = IntegerField(blank=True, null=True)
    quiz_answer_idx = IntegerField(blank=True, null=True)
    quiz_correct = CharField(max_length=50, blank=True, null=True)
    quiz_score = IntegerField(blank=True, null=True)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)
    test_type = IntegerField(blank=True, null=True)

    # Relationship Fields
    lecture_code = ForeignKey(
        'LectureInfo',
        related_name="quizanswerinfos", on_delete=models.DO_NOTHING
    )
    chapter_code = ForeignKey(
        'ChapterInfo',
        related_name="quizanswerinfos", on_delete=models.DO_NOTHING
    )
    member_code = ForeignKey(
        'MemberInfo',
        related_name="quizanswerinfos", on_delete=models.DO_NOTHING
    )
    quiz_code = ForeignKey(
        'QuizInfo',
        related_name="quizanswerinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('quizanswerinfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('quizanswerinfo_update', args=(self.pk,))


class QuizExampleInfo(models.Model):
    # Fields
    quiz_example = CharField(max_length=1000, blank=True, null=True)
    quiz_example_correct = CharField(max_length=10, blank=True, null=True)
    quiz_example_idx = IntegerField(blank=True, null=True)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    quiz_example_type = CharField(max_length=50, blank=True, null=True)

    # Relationship Fields
    quiz_code = ForeignKey(
        'QuizInfo',
        related_name="quizexampleinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('quizexampleinfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('quizexampleinfo_update', args=(self.pk,))


class ScheduleInfo(models.Model):
    # Fields
    title = CharField(max_length=500, blank=True, null=True)
    content = CharField(max_length=2000, blank=True, null=True)
    start_date = CharField(max_length=10, blank=True, null=True)
    start_time = CharField(max_length=8, blank=True, null=True)
    end_date = CharField(max_length=10, blank=True, null=True)
    end_time = CharField(max_length=8, blank=True, null=True)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    # Relationship Fields
    member_code = ForeignKey(
        'MemberInfo',
        related_name="scheduleinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('scheduleinfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('scheduleinfo_update', args=(self.pk,))


class TalkMember(models.Model):
    # Fields
    use_flag = BooleanField(blank=True, null=True)

    # Relationship Fieldspro
    member_code = ForeignKey(
        'MemberInfo',
        related_name="talkmembers", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('talkmember_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('talkmember_update', args=(self.pk,))


class TalkRoom(models.Model):
    # Fields
    talk_room_cate_code = CharField(max_length=10)
    use_flag = BooleanField(blank=True, null=True)

    # Relationship Fields
    lecture_code = ForeignKey(
        'LectureInfo',
        related_name="talkrooms", on_delete=models.DO_NOTHING
    )
    inning_code = ForeignKey(
        'InningInfo',
        related_name="talkrooms", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('talkroom_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('talkroom_update', args=(self.pk,))


class TalkMessage(models.Model):
    # Fields
    message = CharField(max_length=5000, blank=True, null=True)
    sender_member_code = IntegerField(blank=True, null=True)
    send_date = CharField(max_length=10, blank=True, null=True)
    send_time = CharField(max_length=8, blank=True, null=True)

    # Relationship Fields
    talk_room_id = ForeignKey(
        'TalkRoom',
        related_name="talkmessages", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('talkmessage_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('talkmessage_update', args=(self.pk,))


class TalkMessageRead(models.Model):
    # Fields
    is_read = BooleanField()

    # Relationship Fields
    member_code = ForeignKey(
        'MemberInfo',
        related_name="talkmessagereads", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('talkmessageread_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('talkmessageread_update', args=(self.pk,))


class TodoInfo(models.Model):
    # Fields
    todo_comment = CharField(max_length=4000, blank=True, null=True)
    todo_status = CharField(max_length=1, blank=True, null=True)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    teacher_code = IntegerField(blank=True, null=True)
    todo_title = CharField(max_length=500, blank=True, null=True)
    start_date = CharField(max_length=50, blank=True, null=True)
    start_time = CharField(max_length=50, blank=True, null=True)
    end_date = CharField(max_length=50, blank=True, null=True)
    end_time = CharField(max_length=50, blank=True, null=True)

    # Relationship Fields
    chapter_code = ForeignKey(
        'ChapterInfo',
        related_name="todoinfos", on_delete=models.DO_NOTHING
    )
    member_code = ForeignKey(
        'MemberInfo',
        related_name="todoinfos", on_delete=models.DO_NOTHING
    )
    lecture_code = ForeignKey(
        'LectureInfo',
        related_name="todoinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('todoinfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('todoinfo_update', args=(self.pk,))


class TodoTInfo(models.Model):
    # Fields
    todo_code = IntegerField(blank=True, null=True)
    todo_t_flag = CharField(max_length=10, blank=True, null=True)

    Use_Flag = BooleanField(default=True)
    Register_DateTime = DateTimeField(auto_now_add=True)
    Updated_DateTime = DateTimeField(auto_now=True)
    Register_Agent = CharField(max_length=500, blank=True, null=True)

    # Relationship Fields
    member_code = ForeignKey(
        'MemberInfo',
        related_name="todotinfos", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('todotinfo_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('todotinfo_update', args=(self.pk,))


class Events(models.Model):
    even_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    event_type = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.event_name
