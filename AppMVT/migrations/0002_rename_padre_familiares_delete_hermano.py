# Generated by Django 4.1 on 2022-09-03 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppMVT', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Padre',
            new_name='Familiares',
        ),
        migrations.DeleteModel(
            name='Hermano',
        ),
    ]
