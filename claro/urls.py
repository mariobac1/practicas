from django.contrib import admin
from django.urls import path, include, re_path
from claro import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('busqueda/',views.busqueda_articulos),
    #path('buscar/',views.buscar),
    #path('busqueda/', views.busqueda_ingenierias),
    path('search/',views.search),
    path('mail/', include('ingenierias.urls')),
    path('', views.welcome),
    path('login/', views.login),
    path('logout/', views.logut),
    path('sendmail/', views.index)
]

