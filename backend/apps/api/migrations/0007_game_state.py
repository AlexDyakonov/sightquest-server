# Generated by Django 4.0.1 on 2024-01-31 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_game_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='state',
            field=models.CharField(choices=[('LOBBY', 'Lobby'), ('PLAYING', 'Playing'), ('ENDED', 'Ended')], default='LOBBY', max_length=10),
        ),
    ]
