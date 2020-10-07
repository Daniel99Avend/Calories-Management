from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('register/',views.register_page,name='registro'),
    path('login/',views.login_page, name ="login")
]