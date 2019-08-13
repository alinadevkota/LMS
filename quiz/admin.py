import django
from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.html import format_html
from django.utils.translation import gettext as _

from .models import Quiz, Progress, Answer, MCQuestion, TF_Question, Essay_Question


class AnswerInline(admin.TabularInline):
    model = Answer


class QuizAdminForm(forms.ModelForm):
    """
    below is from
    http://stackoverflow.com/questions/11657682/
    django-admin-interface-using-horizontal-filter-with-
    inline-manytomany-field
    """
    class Meta:
        model = Quiz
        exclude = []

    def __init__(self, *args, **kwargs):
        super(QuizAdminForm, self).__init__(*args, **kwargs)


# for adding widget to the quiz fields
    # mcquestion = forms.ModelMultipleChoiceField(
    #     queryset=MCQuestion.objects.all(),
    #     required=False,
    #     # label=_("Questions"),
    #     # widget= AddAnotherWidgetWrapper(
    #     #         forms.SelectMultiple,
    #     #         reverse_lazy('mcquestion_create'),
    #     widget=FilteredSelectMultiple(verbose_name=_("MCQ"), is_stacked=False))


class QuizAdmin(admin.ModelAdmin):
    form = QuizAdminForm

    add_form_template = 'admin_add_form_with_buttons.html'
    change_form_template = 'admin_add_form.html'

    # list_display = ('title', 'category', )
    # list_filter = ('category',)
    search_fields = ('description', 'category',)


    # def changelist_view(self, request, extra_context=None):
    #     # Execute default logic from parent class changelist_view()
    #
    #
    #     return super(QuizAdmin, self).changelist_view(
    #         request, extra_context=extra_context
    #     )

    # def get_osm_info(self):
    #     # ...
    #     pass
    #
    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     extra_context = extra_context or {}
    #     extra_context['osm_data'] = self.get_osm_info()
    #     return super(QuizAdmin, self).change_view(
    #         request, object_id, form_url, extra_context=extra_context,
    #     )
    # def change_button(self, obj):
    #     return format_html('<a class="btn" href="/admin/quiz/mcquestion/{}/change/">Change</a>', obj.id)
    #
    # def delete_button(self, obj):
    #     return format_html('<a class="btn" href="/admin/quiz/mcquestion/{}/delete/">Delete</a>', obj.id)

    # list_display = ('__str__', 'change_button', 'delete_button')


# class CategoryAdmin(admin.ModelAdmin):
#     search_fields = ('category',)
#
#
# class SubCategoryAdmin(admin.ModelAdmin):
#     search_fields = ('sub_category',)
#     # list_display = ('sub_category', 'category',)
#     # list_filter = ('category',)

class ProgressAdmin(admin.ModelAdmin):
    """
    to do:
            create a user section
    """
    search_fields = ('user', 'score',)


class MCQuestionAdmin(admin.ModelAdmin):

    change_form_template = 'admin_add_form.html'
    change_list_template = 'custom_list.html'
    list_display = ('content', 'category', )
    list_filter = ('category',)
    fields = ('content', 'figure', 'explanation', 'answer_order')

    search_fields = ('content', 'explanation')
    # filter_horizontal = ('quiz',)

    inlines = [AnswerInline]
    add_form_template = 'admin_add_form.html'


class TFQuestionAdmin(admin.ModelAdmin):
    change_form_template = 'admin_add_form.html'
    change_list_template = 'custom_list.html'

    list_display = ('content', 'category', )
    list_filter = ('category',)
    fields = ('content', 'figure', 'explanation', 'correct',)

    search_fields = ('content', 'explanation')
    # filter_horizontal = ('quiz',)
    add_form_template = 'admin_add_form.html'


class EssayQuestionAdmin(admin.ModelAdmin):
    change_form_template = 'admin_add_form.html'
    change_list_template = 'custom_list.html'

    # list_display = ('content', 'category', )
    # list_filter = ('category',)
    fields = ('content', 'explanation')
    search_fields = ('content', 'explanation')
    # filter_horizontal = ('quiz',)
    add_form_template = 'admin_add_form.html'


admin.site.register(Quiz, QuizAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(MCQuestion, MCQuestionAdmin)
admin.site.register(Progress, ProgressAdmin)
admin.site.register(TF_Question, TFQuestionAdmin)
admin.site.register(Essay_Question, EssayQuestionAdmin)
