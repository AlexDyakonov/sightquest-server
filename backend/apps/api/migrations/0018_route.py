# Generated by Django 4.0.1 on 2024-02-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_gamesettings_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(default='No description')),
                ('complexity', models.IntegerField(default=0)),
                ('popularity', models.IntegerField(default=0)),
                ('quest_points', models.ManyToManyField(to='api.QuestPoint')),
            ],
        ),
    ]
