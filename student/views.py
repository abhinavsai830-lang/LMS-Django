from django.shortcuts import render

from django.shortcuts import render, redirect
from courses.models import Course, Enrollment
from adminapp.models import AdminUser


def student_dashboard(request):

    username = request.session.get("username")

    student = AdminUser.objects.get(username=username)

    enrollments = Enrollment.objects.filter(student=student)

    return render(request, "student_dashboard.html", {
        "enrollments": enrollments
    })