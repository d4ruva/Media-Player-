from django.contrib import admin
from django.urls import path

from api import views as api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.index)
]
