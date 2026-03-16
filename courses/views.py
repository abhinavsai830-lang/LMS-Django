from .models import Course
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Enrollment
from adminapp.models import AdminUser


def course_list(request):

    courses = Course.objects.all()

    return render(request, "courses.html", {"courses": courses})
from django.shortcuts import render, redirect
from .models import Course


def add_course(request):

    if request.method == "POST":

        title = request.POST.get("title")
        description = request.POST.get("description")
        duration = request.POST.get("duration")
        price = request.POST.get("price")

        Course.objects.create(
            title=title,
            description=description,
            duration=duration,
            price=price
        )

        return redirect("admin_dashboard")

    return render(request, "add_course.html")
def edit_course(request, id):

    course = get_object_or_404(Course, id=id)

    if request.method == "POST":

        course.title = request.POST.get("title")
        course.description = request.POST.get("description")
        course.duration = request.POST.get("duration")
        course.price = request.POST.get("price")

        course.save()

        return redirect("admin_dashboard")

    return render(request, "edit_course.html", {"course": course})


def delete_course(request, id):

    course = get_object_or_404(Course, id=id)

    course.delete()

    return redirect("admin_dashboard")


def enroll_course(request, course_id):

    username = request.session.get("username")

    student = AdminUser.objects.get(username=username)

    course = Course.objects.get(id=course_id)

    Enrollment.objects.create(
        student=student,
        course=course
    )

    return redirect("student_dashboard")