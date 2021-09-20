from itertools import chain

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from django.db.models.functions import Concat
from django.db.models import Prefetch, Min, Value

from .models import Offering, Retailer, Scrape, Laptop
from .serializers import LaptopSerializer

def flatten(listable):
    return list(chain(*listable))

def get_distinct_property(items, property):
    return flatten(items.values_list(property).order_by(property).distinct())

class GetOfferings(APIView):
    def get(self, request, format=None):
        laptops = Laptop.objects.prefetch_related(Prefetch('offerings', queryset=Offering.objects.filter(active=True).filter(ignored=False).order_by('price'))).filter(offerings__active=True)
        items = laptops.annotate(min_price=Min('offerings__price')).order_by('min_price')
        vendors = get_distinct_property(laptops, 'vendor__name')
        gpu_vendors = get_distinct_property(laptops, 'gpu_vendor__name')
        retailers = get_distinct_property(laptops, 'offerings__retailer__name')
        cpu_families = flatten(laptops.values_list(Concat('cpu_family__cpu_vendor__name', Value(' - '), 'cpu_family__name')).order_by('cpu_family__cpu_vendor__name', 'cpu_family__name').distinct())
        ram = get_distinct_property(laptops, 'ram')
        hdd = get_distinct_property(laptops, 'hdd')
        sizes = get_distinct_property(laptops, 'size')
        resolutions = get_distinct_property(laptops, 'resolution')
        return Response({
            'vendor': vendors,
            'retailer': retailers,
            'cpu_family': cpu_families,
            'ram': ram,
            'hdd': hdd,
            'gpu_vendor': gpu_vendors,
            'size': sizes,
            'resolution': resolutions,
            'items': LaptopSerializer(items, many=True).data,
        })


class Update(APIView):
    permission_classes = [HasAPIKey,]

    def post(self, request, format=None):
        items = request.data
        total_offerings_count = len(items)
        Offering.objects.update(active=False)
        new_offerings_count = 0
        for item in items:
            url = item.get('url')
            price = item.get('price')
            offering = Offering.objects.filter(url=url).first()
            if (offering is not None):
                offering.price = price
                offering.active = True
                offering.save()
                continue
            name = item.get('name')
            sku = item.get('sku')
            laptop = Laptop.objects.filter(sku=sku).first()
            retailer_string = item.get('retailer')
            retailer = Retailer.objects.get(code=retailer_string)
            offering = Offering(
                sku=sku,
                name=name,
                url=url,
                price=price,
                retailer=retailer,
                laptop=laptop,
            )

            offering.save()
            new_offerings_count += 1

        scrape_instance = Scrape(
            new_offerings=new_offerings_count,
            total_offerings=total_offerings_count
        )
        scrape_instance.save()
        return Response()
