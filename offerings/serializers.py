from rest_framework import serializers

from .models import Offering, Laptop

class OfferingSerializer(serializers.ModelSerializer):
    retailer_name = serializers.ReadOnlyField(source='retailer.name')
    retailer_code = serializers.ReadOnlyField(source='retailer.code')
    class Meta:
        model = Offering
        fields = ('id', 'retailer_name', 'retailer_code', 'price', 'url',)

class LaptopSerializer(serializers.ModelSerializer):
    vendor = serializers.ReadOnlyField(source='vendor.name')
    cpu_family = serializers.ReadOnlyField(source='cpu_family.name')
    cpu_vendor = serializers.ReadOnlyField(source='cpu_family.cpu_vendor.name')
    gpu_vendor = serializers.ReadOnlyField(source='gpu_vendor.name')
    offerings = OfferingSerializer(many=True, read_only=True)
    min_price = serializers.IntegerField()
    class Meta:
        model = Laptop
        fields = ('id', 'sku', 'name', 'vendor', 'cpu_vendor', 'cpu_model', 'image', 'ram', 'hdd', 'size', 'resolution', 'gpu_model', 'gpu_vendor', 'weight', 'offerings', 'cpu_family', 'min_price',)