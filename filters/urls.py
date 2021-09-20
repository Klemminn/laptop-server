from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GetFilter, CreateFilter

urlpatterns = format_suffix_patterns([
     path(
        r'<str:code>',
        GetFilter.as_view(),
        name='get-filter'
    ),
    path(
        'create/',
        CreateFilter.as_view(),
        name='create-filter'
    ),
])
