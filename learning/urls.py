from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('records', views.record, name='records'),
    path('settings', views.setting, name='settings'),
]