from django.contrib import admin
from Ortak.models import *
# Register your models here.
class KullanıcıAdmin(admin.ModelAdmin):
    list_display = ['Kullanıcı_adı','e_Mail']
    search_fields = ['Kullanıcı_adı']


    class Meta:
        model = Kullanici




admin.site.register(Kullanici,KullanıcıAdmin)
admin.site.register(Takim)