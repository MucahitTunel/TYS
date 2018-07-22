from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from .utils import Roller
from django.urls import reverse
# Create your models here.



class Kullanici(AbstractBaseUser):#Kullanıcı
    TC = models.BigIntegerField(unique=True)
    Kullanıcı_adı = models.CharField(max_length=20, unique=True, verbose_name='KULLANICI ADI')
    Ad = models.CharField(max_length=30, verbose_name='AD')
    Soyad = models.CharField(max_length=30,verbose_name='SOYAD')
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    e_Mail = models.EmailField(max_length=255, unique=True, verbose_name='E-POSTA ADRESİ')
    Rol = models.CharField(max_length=50, choices=Roller, verbose_name='ROL')
    Sifre = models.CharField(max_length=24, verbose_name='ŞİFRE')


    USERNAME_FIELD = 'e_Mail'
    REQUIRED_FIELDS = ['Kullanıcı_adı']

    nesne = UserManager()

    def get_short_name(self):
        return self.Kullanıcı_adı

    def __unicode__(self):
        return self.e_Mail



class Takim(models.Model):#Takım
    Ad = models.CharField(max_length=50)
    numara = models.ManyToManyField(Kullanici)

    def __str__(self):
        return self.Ad




