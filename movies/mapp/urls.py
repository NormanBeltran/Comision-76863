from django.urls import path, include

from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),  
    path("generos/", GenderList.as_view(), name="generos"),  
    path("companias/", CompanyList.as_view(), name="companias"),

    path("peliculas/", MovieList.as_view(), name="peliculas"),  
    path("peliculas_create/", MovieCreate.as_view(), name="peliculas_create"),  
]
