# Generated by Django 4.1.1 on 2023-01-27 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/image/aboutus', verbose_name='image background')),
                ('header', models.CharField(max_length=200, verbose_name='header')),
                ('paragraph', models.TextField(verbose_name='paragraph')),
            ],
        ),
    ]
