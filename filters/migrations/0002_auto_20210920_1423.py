# Generated by Django 3.1.2 on 2021-09-20 14:23

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='filter',
            index=django.contrib.postgres.indexes.GinIndex(fields=['filter'], name='data_gin'),
        ),
    ]