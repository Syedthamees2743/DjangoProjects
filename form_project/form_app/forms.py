import re
from django import forms


class UserDetailsForm(forms.Form):
    name = forms.CharField(
        max_length=150,
        label='Full Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your full name',
        }),
        error_messages={
            'required': 'Please enter your name.',
            'max_length': 'Name cannot exceed 150 characters.',
        },
    )

    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@domain.com',
        }),
        error_messages={
            'required': 'Please enter your email address.',
            'invalid': 'Enter a valid email address.',
        },
    )

    phone = forms.CharField(
        max_length=20,
        label='Phone Number',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+1 (555) 123-4567',
        }),
        error_messages={
            'required': 'Please enter your phone number.',
        },
    )

    address = forms.CharField(
        label='Address',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Street, City, State, ZIP',
        }),
        error_messages={
            'required': 'Please enter your address.',
        },
    )

    additional_details = forms.CharField(
        required=False,
        label='Additional Details',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Any other information you would like to provide...',
        }),
    )

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not re.match(r"^[A-Za-z\s'\-]+$", name):
            raise forms.ValidationError(
                'Name should contain only letters, spaces, hyphens, or apostrophes.'
            )
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        if not re.match(r'^[\d\s\-\+\(\)]+$', phone):
            raise forms.ValidationError(
                'Phone number can only contain digits, spaces, +, -, (, and ).'
            )
        digit_count = sum(c.isdigit() for c in phone)
        if digit_count < 7:
            raise forms.ValidationError(
                'Phone number must contain at least 7 digits.'
            )
        return phone