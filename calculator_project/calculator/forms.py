from django import forms

OPERATOR_CHOICES = [
    ('add', 'Addition (+)'),
    ('subtract', 'Subtraction (-)'),
    ('multiply', 'Multiplication (*)'),
    ('divide', 'Division (/)'),
]


class FirstNumberForm(forms.Form):
    first_number = forms.CharField(
        label='First Number',
        widget=forms.TextInput(attrs={'placeholder': 'e.g. 10'}),
    )

    def clean_first_number(self):
        value = self.cleaned_data['first_number'].strip()
        try:
            return float(value)
        except ValueError:
            raise forms.ValidationError('Please enter a valid number.')


class SecondNumberForm(forms.Form):
    second_number = forms.CharField(
        label='Second Number',
        widget=forms.TextInput(attrs={'placeholder': 'e.g. 5'}),
    )

    def clean_second_number(self):
        value = self.cleaned_data['second_number'].strip()
        try:
            return float(value)
        except ValueError:
            raise forms.ValidationError('Please enter a valid number.')


class OperatorForm(forms.Form):
    operator = forms.ChoiceField(
        label='Select Operation',
        choices=OPERATOR_CHOICES,
        widget=forms.RadioSelect,
    )