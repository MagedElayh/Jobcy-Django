# Generated by Django 4.1.1 on 2023-01-18 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_porfolioitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='paragraph',
            field=models.TextField(max_length=2000),
        ),
    ]
