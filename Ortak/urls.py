from django.conf.urls import url
from Ortak import views

app_name = 'Ortak'

urlpatterns = [
    url(r'^$', views.home, name="Ana_sayfa"),
    url(r'^profil/$', views.profile, name="Profil"),
    url(r'^giris/$', views.giris_crm, name="Giriş"),
    url(r'^sifremi-unuttum/$', views.sifremi_unuttum, name="Sifremiunuttum"),
    url(r'^cikis/$', views.cıkıs_crm, name="Cıkıs"),
    url(r'^kullanici_olustur/$', views.kullanici_olustur, name="olustur"),
    url(r'^kullanici_listele/$', views.kullanici_listele, name="kullanici_list"),
    url(r'^index/$', views.home, name='ev'),
    url(r'^/(?P<user_id>\d*)/kullanici_goruntule', views.kullanici_goruntule, name="Kullanıcı_görüntüle"),

]