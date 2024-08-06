from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('pets/',views.pets,name='pets'),
    path('pets/<int:pet_id>/',views.pet_detail,name='pet_detail') 
]