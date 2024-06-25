# Generated by Django 5.0.6 on 2024-06-20 03:37

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accountuser',
            options={'ordering': ('account_user_related_user',)},
        ),
        migrations.RenameIndex(
            model_name='accountuser',
            new_name='myFirstapp__account_ebbf04_idx',
            old_name='myFirstapp__account_a78183_idx',
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_id',
            field=models.UUIDField(default=uuid.UUID('36d6f4a1-b85d-4151-9a54-1b63aa3a376a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_related_user',
            field=models.CharField(editable=False, max_length=255),
        ),
    ]
