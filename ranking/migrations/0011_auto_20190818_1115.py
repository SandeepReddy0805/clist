# Generated by Django 2.1.7 on 2019-08-18 11:15

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0010_auto_20190818_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='addition',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
    ]
