from django.db import models
from Ortak.models import Kullanici
from account.models import Hesap

# Create your models here.


class Baglanti(models.Model):
    Ad = models.CharField(max_length=20)
    Soyad = models.CharField(max_length=20)
    hesap = models.ForeignKey(Hesap, related_name='Hesap', on_delete=models.CASCADE)
    eMail = models.EmailField()
    assigned_to = models.ManyToManyField(Kullanici)
    created_by = models.ForeignKey(Kullanici, related_name='hesap_olusturan_kisi', on_delete=models.CASCADE)
    created_on = models.DateTimeField(("Created on"), auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.Ad