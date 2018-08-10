from django.conf.urls import url
from .views import baglanti_ekle

app_name = 'bağlantı'

urlpatterns = [
    url(r'^baglanti_ekle/$',baglanti_ekle, name="Baglanti_ekle"),
]