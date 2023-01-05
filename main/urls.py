from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.index, name="index"),
    path("info/", views.index, name="index"),
    path("us/", views.index, name="index"),
    path("FloydWarshall/", views.index, name="index"),
    path("floyd/", views.floyd, name="floyd"),
    path('map/', TemplateView.as_view(template_name="map.html"), name='map'),
]
