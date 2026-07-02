from django import forms
from .models import Train, Ticket, UserProfile
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter first name"}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter last name"}
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter username"}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter email"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter password"}
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm password"}
        )
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter username"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter password"}
        )
    )


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter your email"}
        )
    )


class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter new password"}
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm new password"}
        )
    )


class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = [
            "train_number",
            "train_name",
            "source",
            "destination",
            "departure_time",
            "arrival_time",
            "total_seats",
        ]
        widgets = {
            "train_number": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter train number"}
            ),
            "train_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter train name"}
            ),
            "source": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter source station"}
            ),
            "destination": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter destination station",
                }
            ),
            "departure_time": forms.TimeInput(
                attrs={"type": "time", "class": "form-control"}
            ),
            "arrival_time": forms.TimeInput(
                attrs={"type": "time", "class": "form-control"}
            ),
            "total_seats": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter total seats"}
            ),
        }


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "passenger_name",
            "train",
            "travel_date",
            "seat_number",
            "class_type",
        ]

        widgets = {
            "passenger_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter passenger name"}
            ),
            "train": forms.Select(attrs={"class": "form-control"}),
            "travel_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "seat_number": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter seat number"}
            ),
            "class_type": forms.Select(attrs={"class": "form-control"}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["photo", "phone"]
        widgets = {
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter phone number"}
            ),
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter first name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter last name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter email"}
            ),
        }
