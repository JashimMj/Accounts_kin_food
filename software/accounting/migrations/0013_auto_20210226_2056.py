# Generated by Django 3.1.7 on 2021-02-26 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0012_auto_20210226_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditm',
            name='jv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.dabitm'),
        ),
        migrations.AlterField(
            model_name='dabitm',
            name='jv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.ledjerm'),
        ),
    ]
