# Generated by Django 3.1.2 on 2021-08-18 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offerings', '0006_laptop_vendor_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='vendor_name',
        ),
        migrations.AlterField(
            model_name='laptop',
            name='gpu_vendor',
            field=models.ForeignKey(default='amd', on_delete=django.db.models.deletion.CASCADE, related_name='laptops', to='offerings.gpuvendor', to_field='code'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='laptop',
            name='vendor',
            field=models.ForeignKey(default='lenovo', on_delete=django.db.models.deletion.CASCADE, related_name='laptops', to='offerings.vendor', to_field='code'),
            preserve_default=False,
        ),
    ]