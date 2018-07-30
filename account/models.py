from django.db import models
from Ortak.models import Takim, Kullanici

# Kullanıcı hesap bilgilerini göstermek için oluşturuldu
class Hesap(models.Model):
    Ad = models.CharField(max_length=20)
    eMail = models.EmailField()
    aciklama = models.TextField()
    takim = models.ManyToManyField(Takim)
    created_by = models.ForeignKey(Kullanici, related_name='hesabı_olusturan_kisi', on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(Kullanici)
    created_on = models.DateTimeField(("Created On"), auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.eMail