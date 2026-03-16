from django.urls import path
from . import views

urlpatterns = [

    path("courses/", views.course_list, name="courses"),
    path("add-course/", views.add_course, name="add_course"),

    path("edit-course/<int:id>/", views.edit_course, name="edit_course"),
    path("delete-course/<int:id>/", views.delete_course, name="delete_course"),
    path("enroll/<int:course_id>/", views.enroll_course, name="enroll_course"),

]