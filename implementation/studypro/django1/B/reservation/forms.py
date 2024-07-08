from django import forms
from . models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["phone" , "number" , "date" , "start_time" , "duration"]