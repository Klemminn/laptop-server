from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Filter

class GetFilter(APIView):
    def get(self, request, format=None, **kwargs):
        code = kwargs.get('code')
        filter = Filter.objects.get(code=code)
        return Response(filter.filter)

class CreateFilter(APIView):
    def post(self, request, format=None):
        filter = request.data
        (build, created,) = Filter.objects.get_or_create(filter=filter)

        return Response(build.code)
