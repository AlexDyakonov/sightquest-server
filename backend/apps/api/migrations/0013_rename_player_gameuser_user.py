# Generated by Django 4.0.1 on 2024-02-03 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_playertaskcompletion_player'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gameuser',
            old_name='player',
            new_name='user',
        ),
    ]
