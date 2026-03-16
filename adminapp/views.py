from django.shortcuts import render, redirect
from .models import AdminUser
from courses.models import Course

def home(request):
    return render(request, "home.html")


def register_view(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        role = request.POST['role']

        if AdminUser.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already exists"
            })

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

        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        try:
            user = AdminUser.objects.get(
                username=username,
                password=password,
                role=role
            )

            request.session["username"] = user.username
            request.session["role"] = user.role

            if role == "admin":
                return redirect("admin_dashboard")

            elif role == "student":
                return redirect("student_dashboard")

            elif role == "faculty":
                return redirect("faculty_dashboard")

        except AdminUser.DoesNotExist:

            return render(request, "login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "login.html")


def admin_dashboard(request):

    if request.session.get("role") != "admin":
        return redirect("login")

    users = AdminUser.objects.all()
    courses = Course.objects.all()

    context = {
        "users": users,
        "courses": courses
    }

    return render(request, "admin_dashboard.html", context)
def logout_view(request):

    request.session.flush()

    return redirect("home")