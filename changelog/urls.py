from django.urls import path

from . import views

app_name = 'changelog'

urlpatterns = [
    path('ragcp/', views.CASHView, name='cashpoints'),
    path('rathena/', views.RMTView, name='rmtpoints'),
]
