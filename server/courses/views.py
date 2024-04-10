from django.views import generic
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Group, Course


class CourseGroupList(generic.ListView):
    model = Group
    template_name = 'courses.html'
    context_object_name = 'groups'

    def get_queryset(self):
        return Group.objects.exclude(courses__users__in=[self.request.user])


@login_required()
def addUserToCourse(request, pk):
    if request.method == 'POST':
        course = Course.objects.get(pk=pk)
        course.users.add(request.user)

        return redirect('index')
    return HttpResponse(status=404)
