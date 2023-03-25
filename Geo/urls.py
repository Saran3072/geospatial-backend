from django.contrib import admin
from django.urls import path, include
from IIIT import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('', views.home, name='index'),
    path('https://heatwave-and-aqi-predictor-backend/.onrender.com', TemplateView.as_view(template_name = 'index.html')),
    path('trail', views.analysis),
]
