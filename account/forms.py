from .models import Hesap
from django import forms



class HesapForm(forms.ModelForm):


    class Meta:
        model = Hesap
        field = (
            'Ad',
            'takim',
            'eMail',
            'created_by',
            'created_on',
            'aciklama',
        )

