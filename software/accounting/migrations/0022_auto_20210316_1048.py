# Generated by Django 3.1.7 on 2021-03-16 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0021_auto_20210310_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='jventrym',
            name='amount',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='jventrym',
            name='entry_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='jventrytypeamountM',
        ),
    ]
