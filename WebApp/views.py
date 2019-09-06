from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LogoutView, LoginView, PasswordContextMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from django.views import generic
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView, TemplateView
from django.views.generic.edit import FormView
from django.core.paginator import Paginator

from forum.models import Thread
from forum.views import get_top_thread_keywords
from survey.models import SurveyInfo
from quiz.models import Question

from .forms import CenterInfoForm, CourseInfoForm, ChapterInfoForm, ChapterContentsInfoForm, \
    ChapterMissonCheckCardForm, ChapterMissonCheckItemForm, SessionInfoForm, InningInfoForm, QuizInfoForm, \
    AssignmentInfoForm, QuestionInfoForm, AssignAssignmentInfoForm, \
    AssignAnswerInfoForm, \
    BoardInfoForm, BoardContentInfoForm, InningGroupForm, \
    ChapterContentMediaForm, ChapterImgInfoForm, ChapterMissonCheckForm, ChapterWriteForm, GroupMappingForm, \
    LearningNoteForm, CourseUbtInfoForm, LessonInfoForm, LessonLogForm, MemberGroupForm, \
    MessageInfoForm, \
    QExampleInfoForm, QuizAnswerInfoForm, QuizExampleInfoForm, ScheduleInfoForm, TalkMemberForm, \
    TalkRoomForm, TalkMessageForm, TalkMessageReadForm, TodoInfoForm, TodoTInfoForm, UserUpdateForm, UserRegisterForm, \
    MemberInfoForm, ChangeOthersPasswordForm
from .models import CenterInfo, MemberInfo, CourseInfo, ChapterInfo, ChapterContentsInfo, ChapterMissonCheckCard, \
    ChapterMissonCheckItem, InningInfo, QuizInfo, AssignmentInfo, QuestionInfo, AssignAssignmentInfo, \
    AssignAnswerInfo, BoardInfo, \
    BoardContentInfo, SessionInfo, InningGroup, ChapterContentMedia, ChapterImgInfo, ChapterMissonCheck, ChapterWrite, \
    GroupMapping, \
    LearningNote, CourseUbtInfo, LessonInfo, LessonLog, MemberGroup, MessageInfo, \
    QExampleInfo, QuizAnswerInfo, QuizExampleInfo, \
    ScheduleInfo, TalkMember, TalkRoom, TalkMessage, TalkMessageRead, TodoInfo, TodoTInfo, Events
from datetime import datetime
import json


#
#
# class ProfileListView(ListView):
#     model = Profile
#
#
# class ProfileCreateView(CreateView):
#     model = Profile
#     form_class = ProfileForm
#
#
# class ProfileDetailView(DetailView):
#     model = Profile
#
#
# class ProfileUpdateView(UpdateView):
#     model = Profile
#     form_class = ProfileForm
#

class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


def ProfileView(request):
    try:
        center = CenterInfo.objects.get(Center_Name=request.user.Center_Code)
    except:
        center = None
        pass
    return render(request, 'WebApp/profile.html', {"center": center})


def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          extra_context=None, redirect_authenticated_user=True):
    # warnings.warn(
    #     'The login() view is superseded by the class-based LoginView().',
    #     RemovedInDjango21Warning, stacklevel=2
    # )
    # if request.method == "POST":
    #     form = authentication_form(request, data=request.POST)
    #     if form.is_valid():
    #         return redirect('/')
    #     else:
    #         messages.error(request, 'Invalid Credential')
    #         return redirect('/login')
    # else:
    return LoginView.as_view(
        template_name=template_name,
        redirect_field_name=redirect_field_name,
        form_class=authentication_form,
        extra_context=extra_context,
        redirect_authenticated_user=redirect_authenticated_user,
    )(request)


def logout(request, next_page=None,
           template_name='logged_out.html',
           redirect_field_name=REDIRECT_FIELD_NAME,
           extra_context=None):
    # warnings.warn(
    #     'The logout() view is superseded by the class-based LogoutView().',
    #     RemovedInDjango21Warning, stacklevel=2
    # )
    return LogoutView.as_view(
        next_page=next_page,
        template_name=template_name,
        redirect_field_name=redirect_field_name,
        extra_context=extra_context,
    )(request)


_sentinel = object()


