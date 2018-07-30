from account.models import Hesap
from django import forms

class HesapForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        assigned_users = kwargs.pop('assigned_to', [])
        super(HesapForm, self).__init__(*args, **kwargs)
        # for field in self.fields.values():
        #     field.widget.attrs = {"class": "form-control"}
        # # self.fields['description'].widget.attrs.update({
        # #     'rows': '8'})
        self.fields['assigned_to'].queryset = assigned_users
        self.fields['assigned_to'].required = False
        self.fields['takim'].required = False

    class Meta:
        model = Hesap
        fields = [
            'Ad',
            'takim',
            'eMail',
            'assigned_to',
            'created_by',
            'aciklama',
        ]



