# Generated by Django 2.2.10 on 2020-03-13 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chargeorder',
            options={'managed': True, 'verbose_name_plural': '充值'},
        ),
    ]