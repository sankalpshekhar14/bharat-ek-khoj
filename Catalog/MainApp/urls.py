from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
    # Uncomment the next line to enable the admin:
    url("^$",views.index)
]

