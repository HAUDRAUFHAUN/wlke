# Generated by Django 3.0.7 on 2020-07-01 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0019_auto_20200701_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datei',
            name='ordner',
        ),
        migrations.AlterField(
            model_name='datei',
            name='datei',
            field=models.FileField(blank=True, null=True, upload_to='data/<django.db.models.query_utils.DeferredAttribute object at 0x0000015B257EDFA0>/'),
        ),
    ]