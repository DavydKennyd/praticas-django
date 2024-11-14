from django.urls import path
from . import views

urlpatterns = [
    path('dkpag/', views.membros, name='membros')
]