# Generated by Django 2.1.7 on 2019-08-18 11:25

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_oauth', '0003_auto_20190503_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
