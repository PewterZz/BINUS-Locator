from django.urls import path
from . import views
from django.conf.urls.static import static
from django.views.generic import TemplateView
urlpatterns = [
    path("",views.index, name="index"),
    path('restaurant/', TemplateView.as_view(template_name="restaurant.html"), name='restaurant'),
    path('floyd/', views.floyd, name="floyd"),
    path('showrec/', views.showrec, name="showrec"),
    path('recreational/', views.recreational, name="recreation"),
    path('showuniversity/', views.showuniversity, name="showuniversity"),
    path('university/', views.university, name="university"),
    path('showmall/', views.showmall, name="showmall"),
    path("mall", views.mall, name="mall")
]