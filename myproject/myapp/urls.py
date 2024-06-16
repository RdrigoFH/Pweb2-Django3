from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('crear_persona/', views.crear_persona, name='crear_persona'),
    path('catalog/', index, name='index'),  
]
