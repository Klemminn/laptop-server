# Generated by Django 3.1.2 on 2021-08-22 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offerings', '0007_auto_20210818_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offering',
            name='laptop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offerings', to='offerings.laptop'),
        ),
    ]