from django.urls import path
from . import views

urlpatterns = [
    path('show_data/', views.show_data, name='show_data'),
    path('practice_two/', views.practice_two),
    path('practice_three/', views.practice_three,)
]
