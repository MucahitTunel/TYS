from .models import Baglanti
from django import forms

class BaglantiForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        assigned_users = kwargs.pop('assigned_to', [])
        contact_account = kwargs.pop('Hesap', [])
        super(BaglantiForm, self).__init__(*args, **kwargs)
        # for field in self.fields.values():
        #     field.widget.attrs = {"class": "form-control"}
        self.fields['assigned_to'].queryset = assigned_users
        self.fields['account'].queryset = contact_account
        self.fields['assigned_to'].required = False
        self.fields['takim'].required = False



    class Meta:
        model = Baglanti
        fields = [
            "Ad",
            "Soyad",
            "Hesap",
            "eMail",
            "assigned_to",
            "created_by",
        ]
