# Generated by Django 4.2.11 on 2024-03-31 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0114_stagecontest_stage_new_contests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stage',
            name='contests',
        ),
    ]