from .models import Kullanici
from django import forms
from django.contrib.auth import authenticate

class KullanıcıForm(forms.ModelForm):
    class Meta:
        model = Kullanici

        # def __init__(self, *args, **kwargs):
        #     super(KullanıcıForm, self).__init__(*args, **kwargs)

        fields = [
            'TC',
            'e_Mail',
            'Ad',
            'Soyad',
            'Kullanıcı_adı',
            'Sifre',
            'Rol',
        ]


    def sifre_temizle(self):
        sifre = self.cleaned_data.get('Sifre')

        if sifre:
            if len(sifre) < 4:
                raise forms.ValidationError('Sifre 4 karakterden daha kısa olamaz')

        return sifre


    def mail_temizle(self):
        email = self.cleaned_data.get('e_Mail')
        if self.instance.id:
            if self.instance.e_Mail != email:
                if not Kullanici.objects.filter(e_Mail=self.cleaned_data.get('e_Mail')).exists():
                    return self.cleaned_data.get('e_Mail')
                else:
                    return forms.ValidationError("Mail kullanımda")

            else:
                return self.cleaned_data.get('e_Mail')

        else:
            if not Kullanici.objects.filter(e_Mail = self.cleaned_data.get('e_Mail')).exists():
                return self.cleaned_data.get('e_Mail')

            else:
                raise forms.ValidationError("Email kullanılıyor")


class Giris_form(forms.ModelForm):

    class Meta:
        model = Kullanici
        fields = [
            'e_Mail',
            'Sifre',
        ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(Giris_form, self).__init__(*args, **kwargs)

    def temizle(self):
        email = self.cleaned_data.get('e_Mail')
        sifre = self.cleaned_data.get('Sifre')

        if email and sifre:
            self.user = authenticate(e_Mail = email, Sifre = sifre)
            if self.user:
                if not self.user.is_active:
                    raise forms.ValidationError("kullanıcı aktif değil")

            else:
                raise forms.ValidationError("Email ve Sifre bulunmuyor")

        return self.cleaned_data

class Sifre_degistir(forms.Form):
    Sifre = forms.CharField(max_length=100)
    Yeni_sifre = forms.CharField(max_length=100)
    Onay = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(Sifre_degistir, self).__init__(*args, **kwargs)

    def onay_temizle(self):
        if len(self.cleaned_data.get('Onay')) < 4:
            raise forms.ValidationError("4 karakterden kısa olamaz")
        if self.data.get('Onay') != self.cleaned_data.get('Yeni_sifre'):
            raise forms.ValidationError("Sifreler birbiriyle uyuşmuyor")

        return self.data.get('Onay')





