from django.urls import path
from .views import show_data

urlpatterns = [
    path('show_data/', show_data, name='show_data'),
]
