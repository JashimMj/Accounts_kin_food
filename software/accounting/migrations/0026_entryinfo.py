# Generated by Django 3.1.7 on 2021-03-18 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0025_producerinformatio'),
    ]

    operations = [
        migrations.CreateModel(
            name='entryinfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Invoice_no', models.CharField(blank=True, max_length=255, null=True)),
                ('Invoice_date', models.DateField()),
                ('Delivery_Date', models.DateField()),
                ('Collection_date', models.DateField()),
                ('Client_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Producer_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Amount', models.IntegerField()),
                ('Received_Amount', models.IntegerField()),
            ],
        ),
    ]
