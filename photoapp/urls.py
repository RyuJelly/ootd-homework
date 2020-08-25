from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo, name="photo"),
    path('<int:id>/', views.photo, name="photo"),
    path('<int:id>/<int:like>/', views.photo, name="photo"),
]