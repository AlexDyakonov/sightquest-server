# Generated by Django 4.0.1 on 2024-02-05 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='telegram',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
