from django.contrib import admin
from django.urls import path
from task3.views import platform, cart, cases


urlpatterns = [
    path('admin/', admin.site.urls),
    path('platforma/', platform),
    path('platforma/cart/', cart),
    path('platforma/cases/', cases)
]