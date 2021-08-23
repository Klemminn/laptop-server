# Generated by Django 3.1.2 on 2021-08-17 23:41

from django.db import migrations, models
import laptop.utils
import laptop.validators


class Migration(migrations.Migration):

    dependencies = [
        ('offerings', '0004_laptop_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='image',
            field=models.ImageField(null=True, upload_to=laptop.utils.handle_upload, validators=[laptop.validators.validate_image_extension]),
        ),
    ]