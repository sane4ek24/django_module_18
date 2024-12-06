from django.contrib import admin
from django.urls import path
from task4.views import platform, cart, cases


urlpatterns = [
    path('admin/', admin.site.urls),
    path('platform/', platform),
    path('platform/cart/', cart),
    path('platform/cases/', cases)
]