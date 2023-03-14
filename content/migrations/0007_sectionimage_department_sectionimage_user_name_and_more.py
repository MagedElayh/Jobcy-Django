# Generated by Django 4.1.1 on 2023-01-19 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_rename_sectionfive_sectionfiveourteams_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionimage',
            name='department',
            field=models.CharField(default=0, max_length=50, verbose_name='department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sectionimage',
            name='user_name',
            field=models.CharField(default=0, max_length=50, verbose_name='name of team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sectionimage',
            name='image',
            field=models.ImageField(upload_to='image', verbose_name='image of team'),
        ),
        migrations.AlterField(
            model_name='sectionimage',
            name='text_description',
            field=models.TextField(max_length=2000),
        ),
    ]