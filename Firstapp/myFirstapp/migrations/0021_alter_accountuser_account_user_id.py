# Generated by Django 5.0.6 on 2024-06-25 14:21

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstapp', '0020_alter_accountuser_account_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_id',
            field=models.UUIDField(default=uuid.UUID('786715e1-62e0-45cd-98ba-377ee34cdde0'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
