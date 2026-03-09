from django.shortcuts import render, redirect
from .models import AdminUser


def home(request):
    return render(request, 'home.html')


def register_view(request):
    if request.method == 'POST':
        print("REGISTER VIEW HIT")

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        role = request.POST['role']

        if not all([username, email, password, phone, role]):
            return render(request, 'register.html', {
                'error': 'Please enter all fields.'
            })

        # check duplicate username
        if AdminUser.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists'
            })




        AdminUser.objects.create(
            username=username,
            email=email,
            password=password,
            phone=phone,
            role=role
        )


        return render(request, 'welcome.html', {'username': username})

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        try:
            user = AdminUser.objects.get(
                username=use.gitignorername,
                password=password,
                role=role
            )
            request.session['username'] = user.username
            request.session['role'] = user.role
            if user.role =='admin':
                return redirect('admin_dashboard')
            elif user.role =='student':
                return redirect('student_dashboard')
            elif user.role =='faculty':
                return redirect('faculty_dashboard')
        except AdminUser.DoesNotExist:
            return render(request, 'login.html', {
                'error': 'Invalid credentials'
            })

    return render(request, 'login.html')


def admin_dashboard(request):
    if request.session.get('role')!='admin':
        return redirect('login')
        return redirect('admin_dashboard')
    return render(request, 'admin_dashboard.html')
    return render(request, 'admin_dashboard.html')

