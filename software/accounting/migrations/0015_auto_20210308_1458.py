# Generated by Django 3.1.7 on 2021-03-08 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0014_auto_20210304_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='jventryM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subhed', models.CharField(blank=True, max_length=250, null=True)),
                ('ledger', models.CharField(blank=True, max_length=250, null=True)),
                ('entry_type', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='journalm',
            name='Entry_type',
        ),
        migrations.RemoveField(
            model_name='journalm',
            name='amount',
        ),
    ]
