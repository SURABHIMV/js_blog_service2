# Generated by Django 5.0.7 on 2024-08-12 06:02

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_delete_basemodal_alter_blog_managers_blog_is_deleted'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='service',
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
