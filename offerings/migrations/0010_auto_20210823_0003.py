# Generated by Django 3.1.2 on 2021-08-23 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerings', '0009_auto_20210822_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='sku',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]