# Generated by Django 5.0.7 on 2024-08-05 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(blank=True, db_index=True, null=True, upload_to='Blog_image'),
        ),
    ]
