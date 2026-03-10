from django.urls import path
from . import views

urlpatterns = [

    path("courses/", views.course_list, name="courses"),

    path("add-course/", views.add_course, name="add_course"),

]