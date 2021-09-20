from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/offerings/', include('offerings.urls')),
    path('v1/filters/', include('filters.urls')),
]
