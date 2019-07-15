from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.widgets import RadioSelect, Textarea
from django.utils.translation import gettext as _

from quiz.models import Quiz, Question, MCQuestion, TF_Question, Essay_Question


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

class Media:
    css = {'all': ('/static/admin/css/widgets.css',), }

class QuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = '__all__'

    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all().select_subclasses(),
        required=False,
        # label=_("Questions"),
        widget=FilteredSelectMultiple( verbose_name=_("Questions"), is_stacked=False))

    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['questions'].initial = self.instance.question_set.all().select_subclasses()

    def save(self, commit=True):
        quiz = super(QuizForm, self).save(commit=False)
        quiz.save()
        quiz.question_set.set(self.cleaned_data['questions'])
        self.save_m2m()
        return quiz


class MCQuestionForm(forms.ModelForm):
    class Meta:
        model = MCQuestion
        fields = '__all__'

class TFQuestionForm(forms.ModelForm):
    class Meta:
        model = TF_Question
        fields = '__all__'

class EssayQuestionForm(forms.ModelForm):
    class Meta:
        model = Essay_Question
        fields = '__all__'
