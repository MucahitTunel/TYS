from django.shortcuts import render
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
        if user.is_authenticated:
            if user.role == "Admin":
                return function(request, *args, **kwargs)
            else:
                raise Http404
        else:
            return redirect("common:login")
    return wrapper


@login_required
def home(request):
    return render(request, 'index.html')


@login_required
def profile(request):
    user = request.user
    user_obj = Kullanici.objects.get(id=user.id)
    return render(request, "profile.html", {'user_obj': user_obj})


def giris_crm(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = Giris_form(request.POST, request=request)
        if form.is_valid():
            user = authenticate(Kullanıcı_adı = request.POST.get('Kullanıcı_adı'), Sifre = request.POST.get('Sifre'))
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
    return render(request,'Ortak/sifremi-unuttum.html')


def cıkıs_crm(request):
    logout(request)
    request.session.flush()
    return redirect("Ortak:login")


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
            return redirect("common: kullanici_list")
        else:
            return render(request,'olustur.html',{'kullanici_form':kullanici_form, "errors":kullanici_form.errors})

    else:
        return render(request,'olustur.html', {'kullanici_form':kullanici_form})







