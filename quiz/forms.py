from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.widgets import RadioSelect, Textarea
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
# from quiz import admin
from django_addanother.widgets import AddAnotherWidgetWrapper

from quiz.models import Quiz, MCQuestion, TF_Question


# class AnswerInline(admin.TabularInline):
#     model = Answer

class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list,
                                                   widget=RadioSelect)


class EssayForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(EssayForm, self).__init__(*args, **kwargs)
        self.fields["answers"] = forms.CharField(
            widget=Textarea(attrs={'style': 'width:100%'}))


class QuizForm(forms.ModelForm):

    mcquestion = forms.ModelMultipleChoiceField(
        queryset=MCQuestion.objects.all(),
        initial=[],
        required=False,
        # label=_("Questions"),
        widget= AddAnotherWidgetWrapper(
                forms.SelectMultiple,
                reverse_lazy('mcquestion_create'),
            ))

    class Meta:
        model = Quiz
        fields = '__all__'


class MCQuestionForm(forms.ModelForm):
    class Meta:
        model = MCQuestion
        fields = '__all__'

    quiz = forms.ModelMultipleChoiceField(
        queryset=Quiz.objects.all(),
        required=False,
        # label=_("Questions"),
        widget=FilteredSelectMultiple(verbose_name=_("Quizzes"), is_stacked=False))


class TFQuestionForm(forms.ModelForm):
    class Meta:
        model = TF_Question
        fields = '__all__'

    quiz = forms.ModelMultipleChoiceField(
        queryset=Quiz.objects.all(),
        required=False,
        # label=_("Questions"),
        widget=FilteredSelectMultiple(verbose_name=_("Quizzes"), is_stacked=False))

