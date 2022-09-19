# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-16 04:16


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0028_auto_20180216_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='login',
            unique_together=set([('team', 'stage')]),
        ),
    ]