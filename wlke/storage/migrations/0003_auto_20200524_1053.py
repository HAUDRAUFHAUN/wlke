# Generated by Django 3.0.6 on 2020-05-24 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storage', '0002_auto_20200523_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datei',
            name='benutzer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='datei', to=settings.AUTH_USER_MODEL),
        ),
    ]
