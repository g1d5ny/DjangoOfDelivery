from django.urls import path
from .views import add_point

app_name = 'point'

urlpatterns = [
    path('add/', add_point, name='add'),
]