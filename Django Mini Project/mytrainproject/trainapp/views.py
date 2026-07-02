from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from .forms import TrainForm, TicketForm, ProfileForm, EditUserForm
from .models import Train, Ticket, UserProfile
from datetime import date


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password != confirm_password:
                messages.error(request, 'Passwords do not match')
                return render(request, 'register.html', {'form': form})

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return render(request, 'register.html', {'form': form})

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return render(request, 'register.html', {'form': form})

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            subject = 'Registration Successful'
            message = 'Hello ' + username + '\n\nYour account has been created successfully.\nYou can now login to your account.'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=True)

            messages.success(request, 'Registration Successful! Please login.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successfully!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password')
                return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout Successfully!')
    return redirect('home')


def forgot_password(request):
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                request.session['reset_email'] = email
                messages.success(request, 'Email verified! Set your new password.')
                return redirect('reset_password')
            except User.DoesNotExist:
                messages.error(request, 'Email not found')
                return render(request, 'forgot_password.html', {'form': form})
    else:
        form = ForgotPasswordForm()
    return render(request, 'forgot_password.html', {'form': form})


def reset_password(request):
    if 'reset_email' not in request.session:
        return redirect('forgot_password')

    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']

            if new_password != confirm_password:
                messages.error(request, 'Passwords do not match')
                return render(request, 'reset_password.html', {'form': form})

            email = request.session['reset_email']
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            del request.session['reset_email']
            messages.success(request, 'Password reset successfully! Please login.')
            return redirect('login')
    else:
        form = ResetPasswordForm()
    return render(request, 'reset_password.html', {'form': form})


@login_required
def dashboard(request):
    total_tickets = Ticket.objects.filter(user=request.user).count()
    today = date.today()
    upcoming_trips = Ticket.objects.filter(user=request.user, travel_date__gte=today, is_cancelled=False).count()
    recent_bookings = Ticket.objects.filter(user=request.user).order_by('-id')[:5]

    context = {
        'total_tickets': total_tickets,
        'upcoming_trips': upcoming_trips,
        'recent_bookings': recent_bookings
    }
    return render(request, 'dashboard.html', context)


@login_required
def profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None
    return render(request, 'profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None

    if request.method == "POST":
        user_form = EditUserForm(request.POST, instance=request.user)
        if profile:
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        else:
            profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            if profile:
                profile_form.save()
            else:
                new_profile = profile_form.save(commit=False)
                new_profile.user = request.user
                new_profile.save()
            messages.success(request, 'Profile Updated Successfully!')
            return redirect('profile')
    else:
        user_form = EditUserForm(instance=request.user)
        if profile:
            profile_form = ProfileForm(instance=profile)
        else:
            profile_form = ProfileForm()

    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def train_list(request):
    display = Train.objects.all()
    return render(request, 'train_list.html', {'display': display})


@login_required
def add_train(request):
    if request.method == "POST":
        form = TrainForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Train Added Successfully!')
            return redirect('trainlist')
    else:
        form = TrainForm()
    return render(request, 'add_train.html', {'form': form})


@login_required
def edit_train(request, pk):
    train = Train.objects.get(id=pk)
    form = TrainForm(instance=train)
    return render(request, 'edit_train.html', {'form': form, 'train': train})


@login_required
def update_train(request, pk):
    train = Train.objects.get(id=pk)
    if request.method == "POST":
        form = TrainForm(request.POST, instance=train)
        if form.is_valid():
            form.save()
            messages.success(request, 'Train Updated Successfully!')
            return redirect('trainlist')
    return redirect('edit_train', pk=pk)


@login_required
def delete_train(request, pk):
    train = Train.objects.get(id=pk)
    train.delete()
    messages.success(request, 'Train Deleted Successfully!')
    return redirect('trainlist')


@login_required
def book_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            subject = 'Ticket Booked Successfully'
            message = 'Passenger Name: ' + ticket.passenger_name + '\nTrain: ' + ticket.train.train_name + '\nSeat Number: ' + ticket.seat_number + '\nTravel Date: ' + str(ticket.travel_date) + '\n\nYour booking is confirmed.'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [request.user.email], fail_silently=True)

            messages.success(request, 'Ticket Booked Successfully!')
            return redirect('ticketlist')
    else:
        form = TicketForm()
    return render(request, 'book_ticket.html', {'form': form})


@login_required
def ticket_list(request):
    display = Ticket.objects.filter(user=request.user).order_by('-id')
    return render(request, 'ticket_list.html', {'display': display})


@login_required
def edit_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    form = TicketForm(instance=ticket)
    return render(request, 'edit_ticket.html', {'form': form, 'ticket': ticket})


@login_required
def update_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ticket Updated Successfully!')
            return redirect('ticketlist')
    return redirect('edit_ticket', pk=pk)


@login_required
def cancel_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    ticket.is_cancelled = True
    ticket.save()

    subject = 'Ticket Cancelled Successfully'
    message = 'Passenger Name: ' + ticket.passenger_name + '\nTrain: ' + ticket.train.train_name + '\nSeat Number: ' + ticket.seat_number + '\nTravel Date: ' + str(ticket.travel_date) + '\n\nYour ticket has been cancelled.'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [request.user.email], fail_silently=True)

    messages.success(request, 'Ticket Cancelled Successfully!')
    return redirect('ticketlist')