# Generated by Django 2.1.7 on 2019-08-18 11:25

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0008_auto_20190329_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='addition',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
    ]
