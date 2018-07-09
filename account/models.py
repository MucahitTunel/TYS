from django.db import models
from Ortak.models import Takim, Kullanici

# Create your models here.

class Hesap(models.Model):
    eMail = models.EmailField()
    aciklama = models.TextField()
    takim = models.ManyToManyField(Takim)
    created_by = models.ForeignKey(Kullanici, on_delete=models.CASCADE)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True)
    aktif_mi = models.BooleanField(default=False)

    def __str__(self):
        return self.eMail



