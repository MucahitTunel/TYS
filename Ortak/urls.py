from django.conf.urls import url
from Ortak import views

app_name = 'Ortak'

urlpatterns = [
    url(r'^$', views.home, name="Ana_sayfa"),
    url(r'^profil/$', views.profile, name="Profil"),
    url(r'^giris/$', views.giris_crm, name="Giriş"),
    url(r'^sifremi-unuttum/$', views.sifremi_unuttum, name="Sifremiunuttum"),
    url(r'^cikis/$', views.cıkıs_crm, name="Cıkıs"),

]