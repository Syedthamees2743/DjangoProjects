
from django import forms

from formapp.models import Employee


class employeeforms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