def calendar(request):
    all_events = Events.objects.all()

    get_event_types = Events.objects.only('event_type')
    # if filters applied then get parameter and filter based on condition else return object
    if request.GET:
        event_arr = []
        if request.GET.get('event_type') == "all":
            all_events = Events.objects.all()
        else:
            all_events = Events.objects.filter(event_type__icontains=request.GET.get('event_type'))

        for i in all_events:
            event_sub_arr = {}
            event_sub_arr['title'] = i.event_name
            start_date = datetime.strptime(str(i.start_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            end_date = datetime.strptime(str(i.end_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            event_sub_arr['start'] = start_date
            event_sub_arr['end'] = end_date
            event_arr.append(event_sub_arr)
        return HttpResponse(json.dumps(event_arr))

    # print(context['events'])
    return render(request, 'WebApp/calendar.html', {'events': all_events, "get_event_types": get_event_types})


def start(request):
    """Start page with a documentation.
    """
    # return render(request,"start.html")

    if request.user.is_authenticated:

        if request.user.Is_CenterAdmin:
            thread = Thread.objects.order_by('-pub_date')[:5]
            wordCloud = Thread.objects.all()
            thread_keywords = get_top_thread_keywords(request, 10)
            course = CourseInfo.objects.order_by('-Register_DateTime')[:4]
            coursecount = CourseInfo.objects.count()
            studentcount = MemberInfo.objects.filter(Is_Student=True, Center_Code=request.user.Center_Code).count
            teachercount = MemberInfo.objects.filter(Is_Teacher=True, Center_Code=request.user.Center_Code).count
            threadcount = Thread.objects.count()
            totalcount = MemberInfo.objects.filter(Center_Code=request.user.Center_Code).count

            # return HttpResponse("default home")
            return render(request, "WebApp/homepage.html",
                          {'course': course, 'coursecount': coursecount, 'studentcount': studentcount,
                           'teachercount': teachercount,
                           'threadcount': threadcount, 'totalcount': totalcount, 'thread': thread,
                           'wordCloud': wordCloud, 'get_top_thread_keywords': thread_keywords})
        if request.user.Is_Student:
            return redirect('student_home')
        if request.user.Is_Teacher:
            return redirect('teacher_home')
        if request.user.Is_Parent:
            return redirect('parent_home')
        else:
            msg = "Sorry you aren't assigned to any member type. User must be assigned to a member type\
                to go to their respective dashboard. Please request your center admin or super admin to assign you as one type of member"
            return render(request, "WebApp/splash_page.html", {'msg': msg})

    else:
        return render(request, "WebApp/splash_page.html")


def editprofile(request):
    if not request.user.is_authenticated:
        return HttpResponse("you are not authenticated", {'error_message': 'Error Message Customize here'})

    post = get_object_or_404(MemberInfo, pk=request.user.id)
    if request.method == "POST":

        form = UserUpdateForm(request.POST, request.FILES, instance=post)

        # if request.user.isAdmin:
        #     form = UserUpdateFormForAdmin(request.POST, request.FILES, instance=post)

        if form.is_valid():
            # post.date_last_update = datetime.now()
            post.save()
            return redirect('start')
    else:

        # form = UserUpdateForm(instance=post)
        form = UserUpdateForm(request.POST, request.FILES, instance=post)

        # if request.user.isAdmin == 1:
        #     form = UserUpdateFormForAdmin(instance=post)

    return render(request, 'registration/editprofile.html', {'form': form})


class register(CreateView):
    model = MemberInfo
    form_class = UserRegisterForm
    success_url = reverse_lazy('loginsuccess')
    template_name = 'registration/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['centers'] = CenterInfo.objects.all()
        return context


def change_password_others(request, pk):
    if request.method == 'POST':
        form = ChangeOthersPasswordForm(request.POST)
        if form.is_valid():
            # user = form.save()
            user = MemberInfo.objects.get(pk=pk)
            print(form.cleaned_data.get("password"), "  of user", user.username)
            user.set_password(form.cleaned_data.get("password"))
            user.save()

            # update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')

            return redirect('user_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ChangeOthersPasswordForm()
    return render(request, 'registration/change_password.html', {
        'form': form, 'usr': MemberInfo.objects.get(pk=pk)
    })


def loginsuccess(request):
    return render(request, "registration/registrationsuccessful.html")


class CenterInfoListView(ListView):
    model = CenterInfo


class CenterInfoCreateView(CreateView):
    model = CenterInfo
    form_class = CenterInfoForm


class CenterInfoDetailView(DetailView):
    model = CenterInfo


class CenterInfoUpdateView(UpdateView):
    model = CenterInfo
    form_class = CenterInfoForm


def CenterInfoDeleteView(request, pk):
    CenterInfo.objects.filter(pk=pk).delete()
    return redirect("centerinfo_list")


class MemberInfoListView(ListView):
    model = MemberInfo

    def get_queryset(self):
        return MemberInfo.objects.filter(Center_Code=self.request.user.Center_Code,Use_Flag=True)


class MemberInfoListViewInactive(ListView):
    model = MemberInfo
    template_name = 'WebApp/memberinfo_list_inactive.html'

    def get_queryset(self):
        return MemberInfo.objects.filter(Center_Code=self.request.user.Center_Code,Use_Flag=False)



class MemberInfoCreateView(CreateView):
    model = MemberInfo
    form_class = MemberInfoForm


# ________________________________________________________


class PasswordChangeView(PasswordContextMixin, FormView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('user_profile')
    template_name = 'registration/password_change_form.html'
    title = _('Password change')

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        # Updating the password logs out all other sessions for the user
        # except the current one.
        update_session_auth_hash(self.request, form.user)

        messages.success(self.request,
                         'Your password was successfully updated! You can login with your new credentials')

        return super().form_valid(form)


class MemberInfoDetailView(DetailView):
    model = MemberInfo


class MemberInfoUpdateView(UpdateView):
    model = MemberInfo
    form_class = MemberInfoForm


class MemberInfoDeleteView(DeleteView):
    model = MemberInfo
    success_url = reverse_lazy('memberinfo_list')

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except:
            messages.error(request,
                           "You can't delete this user instead you can turn off the status value which will disable the user.")
            return redirect('memberinfo_list')


# def MemberInfoDeleteView(request, pk):
#     MemberInfo.objects.filter(pk=pk).delete()


class CourseInfoListView(ListView):
    model = CourseInfo
    paginate_by = 8

    def get_queryset(self):
        qs = self.model.objects.all()

        query = self.request.GET.get('query')
        if query:
            qs = qs.filter(Course_Name__contains=query)
            if not len(qs):
                messages.error(self.request, 'Search not found')
        qs = qs.order_by("-id")  # you don't need this if you set up your ordering on the model
        return qs


class CourseInfoCreateView(CreateView):
    model = CourseInfo
    form_class = CourseInfoForm


class CourseInfoDetailView(DetailView):
    model = CourseInfo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chapters'] = ChapterInfo.objects.filter(Course_Code=self.kwargs.get('pk')).order_by('Chapter_No')
        context['surveycount'] = SurveyInfo.objects.filter(Course_Code=self.kwargs.get('pk')).count()
        context['quizcount'] = Question.objects.filter(course_code=self.kwargs.get('pk')).count()

        return context


class CourseInfoUpdateView(UpdateView):
    model = CourseInfo
    form_class = CourseInfoForm


class ChapterInfoListView(ListView):
    model = ChapterInfo


class ChapterInfoCreateView(CreateView):
    model = ChapterInfo
    form_class = ChapterInfoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Course_Code'] = get_object_or_404(CourseInfo, pk=self.kwargs.get('course'))
        return context


class ChapterInfoCreateViewAjax(AjaxableResponseMixin, CreateView):
    model = ChapterInfo
    form_class = ChapterInfoForm
    template_name = 'ajax/chapterinfo_form_ajax.html'

    def post(self, request, *args, **kwargs):
        Obj = ChapterInfo()
        Obj.Chapter_No = request.POST["Chapter_No"]
        Obj.Chapter_Name = request.POST["Chapter_Name"]
        Obj.Summary = request.POST["Summary"]
        # print(request.POST["Use_Flag"])
        if request.POST["Use_Flag"] == 'true':
            Obj.Use_Flag = True
        else:
            Obj.Use_Flag = False
        Obj.Course_Code = CourseInfo.objects.get(pk=request.POST["Course_Code"])
        Obj.Register_Agent = MemberInfo.objects.get(pk=request.POST["Register_Agent"])
        Obj.save()

        return JsonResponse(
            data={'Message': 'Success'}
        )


class ChapterInfoDetailView(DetailView):
    model = ChapterInfo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assignments'] = AssignmentInfo.objects.filter(Chapter_Code=self.kwargs.get('pk'))
        return context


class CourseForum(ListView):
    model = Thread
    paginate_by = 20
    template_name = 'courseinfo/Course_Forum.html'
    context_object_name = 'threads'

    def get_queryset(self):
        return Thread.objects.visible().filter(
            topic__id=self.kwargs.get('course.pk')
        ).select_related(
            'user', 'topic'
        ).prefetch_related(
            'user__forum_avatar'
        ).order_by(
            *['order', get_thread_ordering(self.request)]
        )

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        print(self.kwargs.get('pk'))
        context['topic'] = topic = Topic.objects.get(pk=self.kwargs.get('pk'))
        context['title'] = context['panel_title'] = topic.title
        context['show_order'] = True
        return context


class ChapterInfoUpdateView(UpdateView):
    model = ChapterInfo
    form_class = ChapterInfoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Course_Code'] = get_object_or_404(CourseInfo, pk=self.kwargs.get('course'))
        return context


class ChapterContentsInfoListView(ListView):
    model = ChapterContentsInfo


class ChapterContentsInfoCreateView(CreateView):
    model = ChapterContentsInfo
    form_class = ChapterContentsInfoForm


class ChapterContentsInfoDetailView(DetailView):
    model = ChapterContentsInfo


class ChapterContentsInfoUpdateView(UpdateView):
    model = ChapterContentsInfo
    form_class = ChapterContentsInfoForm


class ChapterMissonCheckCardListView(ListView):
    model = ChapterMissonCheckCard


class ChapterMissonCheckCardCreateView(CreateView):
    model = ChapterMissonCheckCard
    form_class = ChapterMissonCheckCardForm


class ChapterMissonCheckCardDetailView(DetailView):
    model = ChapterMissonCheckCard


class ChapterMissonCheckCardUpdateView(UpdateView):
    model = ChapterMissonCheckCard
    form_class = ChapterMissonCheckCardForm


class ChapterMissonCheckItemListView(ListView):
    model = ChapterMissonCheckItem


class ChapterMissonCheckItemCreateView(CreateView):
    model = ChapterMissonCheckItem
    form_class = ChapterMissonCheckItemForm


class ChapterMissonCheckItemDetailView(DetailView):
    model = ChapterMissonCheckItem


class ChapterMissonCheckItemUpdateView(UpdateView):
    model = ChapterMissonCheckItem
    form_class = ChapterMissonCheckItemForm


class SessionInfoCreateViewPopup(CreateView):
    model = SessionInfo
    form_class = SessionInfoForm
    template_name = 'popup/sessioninfoformpopup.html'


class InningGroupCreateViewPopup(CreateView):
    model = SessionInfo
    form_class = SessionInfoForm
    template_name = 'popup/inninggroupformpopup.html'


class GroupMappingCreateViewPopup(CreateView):
    model = SessionInfo
    form_class = SessionInfoForm
    template_name = 'popup/groupmappingformpopup.html'


class SessionInfoListView(ListView):
    model = SessionInfo


class SessionInfoCreateView(CreateView):
    model = SessionInfo
    form_class = SessionInfoForm


class SessionInfoDetailView(DetailView):
    model = SessionInfo


class SessionInfoUpdateView(UpdateView):
    model = SessionInfo
    form_class = SessionInfoForm


class InningInfoListView(ListView):
    model = InningInfo


class InningInfoCreateView(CreateView):
    # template_name = "WebApp/inninginfo_form.html"
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     form = InningInfoForm()
    #     context['form'] = form
    #     return context
    model = InningInfo
    form_class = InningInfoForm
    # form_classes = {
    #                 # 'sessioninfoform': SessionInfoForm,
    #                 # 'groupmappingform': GroupMappingForm,
    #                 # 'inninggroupform': InningGroupForm,
    #                 'inninginfoform':InningInfoForm
    #                 }


class InningInfoDetailView(DetailView):
    model = InningInfo


class InningInfoUpdateView(UpdateView):
    model = InningInfo
    form_class = InningInfoForm


class InningGroupListView(ListView):
    model = InningGroup


class InningGroupCreateView(CreateView):
    model = InningGroup
    form_class = InningGroupForm


class InningGroupCreateAjax(AjaxableResponseMixin, CreateView):
    model = InningGroup
    form_class = InningGroupForm
    template_name = 'ajax/inninggroup_form_ajax.html'


class InningInfoCreateSessionAjax(AjaxableResponseMixin, CreateView):
    model = SessionInfo
    form_class = SessionInfoForm
    template_name = 'ajax/sessioncreate_form_ajax.html'


class InningGroupDetailView(DetailView):
    model = InningGroup


class InningGroupUpdateView(UpdateView):
    model = InningGroup
    form_class = InningGroupForm


class GroupCreateSessionAjax(AjaxableResponseMixin, CreateView):
    model = GroupMapping
    form_class = GroupMappingForm
    template_name = 'ajax/groupcreate_form_ajax.html'


class GroupMappingListView(ListView):
    model = GroupMapping


class GroupMappingCreateView(CreateView):
    model = GroupMapping
    form_class = GroupMappingForm
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['Inning_Name'] = get_object_or_404(InningInfo, pk=self.kwargs.get('inning_name'))
    #     return context


class GroupMappingDetailView(DetailView):
    model = GroupMapping


class GroupMappingUpdateView(UpdateView):
    model = GroupMapping
    form_class = GroupMappingForm
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['Inning_Name'] = get_object_or_404(InningInfo, pk=self.kwargs.get('inning_name'))
    #     return context


# class OmrQuestionInfoListView(ListView):
#     model = OmrQuestionInfo
#
#
# class OmrQuestionInfoCreateView(CreateView):
#     model = OmrQuestionInfo
#     form_class = OmrQuestionInfoForm
#
#
# class OmrQuestionInfoDetailView(DetailView):
#     model = OmrQuestionInfo
#
#
# class OmrQuestionInfoUpdateView(UpdateView):
#     model = OmrQuestionInfo
#     form_class = OmrQuestionInfoForm


class QuizInfoListView(ListView):
    model = QuizInfo


class QuizInfoCreateView(CreateView):
    model = QuizInfo
    form_class = QuizInfoForm


class QuizInfoDetailView(DetailView):
    model = QuizInfo


class QuizInfoUpdateView(UpdateView):
    model = QuizInfo
    form_class = QuizInfoForm


# AssignmentInfoViews
class AssignmentInfoListView(ListView):
    model = AssignmentInfo


class AssignmentInfoCreateView(CreateView):
    model = AssignmentInfo
    form_class = AssignmentInfoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Course_Code'] = get_object_or_404(CourseInfo, pk=self.kwargs.get('course'))
        context['Chapter_No'] = get_object_or_404(ChapterInfo, pk=self.kwargs.get('chapter'))
        return context


class AssignmentInfoCreateViewAjax(AjaxableResponseMixin, CreateView):
    model = AssignmentInfo
    form_class = AssignmentInfoForm
    template_name = 'ajax/assignmentinfo_form_ajax.html'

    def post(self, request, *args, **kwargs):
        Obj = AssignmentInfo()
        Obj.Assignment_Topic = request.POST["Assignment_Topic"]
        Obj.Assignment_Deadline = request.POST["Assignment_Deadline"]
        Obj.Course_Code = CourseInfo.objects.get(pk=request.POST["Course_Code"])
        Obj.Chapter_Code = ChapterInfo.objects.get(id=request.POST["Chapter_Code"])
        Obj.Register_Agent = MemberInfo.objects.get(pk=request.POST["Register_Agent"])
        Obj.save()

        return JsonResponse(
            data={'Message': 'Success'}
        )

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['Course_Code'] = get_object_or_404(CourseInfo, pk=self.kwargs.get('course'))
    #     context['Chapter_No'] = get_object_or_404(ChapterInfo, pk=self.kwargs.get('chapter'))
    #     return context


class AssignmentInfoDetailView(DetailView):
    model = AssignmentInfo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Questions'] = QuestionInfo.objects.filter(Assignment_Code=self.kwargs.get('pk'))
        context['Course_Code'] = get_object_or_404(CourseInfo, pk=self.kwargs.get('course'))
        context['Chapter_No'] = get_object_or_404(ChapterInfo, pk=self.kwargs.get('chapter'))
        # context['Assignment_Code'] = get_object_or_404(AssignmentInfo, pk=self.kwargs.get('assignment'))
        return context


class AssignmentInfoUpdateView(UpdateView):
    model = AssignmentInfo
    form_class = AssignmentInfoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Course_Code'] = get_object_or_404(CourseInfo, pk=self.kwargs.get('course'))
        context['Chapter_No'] = get_object_or_404(ChapterInfo, pk=self.kwargs.get('chapter'))
        return context


class QuestionInfoListView(ListView):
    model = QuestionInfo


class QuestionInfoCreateView(CreateView):
    model = QuestionInfo
    form_class = QuestionInfoForm

    # success_url = 'questioninfo_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Course_Code'] = get_object_or_404(CourseInfo, pk=self.kwargs.get('course'))
        context['Chapter_No'] = get_object_or_404(ChapterInfo, pk=self.kwargs.get('chapter'))
        context['Assignment_Code'] = get_object_or_404(AssignmentInfo, pk=self.kwargs.get('assignment'))
        return context


class QuestionInfoCreateViewAjax(AjaxableResponseMixin, CreateView):
    model = QuestionInfo
    form_class = QuestionInfoForm
    template_name = 'ajax/questioninfo_form_ajax.html'

    def post(self, request, *args, **kwargs):
        Obj = QuestionInfo()
        Obj.Question_Title = request.POST["Question_Title"]
        Obj.Question_Score = request.POST["Question_Score"]
        Obj.Question_Description = request.POST["Question_Description"]
        Obj.Answer_Type = request.POST["Answer_Type"]
        Obj.Question_Media_File = request.POST["Question_Media_File"]
        if request.POST["Use_Flag"] == 'true':
            Obj.Use_Flag = True
        else:
            Obj.Use_Flag = False
        Obj.Register_Agent = MemberInfo.objects.get(pk=request.POST["Register_Agent"])
        Obj.Assignment_Code = AssignmentInfo.objects.get(pk=request.POST["Assignment_Code"])
        Obj.save()

        return JsonResponse(
            data={'Message': 'Success'}
        )


class QuestionInfoDetailView(DetailView):
    model = QuestionInfo


class QuestionInfoUpdateView(UpdateView):
    model = QuestionInfo
    form_class = QuestionInfoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Course_Code'] = get_object_or_404(CourseInfo, pk=self.kwargs.get('course'))
        context['Chapter_No'] = get_object_or_404(ChapterInfo, pk=self.kwargs.get('chapter'))
        context['Assignment_Code'] = get_object_or_404(AssignmentInfo, pk=self.kwargs.get('assignment'))
        return context


class AssignAssignmentInfoListView(ListView):
    model = AssignAssignmentInfo


class AssignAssignmentInfoCreateView(CreateView):
    model = AssignAssignmentInfo
    form_class = AssignAssignmentInfoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Inning_Code'] = get_object_or_404(InningInfo, pk=self.kwargs.get('session'))
        context['Assignment_Code'] = get_object_or_404(AssignmentInfo, pk=self.kwargs.get('assignment'))
        return context


class AssignAssignmentInfoDetailView(DetailView):
    model = AssignAssignmentInfo


class AssignAssignmentInfoUpdateView(UpdateView):
    model = AssignAssignmentInfo
    form_class = AssignAssignmentInfoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Inning_Code'] = get_object_or_404(InningInfo, pk=self.kwargs.get('session'))
        context['Assignment_Code'] = get_object_or_404(AssignmentInfo, pk=self.kwargs.get('assignment'))
        return context


# class AssignQuestionInfoListView(ListView):
#     model = AssignQuestionInfo
#
#
# class AssignQuestionInfoCreateView(CreateView):
#     model = AssignQuestionInfo
#     form_class = AssignQuestionInfoForm
#
#
# class AssignQuestionInfoDetailView(DetailView):
#     model = AssignQuestionInfo
#
#
# class AssignQuestionInfoUpdateView(UpdateView):
#     model = AssignQuestionInfo
#     form_class = AssignQuestionInfoForm


class AssignAnswerInfoListView(ListView):
    model = AssignAnswerInfo


class AssignAnswerInfoCreateView(CreateView):
    model = AssignAnswerInfo
    form_class = AssignAnswerInfoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Question_Code'] = get_object_or_404(QuestionInfo, pk=self.kwargs.get('questioncode'))
        return context


class AssignAnswerInfoDetailView(DetailView):
    model = AssignAnswerInfo


class AssignAnswerInfoUpdateView(UpdateView):
    model = AssignAnswerInfo
    form_class = AssignAnswerInfoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Question_Code'] = get_object_or_404(QuestionInfo, pk=self.kwargs.get('questioncode'))
        return context


class BoardInfoListView(ListView):
    model = BoardInfo


class BoardInfoCreateView(CreateView):
    model = BoardInfo
    form_class = BoardInfoForm


class BoardInfoDetailView(DetailView):
    model = BoardInfo


class BoardInfoUpdateView(UpdateView):
    model = BoardInfo
    form_class = BoardInfoForm


class BoardContentInfoListView(ListView):
    model = BoardContentInfo


class BoardContentInfoCreateView(CreateView):
    model = BoardContentInfo
    form_class = BoardContentInfoForm


class BoardContentInfoDetailView(DetailView):
    model = BoardContentInfo


class BoardContentInfoUpdateView(UpdateView):
    model = BoardContentInfo
    form_class = BoardContentInfoForm


class ChapterContentMediaListView(ListView):
    model = ChapterContentMedia


class ChapterContentMediaCreateView(CreateView):
    model = ChapterContentMedia
    form_class = ChapterContentMediaForm


class ChapterContentMediaDetailView(DetailView):
    model = ChapterContentMedia


class ChapterContentMediaUpdateView(UpdateView):
    model = ChapterContentMedia
    form_class = ChapterContentMediaForm


class ChapterImgInfoListView(ListView):
    model = ChapterImgInfo


class ChapterImgInfoCreateView(CreateView):
    model = ChapterImgInfo
    form_class = ChapterImgInfoForm


class ChapterImgInfoDetailView(DetailView):
    model = ChapterImgInfo


class ChapterImgInfoUpdateView(UpdateView):
    model = ChapterImgInfo
    form_class = ChapterImgInfoForm


class ChapterMissonCheckListView(ListView):
    model = ChapterMissonCheck


class ChapterMissonCheckCreateView(CreateView):
    model = ChapterMissonCheck
    form_class = ChapterMissonCheckForm


class ChapterMissonCheckDetailView(DetailView):
    model = ChapterMissonCheck


class ChapterMissonCheckUpdateView(UpdateView):
    model = ChapterMissonCheck
    form_class = ChapterMissonCheckForm


class ChapterWriteListView(ListView):
    model = ChapterWrite


class ChapterWriteCreateView(CreateView):
    model = ChapterWrite
    form_class = ChapterWriteForm


class ChapterWriteDetailView(DetailView):
    model = ChapterWrite


class ChapterWriteUpdateView(UpdateView):
    model = ChapterWrite
    form_class = ChapterWriteForm


class LearningNoteListView(ListView):
    model = LearningNote


class LearningNoteCreateView(CreateView):
    model = LearningNote
    form_class = LearningNoteForm


class LearningNoteDetailView(DetailView):
    model = LearningNote


class LearningNoteUpdateView(UpdateView):
    model = LearningNote
    form_class = LearningNoteForm


class CourseUbtInfoListView(ListView):
    model = CourseUbtInfo


class CourseUbtInfoCreateView(CreateView):
    model = CourseUbtInfo
    form_class = CourseUbtInfoForm


class CourseUbtInfoDetailView(DetailView):
    model = CourseUbtInfo


class CourseUbtInfoUpdateView(UpdateView):
    model = CourseUbtInfo
    form_class = CourseUbtInfoForm


class LessonInfoListView(ListView):
    model = LessonInfo


class LessonInfoCreateView(CreateView):
    model = LessonInfo
    form_class = LessonInfoForm


class LessonInfoDetailView(DetailView):
    model = LessonInfo


class LessonInfoUpdateView(UpdateView):
    model = LessonInfo
    form_class = LessonInfoForm


class LessonLogListView(ListView):
    model = LessonLog


class LessonLogCreateView(CreateView):
    model = LessonLog
    form_class = LessonLogForm


class LessonLogDetailView(DetailView):
    model = LessonLog


class LessonLogUpdateView(UpdateView):
    model = LessonLog
    form_class = LessonLogForm


class MemberGroupListView(ListView):
    model = MemberGroup


class MemberGroupCreateView(CreateView):
    model = MemberGroup
    form_class = MemberGroupForm


class MemberGroupDetailView(DetailView):
    model = MemberGroup


class MemberGroupUpdateView(UpdateView):
    model = MemberGroup
    form_class = MemberGroupForm


class MessageInfoListView(ListView):
    model = MessageInfo


class MessageInfoCreateView(CreateView):
    model = MessageInfo
    form_class = MessageInfoForm


class MessageInfoDetailView(DetailView):
    model = MessageInfo


class MessageInfoUpdateView(UpdateView):
    model = MessageInfo
    form_class = MessageInfoForm


# class OmrAnswerInfoListView(ListView):
#     model = OmrAnswerInfo
#
#
# class OmrAnswerInfoCreateView(CreateView):
#     model = OmrAnswerInfo
#     form_class = OmrAnswerInfoForm
#
#
# class OmrAnswerInfoDetailView(DetailView):
#     model = OmrAnswerInfo
#
#
# class OmrAnswerInfoUpdateView(UpdateView):
#     model = OmrAnswerInfo
#     form_class = OmrAnswerInfoForm
#
#
# class OmrAssignInfoListView(ListView):
#     model = OmrAssignInfo
#
#
# class OmrAssignInfoCreateView(CreateView):
#     model = OmrAssignInfo
#     form_class = OmrAssignInfoForm
#
#
# class OmrAssignInfoDetailView(DetailView):
#     model = OmrAssignInfo
#
#
# class OmrAssignInfoUpdateView(UpdateView):
#     model = OmrAssignInfo
#     form_class = OmrAssignInfoForm
#
#
# class OmrExampleInfoListView(ListView):
#     model = OmrExampleInfo
#
#
# class OmrExampleInfoCreateView(CreateView):
#     model = OmrExampleInfo
#     form_class = OmrExampleInfoForm
#
#
# class OmrExampleInfoDetailView(DetailView):
#     model = OmrExampleInfo
#
#
# class OmrExampleInfoUpdateView(UpdateView):
#     model = OmrExampleInfo
#     form_class = OmrExampleInfoForm


# class QAnswerLogListView(ListView):
#     model = QAnswerLog

#
# class QAnswerLogCreateView(CreateView):
#     model = QAnswerLog
#     form_class = QAnswerLogForm

#
# class QAnswerLogDetailView(DetailView):
#     model = QAnswerLog
#
# #
# class QAnswerLogUpdateView(UpdateView):
#     model = QAnswerLog
#     form_class = QAnswerLogForm


class QExampleInfoListView(ListView):
    model = QExampleInfo


class QExampleInfoCreateView(CreateView):
    model = QExampleInfo
    form_class = QExampleInfoForm


class QExampleInfoDetailView(DetailView):
    model = QExampleInfo


class QExampleInfoUpdateView(UpdateView):
    model = QExampleInfo
    form_class = QExampleInfoForm


class QuizAnswerInfoListView(ListView):
    model = QuizAnswerInfo


class QuizAnswerInfoCreateView(CreateView):
    model = QuizAnswerInfo
    form_class = QuizAnswerInfoForm


class QuizAnswerInfoDetailView(DetailView):
    model = QuizAnswerInfo


class QuizAnswerInfoUpdateView(UpdateView):
    model = QuizAnswerInfo
    form_class = QuizAnswerInfoForm


class QuizExampleInfoListView(ListView):
    model = QuizExampleInfo


class QuizExampleInfoCreateView(CreateView):
    model = QuizExampleInfo
    form_class = QuizExampleInfoForm


class QuizExampleInfoDetailView(DetailView):
    model = QuizExampleInfo


class QuizExampleInfoUpdateView(UpdateView):
    model = QuizExampleInfo
    form_class = QuizExampleInfoForm


class ScheduleInfoListView(ListView):
    model = ScheduleInfo


class ScheduleInfoCreateView(CreateView):
    model = ScheduleInfo
    form_class = ScheduleInfoForm


class ScheduleInfoDetailView(DetailView):
    model = ScheduleInfo


class ScheduleInfoUpdateView(UpdateView):
    model = ScheduleInfo
    form_class = ScheduleInfoForm


class TalkMemberListView(ListView):
    model = TalkMember


class TalkMemberCreateView(CreateView):
    model = TalkMember
    form_class = TalkMemberForm


class TalkMemberDetailView(DetailView):
    model = TalkMember


class TalkMemberUpdateView(UpdateView):
    model = TalkMember
    form_class = TalkMemberForm


class TalkRoomListView(ListView):
    model = TalkRoom


class TalkRoomCreateView(CreateView):
    model = TalkRoom
    form_class = TalkRoomForm


class TalkRoomDetailView(DetailView):
    model = TalkRoom


class TalkRoomUpdateView(UpdateView):
    model = TalkRoom
    form_class = TalkRoomForm


class TalkMessageListView(ListView):
    model = TalkMessage


class TalkMessageCreateView(CreateView):
    model = TalkMessage
    form_class = TalkMessageForm


class TalkMessageDetailView(DetailView):
    model = TalkMessage


class TalkMessageUpdateView(UpdateView):
    model = TalkMessage
    form_class = TalkMessageForm


class TalkMessageReadListView(ListView):
    model = TalkMessageRead


class TalkMessageReadCreateView(CreateView):
    model = TalkMessageRead
    form_class = TalkMessageReadForm


class TalkMessageReadDetailView(DetailView):
    model = TalkMessageRead


class TalkMessageReadUpdateView(UpdateView):
    model = TalkMessageRead
    form_class = TalkMessageReadForm


class TodoInfoListView(ListView):
    model = TodoInfo


class TodoInfoCreateView(CreateView):
    model = TodoInfo
    form_class = TodoInfoForm


class TodoInfoDetailView(DetailView):
    model = TodoInfo


class TodoInfoUpdateView(UpdateView):
    model = TodoInfo
    form_class = TodoInfoForm


class TodoTInfoListView(ListView):
    model = TodoTInfo


class TodoTInfoCreateView(CreateView):
    model = TodoTInfo
    form_class = TodoTInfoForm


class TodoTInfoDetailView(DetailView):
    model = TodoTInfo


class TodoTInfoUpdateView(UpdateView):
    model = TodoTInfo
    form_class = TodoTInfoForm


def question(request):
    return render(request, 'WebApp/question.html')


def polls(request):
    return render(request, 'WebApp/polls.html')


# chapter builder code starts from here

from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import json
from django.http import Http404, HttpResponse
from PIL import Image


def chapterviewer(request):
    if request.method == "GET":
        path = settings.MEDIA_ROOT
        chapterID = request.GET['chapterID']
        chapterobj = ChapterInfo.objects.get(id=chapterID)
        courseID = chapterobj.Course_Code.id
        try:
            with open(path + '/chapterBuilder/' + str(courseID) + '/' + str(chapterID) + '/' + str(
                    chapterID) + '.txt') as json_file:
                data = json.load(json_file)
        except Exception as e:
            print(e)
        return JsonResponse({'data': data})


def chapterpagebuilder(request, course, chapter):
    chaptertitle = ChapterInfo.objects.get(id=chapter).Chapter_Name
    path = settings.MEDIA_ROOT
    data = None
    try:
        with open(path + '/chapterBuilder/' + str(course) + '/' + str(chapter) + '/' + str(
                chapter) + '.txt') as json_file:
            data = json.load(json_file)
    except Exception as e:
        print(e)
    context = {
        'course': course,
        'chapter': chapter,
        'chaptertitle': chaptertitle,
        'file_path': path,
        'data': data
    }
    return render(request, 'WebApp/chapterbuilder.html', context)


@csrf_exempt
def save_file(request):
    if request.method == "POST":
        count = request.POST['count']
        chapterID = request.POST['chapterID']
        courseID = request.POST['courseID']
        path = ''
        for x in range(int(count)):
            if request.FILES['file-'+str(x)]:
                image = request.FILES['file-'+str(x)]
                if (image.size/1024) > 500:
                    return JsonResponse(data = {"message":"File size exceeds 2MB"}, status=500)
                path = settings.MEDIA_ROOT
                image
                # following is commented because filesystemstorage auto create directories if not exist
                # if not os.path.exists(os.path.join(path, 'chapterBuilder')):
                #     os.makedirs(os.path.join(path, 'chapterBuilder'))
                # if not os.path.exists(path+'chapterBuilder/'+courseID):
                #     os.makedirs(os.path.join(path, 'chapterBuilder/'+courseID))
                # if not os.path.exists(path+'chapterBuilder/'+courseID+'/'+chapterID):
                #     os.makedirs(os.path.join(path, 'chapterBuilder/'+courseID+'/'+chapterID))    
                fs = FileSystemStorage(location=path + '/chapterBuilder/' + courseID + '/' + chapterID)
                filename = fs.save(image.name, image)
        return JsonResponse(data={"message": "success"})


@csrf_exempt
def save_json(request):
    if request.method == "POST":
        jsondata = json.loads(request.POST['json'])
        chapterID = request.POST['chapterID']
        courseID = request.POST['courseID']
        path = settings.MEDIA_ROOT
        with open(path + '/chapterBuilder/' + courseID + '/' + chapterID + '/' + chapterID + '.txt', 'w') as outfile:
            json.dump(jsondata, outfile, indent=4)

        chapterObj = ChapterInfo.objects.get(id = chapterID)
        chapterObj.Page_Num = int(jsondata['numberofpages'])
        chapterObj.save()

        return JsonResponse(data = {"message":"Json Saved"})

# -------------------------------------------------------------------------------------------------------
