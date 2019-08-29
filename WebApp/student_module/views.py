# from django.shortcuts import render
#
#
# def start(request):
#     """Start page with a documentation.
#     """
#     # return render(request,"start.html")
#     return render(request, "student_module/homepage.html")

from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView

from WebApp.models import LectureInfo, GroupMapping, InningInfo, InningGroup, ChapterInfo, AssignmentInfo


def start(request):
    return render(request, 'student_module/dashboard.html')


# def mycourse(request):
#     return render(request, 'student_module/myCourse.html')


def quiz(request):
    return render(request, 'student_module/quiz.html')


def quizzes(request):
    return render(request, 'student_module/quizzes.html')


def calendar(request):
    return render(request, 'student_module/calendar.html')


# def coursedetail(request):
#     return render(request, 'student_module/course_detail.html')
# #
class MyCoursesListView(ListView):
    model = LectureInfo
    template_name = 'student_module/myCourse.html'

    paginate_by = 8

    def get_queryset(self):
        qs = self.model.objects.all()

        query = self.request.GET.get('query')
        if query:
            qs = qs.filter(Lecture_Name__contains=query)
            if not len(qs):
                messages.error(self.request, 'Search not found')
        qs = qs.order_by("-id")  # you don't need this if you set up your ordering on the model
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['GroupName'] = GroupMapping.objects.get(Students__id=self.request.user.id)
        context['Group'] = InningInfo.objects.get(Groups__id=context['GroupName'].id)
        # for course in context['Group']():
        #     context['Course'] = InningGroup.objects.filter(id=context['Group'].id)
        # context['Course'] = InningGroup.objects.filter(id=context['Group'].id)
        context['Course'] = context['Group'].Course_Group.all()
        # context['Course_Group'] = InningInfo.objects.get(Course_Group__id=context['Group'].Course_Group)
        # print(context['Group'].Course_Group)
        return context


class LectureInfoListView(ListView):
    model = LectureInfo
    template_name = 'student_module/lectureinfo_list.html'


class LectureInfoDetailView(DetailView):
    model = LectureInfo
    template_name = 'student_module/lectureinfo_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chapters'] = ChapterInfo.objects.filter(Lecture_Code=self.kwargs.get('pk'))
        return context

class ChapterInfoListView(ListView):
    model = ChapterInfo

class ChapterInfoDetailView(DetailView):
    model = ChapterInfo
    template_name = 'student_module/chapterinfo_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assignments'] = AssignmentInfo.objects.filter(Chapter_Code=self.kwargs.get('pk'))
        return context


def ProfileView(request):
    return render(request, 'student_module/profile.html')


def questions_student(request):
    return render(request, 'student_module/questions_student.html')


def polls_student(request):
    return render(request, 'student_module/polls_student.html')


def polls_student_view(request):
    return render(request, 'student_module/polls_student_view.html')
