# Generated by Django 3.1.7 on 2021-03-10 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0020_auto_20210310_1425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jventrytypeamountm',
            old_name='jvd',
            new_name='jvid',
        ),
    ]