from django import forms
from .models import booking

class dateinput(forms.DateInput):
    input_type='date'
class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = '__all__'
        widgets={
            'booking_date':dateinput(),
        }

        labels={
        'p_name':'Patient name :',
        'p_phone':'Patient phone number :',
        'p_email':'Patient email :',
        'doc_name':'Doctor name :',
        'booking_date':'Booking date :'
        }        