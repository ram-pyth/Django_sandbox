from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.OrderCreateView.as_view(), name='create-order'),
]