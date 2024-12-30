from django.urls import path
from . import views

urlpatterns = [
    path('practice_one/', views.practice_one, name='show_data'),
    path('practice_two/', views.practice_two,),
]
