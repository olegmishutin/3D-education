from django.views import generic
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Group, Course


class CourseGroupList(generic.ListView):
    model = Group
    template_name = 'courses.html'
    context_object_name = 'groups'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['user_courses'] = self.request.user.courses.all() if self.request.user.is_authenticated else []
        return context


@login_required()
def addUserToCourse(request, pk):
    if request.method == 'POST':
        course = Course.objects.get(pk=pk)
        course.users.add(request.user)

        return redirect('courses:myCourses')
    return HttpResponse(status=404)


class UserCourseList(generic.ListView):
    model = Course
    template_name = 'user courses.html'
    context_object_name = 'courses'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super(UserCourseList, self).get(request, *args, **kwargs)
        return HttpResponse(status=401)

    def get_queryset(self):
        return self.request.user.courses.all()
