# Generated by Django 3.0.6 on 2020-06-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0014_auto_20200624_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datei',
            name='datei',
            field=models.FileField(blank=True, null=True, upload_to='data/<bound method Field.get_default of <django.db.models.fields.CharField>>/'),
        ),
    ]