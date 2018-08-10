from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import BaglantiForm
from account.models import Hesap
from Ortak.models import Kullanici,Takim
from .models import Baglanti
from account.models import Hesap


# Create your views here.

# @login_required
# def add_contact(request):
#     accounts = Account.objects.all()
#     users = User.objects.filter(is_active=True).order_by('email')
#     form = ContactForm(assigned_to=users, account=accounts)
#     address_form = BillingAddressForm()
#     teams = Team.objects.all()
#     assignedto_list = request.POST.getlist('assigned_to')
#     teams_list = request.POST.getlist('teams')
#     if request.method == 'POST':
#         form = ContactForm(request.POST, assigned_to=users, account=accounts)
#         address_form = BillingAddressForm(request.POST)
#         if form.is_valid() and address_form.is_valid():
#             address_obj = address_form.save()
#             contact_obj = form.save(commit=False)
#             contact_obj.address = address_obj
#             contact_obj.created_by = request.user
#             contact_obj.save()
#             contact_obj.assigned_to.add(*assignedto_list)
#             contact_obj.teams.add(*teams_list)
#             if request.is_ajax():
#                 return JsonResponse({'error': False})
#             if request.POST.get("savenewform"):
#                 return HttpResponseRedirect(reverse("contacts:add_contact"))
#             else:
#                 return HttpResponseRedirect(reverse('contacts:list'))
#         else:
#             if request.is_ajax():
#                 return JsonResponse({'error': True, 'contact_errors': form.errors})
#             return render(request, 'create_contact.html', {
#                 'contact_form': form,
#                 'address_form': address_form,
#                 'accounts': accounts,
#                 'countries': COUNTRIES,
#                 'teams': teams,
#                 'users': users,
#                 'assignedto_list': [int(user_id) for user_id in assignedto_list],
#                 'teams_list': teams_list
#             })
#     else:
#         return render(request, 'create_contact.html', {
#             'contact_form': form,
#             'address_form': address_form,
#             'accounts': accounts,
#             'countries': COUNTRIES,
#             'teams': teams,
#             'users': users,
#             'assignedto_list': assignedto_list,
#             'teams_list': teams_list
#         })




# @login_required
# def contacts_list(request):
#     contact_obj_list = Contact.objects.all()
#     accounts = Account.objects.all()
#     page = request.POST.get('per_page')
#     first_name = request.POST.get('first_name')
#     account = request.POST.get('account')
#     city = request.POST.get('city')
#     phone = request.POST.get('phone')
#     email = request.POST.get('email')
#     if first_name:
#         contact_obj_list = contact_obj_list.filter(first_name__icontains=first_name)
#     if account:
#         contact_obj_list = contact_obj_list.filter(account=account)
#     if city:
#         a = Address.objects.filter(city__icontains=city)
#         contact_obj_list = contact_obj_list.filter(address__in=a)
#     if phone:
#         contact_obj_list = contact_obj_list.filter(phone__icontains=phone)
#     if email:
#         contact_obj_list = contact_obj_list.filter(email__icontains=email)
#     return render(request, 'contacts.html', {
#         'contact_obj_list': contact_obj_list,
#         'accounts': accounts,
#         'per_page': page
#     })








def baglanti_ekle(request):
    hesaplar = Hesap.objects.all()
    kullanici = Kullanici.objects.filter(is_active=True).order_by('eMail')
    takim = Takim.objects.all()
    form = BaglantiForm(assigned_to=kullanici, hesap=hesaplar)

    if request.method == 'POST':
        form = BaglantiForm(request.POST, assigned_to=kullanici, hesap=hesaplar)

        if form.is_valid():
            baglanti = form.save(commit=False)
            baglanti.created_by = request.user
            baglanti.save()
            if request.POST.get("savenewform"):
                return HttpResponseRedirect(reverse("contacts:add_contact"))

        else:
            return render(request,'Baglanti/baglanti_ekle.html',{'hesaplar':hesaplar, 'kullanici:':kullanici, 'takim':takim, 'form':form})

def baglanti_listele(request):
    baglanti_listesi = Baglanti.objects.all()
    hesaplar = Hesap.objects.all()

    Ad = request.POST.get('Ad')
    hesap = request.POST.get('hesap')
    eMail = request.POST.get('eMail')

    if Ad:
        baglanti_listesi = baglanti_listesi.filter(Ad__icontains=Ad)
    if hesap:
        baglanti_listesi = baglanti_listesi.filter(hesap__icontains=hesap)
    if eMail:
        baglanti_listesi = baglanti_listesi.filter(eMail__icontains=eMail)


    return render(request,'Baglanti/baglanti_listele.html', {'baglanti_listesi':baglanti_listesi,
                                                             'hesaplar':hesaplar})










