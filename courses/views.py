from django.shortcuts import render, redirect
from .models import Course


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