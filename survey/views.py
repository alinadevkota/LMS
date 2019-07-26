from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import CategoryInfo, SurveyInfo, QuestionInfo, OptionInfo
from .forms import CategoryInfoForm, SurveyInfoForm, QuestionInfoForm, OptionInfoForm


class CategoryInfoListView(ListView):
    model = CategoryInfo


class CategoryInfoCreateView(CreateView):
    model = CategoryInfo
    form_class = CategoryInfoForm


class CategoryInfoDetailView(DetailView):
    model = CategoryInfo


class CategoryInfoUpdateView(UpdateView):
    model = CategoryInfo
    form_class = CategoryInfoForm


class SurveyInfoListView(ListView):
    model = SurveyInfo


class SurveyInfoCreateView(CreateView):
    model = SurveyInfo
    form_class = SurveyInfoForm


class SurveyInfoDetailView(DetailView):
    model = SurveyInfo


class SurveyInfoUpdateView(UpdateView):
    model = SurveyInfo
    form_class = SurveyInfoForm


class QuestionInfoListView(ListView):
    model = QuestionInfo


class QuestionInfoCreateView(CreateView):
    model = QuestionInfo
    form_class = QuestionInfoForm


class QuestionInfoDetailView(DetailView):
    model = QuestionInfo


class QuestionInfoUpdateView(UpdateView):
    model = QuestionInfo
    form_class = QuestionInfoForm


class OptionInfoListView(ListView):
    model = OptionInfo


class OptionInfoCreateView(CreateView):
    model = OptionInfo
    form_class = OptionInfoForm


class OptionInfoDetailView(DetailView):
    model = OptionInfo


class OptionInfoUpdateView(UpdateView):
    model = OptionInfo
    form_class = OptionInfoForm

