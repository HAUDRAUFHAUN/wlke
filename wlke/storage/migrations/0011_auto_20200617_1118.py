# Generated by Django 3.0.6 on 2020-06-17 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0010_auto_20200617_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datei',
            name='datei',
            field=models.FileField(upload_to='data/<django.db.models.query_utils.DeferredAttribute object at 0x040E6F10>/'),
        ),
    ]