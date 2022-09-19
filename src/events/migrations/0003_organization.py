# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-03 11:21


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20180203_0046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('name_ru', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]