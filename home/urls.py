from django.urls import path
# from .views import hola, fecha
from home import views
# from . import views

urlpatterns = [
    path('', views.index),
    path('ver-personas/', views.ver_personas),
    path('crear-persona/<str:nombre>/<str:apellido>/', views.crear_persona),
    # path('hola/', hola),
    # path('fecha/', fecha),
]
