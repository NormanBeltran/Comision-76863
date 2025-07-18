from django.urls import path, include

from django.contrib.auth.views import LogoutView

from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),  
    path("generos/", GenderList.as_view(), name="generos"),  
    path("companias/", CompanyList.as_view(), name="companias"),

    path("peliculas/", MovieList.as_view(), name="peliculas"),  
    path("peliculas_create/", MovieCreate.as_view(), name="peliculas_create"),  
    path("peliculas_update/<int:pk>/", MovieUpdate.as_view(), name="peliculas_update"),  
    path("peliculas_delete/<int:pk>/", MovieDelete.as_view(), name="peliculas_delete"), 

    path("login/", MyLoginView.as_view(), name="login"),  
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),  
]
