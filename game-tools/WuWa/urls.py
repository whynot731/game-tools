from django.urls import path#, include
from WuWa import views as views

urlpatterns = [

    path('', views.home, name='home'),
    path('materials', views.material_calc, name='materials'),
]
