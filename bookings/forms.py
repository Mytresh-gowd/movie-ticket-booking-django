from django import forms

class BookingForm(forms.Form):
    customer_name = forms.CharField(
        max_length=100,
        label="Your Name"
    )