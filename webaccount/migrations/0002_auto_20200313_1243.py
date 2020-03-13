# Generated by Django 2.2.10 on 2020-03-13 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webaccount', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='webaccount',
            options={'managed': True, 'verbose_name_plural': '玩家'},
        ),
        migrations.AddField(
            model_name='webaccount',
            name='lastserver',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='webaccount',
            name='lock',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='webaccount',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='webaccount',
            name='playerid',
            field=models.IntegerField(default=0),
        ),
    ]
