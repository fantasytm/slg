# Generated by Django 2.2.10 on 2020-03-13 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebAccount',
            fields=[
                ('uid', models.CharField(db_index=True, max_length=64, primary_key=True, serialize=False)),
                ('device', models.CharField(db_index=True, default='', max_length=64)),
                ('googleplay', models.CharField(db_index=True, default='', max_length=64)),
                ('facebook', models.CharField(db_index=True, default='', max_length=64)),
                ('lastdevice', models.CharField(default='', max_length=64)),
                ('feiyu', models.CharField(db_index=True, default='', max_length=64)),
                ('xindong', models.CharField(db_index=True, default='', max_length=64)),
                ('subplatform', models.CharField(default='', max_length=64)),
                ('loginid', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name_plural': '玩家',
                'db_table': 'webaccount',
                'managed': True,
            },
        ),
    ]
