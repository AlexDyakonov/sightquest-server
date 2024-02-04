# Generated by Django 4.0.1 on 2024-02-04 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_gamephoto_image_alter_questpoint_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='started_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='gamesettings',
            name='mode',
            field=models.CharField(choices=[('BASE', 'Base')], max_length=50),
        ),
    ]
