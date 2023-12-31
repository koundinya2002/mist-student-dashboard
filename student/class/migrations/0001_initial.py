# Generated by Django 4.2.7 on 2023-11-27 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0002_classroom_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('points', models.IntegerField()),
                ('assigned', models.DateTimeField(auto_now=True)),
                ('due', models.DateTimeField(null=True)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.classroom')),
            ],
        ),
    ]
