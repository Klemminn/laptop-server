# Generated by Django 3.1.2 on 2021-08-22 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerings', '0008_auto_20210822_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offering',
            name='sku',
            field=models.CharField(max_length=30),
        ),
    ]
