from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.models import Hesap
from Ortak.models import Kullanici, Takim
from account.forms import HesapForm
from bağlantı.models import Baglanti

# @login_required
def hesap_listele(request):
    hesaplar = Hesap.objects.all()
    return render(request, 'hesap.html', {'hesaplar':hesaplar})

 # @login_required
def hesap_ekle(request):
    kullanıcı = Kullanici.nesne.filter(is_active = True).order_by('eMail')
    hesapForm = HesapForm(assigned_to=kullanıcı)

    if request.method == 'POST':
        hesapForm = HesapForm(request.POST, assigned_to=kullanıcı)

        if hesapForm.is_valid():
            hesap_object = hesapForm.save(commit=False)
            hesap_object.created_by = request.user
            hesap_object.save()

            if request.POST.get("YeniHesapKayıt"):
                return redirect("account:yeni_hesap")
            else:
                return redirect("accounts:liste")

        else:
            return render(request, 'Hesaplar/hesap_olustur.html', {
                'hesap_form': hesapForm,
                'kullanıcı': kullanıcı,
            })

# @login_required
def hesap_goruntule(request, account_id):
    baglantilar = Baglanti.objects.get(id = account_id)
    takimlar = Takim.objects.all()
    kullanıcılar = Kullanici.nesne.filter(is_active = True).order_by('e_Mail')


    return render(request, 'Hesaplar/hesap_goruntule',{'baglantilar':baglantilar,
                                                       'takimlar':takimlar,
                                                       'kullanıcılar': kullanıcılar})







