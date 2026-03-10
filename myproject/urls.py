from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path("admin/", admin.site.urls),

    path("", include("adminapp.urls")),
    path("", include("courses.urls")),
    path("", include("faculty.urls")),
    path("", include("student.urls")),

]