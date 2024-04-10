from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
    path('courses/', views.CourseGroupList.as_view(), name='courses'),
    path('add-user-course/<int:pk>/', views.addUserToCourse, name='addUserToCourse'),
    path('my-courses/', views.UserCourseList.as_view(), name='myCourses')
]