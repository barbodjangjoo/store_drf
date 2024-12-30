from django.urls import path
from . import views

urlpatterns = [
    path('practice_one/', views.practice_one, name='show_data'),
    path('practice_two/', views.practice_two,),
    path('practice_three/', views.practice_three,),
    path('practice_four/', views.practice_four,),
    # path('practice_five/', views.practice_five,),
    # path('practice_six/', views.practice_six,),
    # path('practice_seven/', views.practice_seven,),
]
