# Generated by Django 4.2.5 on 2023-10-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
