from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'order_note', ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 5}),
            'order_note': forms.Textarea(attrs={'rows': 5, 'placeholder': 'if you have any note please enter here'}),
        }