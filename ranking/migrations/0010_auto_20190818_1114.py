# Generated by Django 2.1.7 on 2019-08-18 11:14

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0009_auto_20190813_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='addition',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}),
        ),
    ]
