# Generated by Django 4.1.2 on 2023-05-13 18:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_department_id_alter_office_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('99274bac-8e69-4057-86e1-954ac2bd78f6'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
