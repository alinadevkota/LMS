from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.contenttypes.models import ContentType
from django.core.files.storage import FileSystemStorage
from django.db import models as models
from django.db.models import ForeignKey, CharField, IntegerField, DateTimeField, TextField, BooleanField, \
    ImageField
from django.urls import reverse
from django.utils.translation import gettext as _
from WebApp.models import MemberInfo,InningInfo

class CategoryInfo(models.Model):

    # Fields
    Category_Name = CharField(max_length=500, blank=True, null=True)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('categoryinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('categoryinfo_update', args=(self.pk,))


class SurveyInfo(models.Model):

    # Fields
    Survey_Title = CharField(max_length=500, blank=True, null=True)
    Start_Date = DateTimeField(auto_now=False, auto_now_add=False)
    End_Date = DateTimeField(auto_now=False, auto_now_add=False)
    Survey_Cover = ImageField(upload_to="Survey_Covers/", blank=True, null=False)
    Use_Flag = BooleanField(default=True)
    Assigned_To = ForeignKey(
        'WebApp.InningInfo',
        related_name="surveyinfo", on_delete=models.DO_NOTHING, null=True
    )
    Added_By = ForeignKey(
        'WebApp.MemberInfo',
        related_name="surveyinfo", on_delete=models.DO_NOTHING
    )
    Category_Code = ForeignKey(
        'CategoryInfo',
        related_name="surveyinfo", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('surveyinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('surveyinfo_update', args=(self.pk,))
    
    

class QuestionInfo(models.Model):

    # Fields
    Question_Name = CharField(max_length=500, blank=True, null=True)
    Question_Answer = CharField(max_length=500, blank=True, null=True)
    Question_Type=CharField(max_length=500, blank=True, null=True)
    Survey_Code = ForeignKey(
        'SurveyInfo',
        related_name="questioninfo", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('questioninfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('questioninfo_update', args=(self.pk,))


class OptionInfo(models.Model):

    # Fields
    Option_Name = CharField(max_length=500, blank=True, null=True)
    Question_Code = ForeignKey(
        'QuestionInfo',
        related_name="optioninfo", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('optioninfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('optioninfo_update', args=(self.pk,))


