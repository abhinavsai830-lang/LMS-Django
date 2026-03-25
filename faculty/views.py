from django.shortcuts import render
from django.shortcuts import render, redirect
from courses.models import Course, Lecture


def faculty_dashboard(request):

    courses = Course.objects.all()

    return render(request, "faculty_dashboard.html", {
        "courses": courses
    })


def add_lecture(request, course_id):

    course = Course.objects.get(id=course_id)

    if request.method == "POST":

        title = request.POST.get("title")
        video_url = request.POST.get("video_url")
        material = request.FILES.get("material")

        Lecture.objects.create(
            course=course,
            title=title,
            video_url=video_url,
            material=material
        )

        return redirect("faculty_dashboard")

    return render(request, "add_lecture.html", {"course": course})