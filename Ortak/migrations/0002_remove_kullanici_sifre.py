# Generated by Django 2.0.7 on 2018-07-11 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ortak', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kullanici',
            name='Sifre',
        ),
    ]
