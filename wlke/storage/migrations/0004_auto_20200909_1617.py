# Generated by Django 3.0.7 on 2020-09-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_datei'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datei',
            name='datei',
            field=models.FileField(blank=True, null=True, upload_to='data/7VES592PMSESU802OZGA/'),
        ),
    ]