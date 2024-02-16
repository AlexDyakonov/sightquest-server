# Generated by Django 4.0.1 on 2024-02-10 17:50

import apps.api.models
import backend.yandex_s3_storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_rename_gameuser_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questpoint',
            name='image',
            field=models.ImageField(null=True, storage=backend.yandex_s3_storage.ClientDocsStorage(), upload_to=apps.api.models.quest_point_file_path),
        ),
    ]
