# Generated by Django 4.2.5 on 2023-12-21 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_remove_notifications_text_notifications_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
