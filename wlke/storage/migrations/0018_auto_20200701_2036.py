# Generated by Django 3.0.7 on 2020-07-01 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0017_remove_datei_benutzername'),
    ]

    operations = [
        migrations.AddField(
            model_name='datei',
            name='ordner',
            field=models.CharField(default='adjkncvir1495kgsiqiy', max_length=200),
        ),
        migrations.AlterField(
            model_name='datei',
            name='datei',
            field=models.FileField(blank=True, null=True, upload_to='data/{{ornder}}/'),
        ),
    ]
