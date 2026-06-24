from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = [
            'name',
            'price',
            'quantity',
            'category',
            'description'
        ]

        widgets = {

            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter product name'
            }),

            'price': forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Enter price'
            }),

            'quantity': forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Enter quantity'
            }),

            'category': forms.Select(attrs={
                'class':'form-select'
            }),

            'description': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Enter product description',
                'rows':4
            })

        }