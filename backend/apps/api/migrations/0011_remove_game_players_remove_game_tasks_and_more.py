# Generated by Django 4.0.1 on 2024-02-03 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_playertaskcompletion_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='players',
        ),
        migrations.RemoveField(
            model_name='game',
            name='tasks',
        ),
        migrations.RemoveField(
            model_name='gamequesttask',
            name='game',
        ),
        migrations.AddField(
            model_name='gamequesttask',
            name='settings',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.gamesettings'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gamesettings',
            name='tasks',
            field=models.ManyToManyField(through='api.GameQuestTask', to='api.QuestTask'),
        ),
        migrations.AlterField(
            model_name='gameuser',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='api.game'),
        ),
    ]
