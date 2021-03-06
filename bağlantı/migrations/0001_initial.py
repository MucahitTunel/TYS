# Generated by Django 2.0.7 on 2018-07-19 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('Ortak', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baglanti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ad', models.CharField(max_length=20)),
                ('Soyad', models.CharField(max_length=20)),
                ('eMail', models.EmailField(max_length=254)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('is_active', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hesap_olusturan_kisi', to='Ortak.Kullanici')),
                ('hesap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Hesap', to='account.Hesap')),
                ('tanımlı', models.ManyToManyField(to='Ortak.Kullanici')),
            ],
        ),
    ]
