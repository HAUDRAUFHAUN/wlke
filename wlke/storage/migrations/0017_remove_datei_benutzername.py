# Generated by Django 3.0.7 on 2020-07-01 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0016_auto_20200626_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datei',
            name='benutzername',
        ),
    ]
