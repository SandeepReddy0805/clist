# Generated by Django 2.1.7 on 2019-08-18 12:13

import django.contrib.postgres.fields
from django.db import migrations, models
import true_coders.models


def init_from_jsonfield(apps, schema_editor):
    Filter = apps.get_model('true_coders', 'filter')

    for f in Filter.objects.all():
        f.arr_categories = f.categories
        f.save()


class Migration(migrations.Migration):

    dependencies = [
        ('true_coders', '0018_auto_20190818_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='arr_categories',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, default=true_coders.models._get_default_categories, size=None),  # noqa
        ),
        migrations.RunPython(init_from_jsonfield),
    ]
