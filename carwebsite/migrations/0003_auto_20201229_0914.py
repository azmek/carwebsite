# Generated by Django 3.1.4 on 2020-12-29 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carwebsite', '0002_auto_20201228_1429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='phot',
            new_name='photo',
        ),
    ]
