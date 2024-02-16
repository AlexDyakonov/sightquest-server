# Generated by Django 4.0.1 on 2024-02-03 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_game_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameuser',
            name='role',
            field=models.CharField(choices=[('RUNNER', 'Runner'), ('CATCHER', 'Catcher')], default='CATCHER', max_length=10),
        ),
    ]
