from django.shortcuts import render, redirect
from .models import Course


def course_list(request):

    courses = Course.objects.all()

    return render(request, "courses.html", {"courses": courses})