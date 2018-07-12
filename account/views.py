from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Hesap
from Ortak.models import Kullanici, Takim
from .forms import HesapForm


@login_required
def hesap_listele(request):
    hesaplar = Hesap.objects.all()
    ad = request.POST.get('Ad')

    if ad:
        hesaplar = hesaplar.filter(ad__icontains = ad)


    return render(request, 'hesap.html', {'hesaplar':hesaplar})


@login_required
def hesap_ekle(request):
    kullanıcı = Kullanici.objects.filter(aktif_mi = True).order_by('eMail')
    hesapForm = HesapForm(assigned_to = kullanıcı)

    if request.method == 'POST':
        hesapForm = HesapForm(request.POST, assigned_to = kullanıcı)

        if hesapForm.is_valid():
            hesap_object = hesapForm.save(commit=False)
            hesap_object.created_by = request.user
            hesap_object.save()

            if request.POST.get("YeniHesapKayıt"):
                return redirect("account:yeni_hesap")
            else:
                return redirect("accounts:liste")

        else:
            return render(request, 'hesap_olustur.html', {
                'hesap_form': hesapForm,
                'kullanıcı': kullanıcı,
            })











