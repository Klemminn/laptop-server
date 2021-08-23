# Generated by Django 3.1.2 on 2021-08-23 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offerings', '0010_auto_20210823_0003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='laptop',
            options={'ordering': ('sku',)},
        ),
        migrations.AlterModelOptions(
            name='offering',
            options={'ordering': ('-laptop',)},
        ),
        migrations.AlterField(
            model_name='offering',
            name='laptop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offerings', to='offerings.laptop'),
        ),
    ]