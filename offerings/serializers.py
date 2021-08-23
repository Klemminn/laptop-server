from rest_framework import serializers

from .models import Offering, Laptop

class OfferingSerializer(serializers.ModelSerializer):
    retailer_name = serializers.ReadOnlyField(source='retailer.name')
    retailer_code = serializers.ReadOnlyField(source='retailer.code')
    class Meta:
        model = Offering
        fields = ('id', 'retailer_name', 'retailer_code', 'price', 'url', 'active',)

class LaptopSerializer(serializers.ModelSerializer):
    vendor = serializers.ReadOnlyField(source='vendor.name')
    cpu_family = serializers.ReadOnlyField(source='cpu_family.name')
    offerings = OfferingSerializer(many=True, read_only=True)
    min_price = serializers.IntegerField()
    class Meta:
        model = Laptop
        fields = ('id', 'sku', 'name', 'vendor', 'cpu_model', 'ram', 'hdd', 'size', 'resolution', 'gpu_model', 'weight', 'created', 'offerings', 'cpu_family', 'min_price',)