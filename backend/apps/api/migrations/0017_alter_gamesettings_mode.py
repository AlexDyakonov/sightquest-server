# Generated by Django 4.0.1 on 2024-02-04 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_game_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesettings',
            name='mode',
            field=models.CharField(choices=[('BASE', 'Base')], default='BASE', max_length=50),
        ),
    ]