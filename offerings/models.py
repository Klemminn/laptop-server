from django.db import models

from laptop.validators import validate_image_extension
from laptop.utils import handle_upload

def ImageField():
    return models.ImageField(
        null=True,
        blank=True,
        upload_to=handle_upload,
        validators=[validate_image_extension],
    )

class Retailer(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('code',)

class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class CpuVendor(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class GpuVendor(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class CpuFamily(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10)
    cpu_vendor = models.ForeignKey(CpuVendor, related_name='cpu_families', to_field='code', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Laptop(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=30, unique=True)
    vendor = models.ForeignKey(Vendor, related_name='laptops', to_field='code', on_delete=models.CASCADE)
    cpu_family = models.ForeignKey(CpuFamily, related_name='laptops', to_field='code', on_delete=models.CASCADE)
    cpu_model = models.CharField(max_length=30)
    ram = models.IntegerField()
    hdd = models.IntegerField()
    size = models.FloatField()
    resolution = models.CharField(max_length=12)
    gpu_vendor = models.ForeignKey(GpuVendor, related_name='laptops', to_field='code', on_delete=models.CASCADE)
    gpu_model = models.CharField(max_length=30)
    weight = models.FloatField(null=True, blank=True)

    image = ImageField()

    def __str__(self):
        return '%s - %s' % (self.sku, self.name,)
    
    class Meta:
        ordering = ('sku',)

class Offering(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=300)
    sku = models.CharField(max_length=30)
    laptop = models.ForeignKey(Laptop, related_name='offerings', to_field='id', on_delete=models.CASCADE, null=True, blank=True)
    retailer = models.ForeignKey(Retailer, related_name='offerings', to_field='code', on_delete=models.CASCADE)
    price = models.IntegerField()
    url = models.URLField(unique=True)
    active = models.BooleanField(default=True)
    ignored = models.BooleanField(default=False)

    class Meta:
        ordering = ('-laptop',)
        indexes = [
            models.Index(fields=['price',]),
            models.Index(fields=['active',]),
        ]


class Scrape(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    total_offerings = models.PositiveIntegerField()
    new_offerings = models.PositiveIntegerField()
