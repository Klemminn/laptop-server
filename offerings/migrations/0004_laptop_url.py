# Generated by Django 3.1.2 on 2021-08-17 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerings', '0003_auto_20210817_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='url',
            field=models.URLField(default=''),
        ),
    ]