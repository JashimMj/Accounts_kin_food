# Generated by Django 3.1.7 on 2021-03-08 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0015_auto_20210308_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jventrym',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]