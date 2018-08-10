from django.conf.urls import url
from .views import hesap_olustur, hesap_listele

app_name = 'account'

urlpatterns = [
    url(r'^hesap_olustur/$',hesap_olustur, name="Hesap_Ekle"),
    url(r'^hesap_listele/$',hesap_listele, name="liste"),
]