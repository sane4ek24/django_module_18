from django.contrib import admin
from django.urls import path
from task2.views import func_templ, class_templ

urlpatterns = [
    path('/admin/', admin.site.urls),
    path('func_templ/', func_templ),
    path('class_templ/', class_templ.as_view()),
    ]