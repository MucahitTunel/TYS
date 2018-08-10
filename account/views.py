from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.models import Hesap
from Ortak.models import Kullanici, Takim
from account.forms import HesapForm
from bağlantı.models import Baglanti

# @login_required
def hesap_listele(request):
    hesaplar = Hesap.objects.all()
    return render(request, 'Hesaplar/hesap.html', {'hesaplar':hesaplar})

 # @login_required
def hesap_olustur(request):

    kullanıcı = Kullanici.nesne.filter(is_active = True).order_by('e_Mail')
    hesapForm = HesapForm(assigned_to=request.user)

    if request.method == 'POST':
        hesapForm = HesapForm(request.POST, assigned_to=request.user)

        if hesapForm.is_valid():
            hesap_object = hesapForm.save(commit=False)
            hesap_object.created_by = request.user
            hesap_object.save()

            if request.POST.get("Kaydet"):
                return redirect("accounts:liste")
        else:
            return render(request, 'Hesaplar/hesap_olustur.html', {
                'hesap_form': hesapForm,

            })

# @login_required
def hesap_goruntule(request, account_id):
    baglantilar = Baglanti.objects.get(id = account_id)
    takimlar = Takim.objects.all()
    kullanıcılar = Kullanici.nesne.filter(is_active = True).order_by('e_Mail')

    return render(request, 'Hesaplar/hesap_goruntule',{'baglantilar':baglantilar,
                                                       'takimlar':takimlar,
                                                       'kullanıcılar': kullanıcılar})


def hesap_duzenle(request, edit_id):
    hesap = get_object_or_404(Hesap, id = edit_id)

