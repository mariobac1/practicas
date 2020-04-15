from django.urls import path, include
from claro import views
urlpatterns = [
    path('',views.index),
]
