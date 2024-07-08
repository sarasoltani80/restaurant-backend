from django import forms
from .models import Sabad , Wallet , Vote

class SabadForm(forms.ModelForm):
    class Meta:
        model = Sabad
        fields = ["number"]

class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ["money"]

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ["price_rate" , "behdasht_rate" , "service_rate"]