# Generated by Django 4.0.1 on 2024-02-03 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_gameuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playertaskcompletion',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_completions', to='api.gameuser'),
        ),
    ]
