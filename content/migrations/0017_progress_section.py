# Generated by Django 4.1.1 on 2023-01-25 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0016_alter_header_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.sectiontwo'),
        ),
    ]
