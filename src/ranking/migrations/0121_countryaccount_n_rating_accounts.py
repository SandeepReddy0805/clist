# Generated by Django 4.2.11 on 2024-04-05 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0120_alter_countryaccount_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='countryaccount',
            name='n_rating_accounts',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]