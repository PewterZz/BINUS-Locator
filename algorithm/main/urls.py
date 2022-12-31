from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.index, name="index"),
    path('map/', TemplateView.as_view(template_name="map.html"),
                   name='map'),
]
