# Generated by Django 3.1.7 on 2021-02-25 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0007_auto_20210225_1351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ledjerm',
            old_name='jv',
            new_name='jvl',
        ),
    ]