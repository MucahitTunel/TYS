from django.db import models
from Ortak.models import *
from account.models import *

# Create your models here.


class Baglanti(models.Model):
    Ad = models.CharField(max_length=20)
    Soyad = models.CharField(max_length=20)
    hesap = models.ForeignKey(Hesap)
    eMail = models.EmailField()
    tanımlı = models.ManyToManyField(Kullanici)
    created_by = models.ForeignKey(Kullanici)
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    aktif_mi = models.BooleanField(default=False)

    def __str__(self):
        return self.Ad