# Generated by Django 3.1.7 on 2021-02-25 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_auto_20210225_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journalm',
            name='credit',
        ),
        migrations.RemoveField(
            model_name='journalm',
            name='dabit',
        ),
        migrations.RemoveField(
            model_name='journalm',
            name='ledjer',
        ),
        migrations.RemoveField(
            model_name='journalm',
            name='subhed',
        ),
        migrations.CreateModel(
            name='subheadM',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subhed', models.CharField(blank=True, max_length=255, null=True)),
                ('jv', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.journalm')),
            ],
        ),
        migrations.CreateModel(
            name='ledjerM',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ledjer', models.CharField(blank=True, max_length=255, null=True)),
                ('jv', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.journalm')),
            ],
        ),
        migrations.CreateModel(
            name='dabitM',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dabit', models.CharField(blank=True, max_length=255, null=True)),
                ('jv', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.journalm')),
            ],
        ),
        migrations.CreateModel(
            name='creditM',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('credit', models.CharField(blank=True, max_length=255, null=True)),
                ('jv', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.journalm')),
            ],
        ),
    ]