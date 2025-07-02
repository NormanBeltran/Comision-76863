from django.urls import include, path
from myapp import views

urlpatterns = [
    path(""       ,   views.index,      name="index"),
    path("acerca/",   views.acerca,     name="acerca"),
    path("contacto/", views.contacto,   name="contacto"),

    path("cursos/",   views.cursos,     name="cursos"),
    path("aero/",     views.aero,       name="aero"),
    path("aero_api/", views.aero_api,   name="aero_api"),

    path("bienvenido/",  views.bienvenido,  name="bienvenido"),
    path("welcome/",     views.welcome,     name="welcome"),
    path("bienvenido2/", views.bienvenido2, name="bienvenido2"),
    path("uncurso/<id>/", views.unCurso,    name="uncurso"),
    path("cursos_all/",   views.cursos_all, name="cursos_all"),

    path("nuevo_curso/",   views.nuevoCurso, name="nuevo_curso"),
]
