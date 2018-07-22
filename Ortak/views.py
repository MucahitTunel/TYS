from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import Http404
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Ortak.models import Kullanici
from Ortak.forms import Giris_form, KullanıcıForm


def admin_required(function):
    def wrapper(request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            if user.is_superuser:
                return function(request, *args, **kwargs)
            else:
                raise Http404
        else:
            return redirect("Ortak:Giriş")
    return wrapper

@login_required
def home(request):
    return render(request, 'base.html')


@login_required
def profile(request):
    user = request.user
    user_obj = Kullanici.objects.get(id=user.id)
    return render(request, "profil.html", {'user_obj': user_obj})


# def giris_crm(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect('/')
#     if request.method == 'POST':
#         form = Giris_form(request.POST, request=request)
#         if form.is_valid():
#             user = authenticate(username = request.POST.get('e_Mail'), password = request.POST.get('Sifre'))
#             if user is not None:
#                 if user.is_active:
#                     login(request,user)
#                     return HttpResponseRedirect('/')
#                 else:
#                     return render(request,'giris.html',{'error':True, "mesaj":"Hesabınız aktif değil"})
#             else:
#                return render(request,'giris.html',{"error":True, "mesaj":"Kullanıcı adı veya şifre hatalı"})
#         else:
#            return render(request,'giris.html',{"error":True, "mesaj":"Lütfen formu düzgün bir şekilde doldurunuz"})
#
#     return render(request,'giris.html')



def giris_crm(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = Giris_form(request.POST, request=request)
        if not form.is_valid():
            user = authenticate(username = request.POST.get('e_Mail'), password = request.POST.get('Sifre'))
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/')
                else:
                    return render(request,'giris.html',{'error':True, "mesaj":"Hesabınız aktif değil"})
            else:
               return render(request,'giris.html',{"error":True, "mesaj":"Kullanıcı adı veya şifre hatalı"})
        else:
           return render(request,'giris.html',{"error":True, "mesaj":"Lütfen formu düzgün bir şekilde doldurunuz"})

    return render(request,'giris.html')


def sifremi_unuttum(request):

    return render(request,'sifremi-unuttum.html')


def cıkıs_crm(request):
    logout(request)
    request.session.flush()
    return redirect("Ortak:Giriş")


@admin_required
def kullanici_olustur(request):
    kullanici_form = KullanıcıForm()
    if request.method== 'POST':
        kullanici_form = KullanıcıForm(request.POST)
        if kullanici_form.is_valid():
            kullanici_form.save(commit=False)
            if request.POST.get('Sifre'):
                Kullanici.set_password(request.POST.get('Sifre'))
            Kullanici.save()
            return redirect("Ortak: kullanici_list")
        else:
            return render(request,'Ortak/kullanici_olustur.html',{'kullanici_form':kullanici_form, "errors":kullanici_form.errors})

    else:
        return render(request,'Ortak/kullanici_olustur.html', {'kullanici_form':kullanici_form})


@admin_required
def kullanici_listele(request):

    kullanicilar = Kullanici.nesne.all()#UserManager nesnesinden tüm kullanıcı bilgilerini alıyoruz

    # ad = request.POST.get('Ad')
    # soyad = request.POST.get('Soyad')
    # kullanici_adi = request.POST.get('Kullanıcı_adı')
    # eMail = request.POST.get('e_Mail')



    # if ad:
    #     kullanicilar = kullanicilar.filter(kullanicilar__icontains=ad)
    # if soyad:
    #     kullanicilar = kullanicilar.filter(kullanicilar__icontains=soyad)
    # if kullanici_adi:
    #     kullanicilar = kullanicilar.filter(kullanicilar__icontains=kullanici_adi)
    # if eMail:
    #     kullanicilar = kullanicilar.filter(kullanicilar__icontains=eMail)


    return render(request,'Ortak/kullanici_listele.html', {'kullanicilar':kullanicilar})



@admin_required
def kullanici_olustur(request):
    kullanici_form = KullanıcıForm()

    if request.method == 'POST':
        kullanici_form = KullanıcıForm(request.POST)
        if kullanici_form.is_valid():
            kullanici = kullanici_form.save(commit=False)
            if request.POST.get('Sifre'):
                kullanici.set_password(request.POST.get('Sifre'))
            kullanici.save()
            return redirect('Ortak:kullanici_list')
        else:
            return render(request,'Ortak/kullanici_olustur.html', {'kullanici_form':kullanici_form, 'errors':kullanici_form.errors})
    else:
        return render(request,'Ortak/kullanici_olustur.html', {'kullanici_form':kullanici_form})


@admin_required
def kullanici_goruntule(request, user_id):
    # users_list = Kullanici.objects.all()
    kullanici = Kullanici.nesne.get(id=user_id)

    return render(request, "Ortak/kullanici_goruntule.html", {'kullanici': kullanici})