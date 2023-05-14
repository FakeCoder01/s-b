# Generated by Django 4.1.2 on 2023-05-14 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_profile_id_delete_chathistory'),
        ('knowledgebase', '0007_remove_answer_helpful_alter_answer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chathistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chathistory_ayon_profile', to='api.profile'),
        ),
    ]
