from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')


def login_view(request):
    return render(request, 'Login_page.html')


def signup_view(request):
    return render(request, 'Signup_page.html')

@login_required(login_url='login_view')
def about(request):
    return render(request, 'About_page.html')


def usercreate(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password1']
        cpassword = request.POST['password2']
        email = request.POST['email']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists.')
                return redirect('signup')
            else:
                User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email,
                )
                messages.success(request, 'Signup completed successfully.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')
    return redirect('signup')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'Welcome {username}')
            return redirect('about')
        else:
            messages.error(request, 'Invalid Username or Password. Try Again.')
            return redirect('login')
    else:
        return redirect('login')


def user_logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')