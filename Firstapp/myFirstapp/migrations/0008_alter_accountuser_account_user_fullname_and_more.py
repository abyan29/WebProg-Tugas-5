# Generated by Django 5.0.6 on 2024-06-23 06:00

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstapp', '0007_alter_accountuser_account_user_fullname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_fullname',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_id',
            field=models.UUIDField(default=uuid.UUID('fe3ffd3c-26b9-445e-ba8b-592f1828e6e8'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
