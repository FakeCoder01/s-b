# Generated by Django 4.1.2 on 2023-05-13 18:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e21c569b-4aad-4999-9030-38fc16b5ca0c'), editable=False, primary_key=True, serialize=False),
        ),
    ]
