from django.urls import path
from . import views

urlpatterns = [

    path(
        "faculty-dashboard/",
        views.faculty_dashboard,
        name="faculty_dashboard"
    ),

    path(
        "add-lecture/<int:course_id>/",
        views.add_lecture,
        name="add_lecture"
    ),
]