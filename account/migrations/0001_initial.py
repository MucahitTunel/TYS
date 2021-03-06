# Generated by Django 2.0.7 on 2018-07-19 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ortak', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hesap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ad', models.CharField(max_length=20)),
                ('eMail', models.EmailField(max_length=254)),
                ('aciklama', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('is_active', models.BooleanField(default=False)),
                ('assigned_to', models.ManyToManyField(to='Ortak.Kullanici')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hesabı_olusturan_kisi', to='Ortak.Kullanici')),
                ('takim', models.ManyToManyField(to='Ortak.Takim')),
            ],
        ),
    ]
