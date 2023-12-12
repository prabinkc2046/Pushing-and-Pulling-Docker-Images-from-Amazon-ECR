
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('website.urls')),
    path('admin/', admin.site.urls),
]
