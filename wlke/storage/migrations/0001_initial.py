# Generated by Django 3.0.6 on 2020-05-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datei', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
