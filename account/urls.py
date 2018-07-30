from django.conf.urls import url
from .views import hesap_ekle

app_name = 'account'

urlpatterns = [
    url(r'^hesap_ekle/$',hesap_ekle, name="Hesap_Ekle"),


]