# Generated by Django 5.0.6 on 2024-06-25 14:32

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstapp', '0021_alter_accountuser_account_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_id',
            field=models.UUIDField(default=uuid.UUID('dee54163-baae-48d0-a81d-9199c561eb71'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
