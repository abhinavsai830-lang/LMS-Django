from django.shortcuts import render, redirect
from .models import AdminUser


def home(request):
    return render(request, "home.html")


def register_view(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        phone = request.POST["phone"]
        role = request.POST["role"]

        AdminUser.objects.create(
            username=username,
            email=email,
            password=password,
            phone=phone,
            role=role
        )

        return redirect("login")

    return render(request, "register.html")


def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        role = request.POST["role"]

        try:
            user = AdminUser.objects.get(
                username=username,
                password=password,
                role=role
            )

            request.session["username"] = user.username
            request.session["role"] = user.role

            if user.role == "admin":
                return redirect("admin_dashboard")

            elif user.role == "student":
                return redirect("student_dashboard")

            elif user.role == "faculty":
                return redirect("faculty_dashboard")

        except AdminUser.DoesNotExist:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


def admin_dashboard(request):
    return render(request, "admin_dashboard.html")