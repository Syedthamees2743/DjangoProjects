from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course

        fields = "__all__"

        widgets = {
            "course_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Course Name"}
            ),
            "course_fees": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter Course Fees"}
            ),
        }