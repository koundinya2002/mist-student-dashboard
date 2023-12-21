# Generated by Django 4.2.5 on 2023-12-08 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
                ('file', models.FileField(null=True, upload_to='')),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
