from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import sqlite3
from .forms import *
from .models import *

# Create your views here.

def index(request):
    return HttpResponse("Bienvenidos al sitio del curso de Django!")

def acerca(request):
    return HttpResponse("""
            <html>            
                    <h1>Acerca de mi ....</h1>
                    <h2>Prof. Norman Beltran</h2>
                    <h3>Curso de Django Python</h3>
            </html>
            """)    

def contacto(request):
    html = """
            <html>            
                    <h1>Contactenos a ....</h1>
                    <h2>Empresa yyyyyyyyyyyyy</h2>
                    <h3>Copyright 2025</h3>
            </html>
            """
    return HttpResponse(html)    

def cursos(request):
    conn = sqlite3.connect("curso.db")
    cursor = conn.cursor()

    html = """
            <html>            
                    <title>Lista de cursos</title>
                    
                    <table style='border:1px solid'>    
                    <thead>
                        <tr>
                            <th>Id</th>
                            <th>Nombre</th>
                            <th>Inscriptos</th>
                        </tr>
                    </thead>        
            """
    
    cursor.execute("SELECT id, nombre, inscriptos FROM cursos;")

    for (id, nombre, inscriptos) in cursor.fetchall():
        html += f"""
                <tr>
                    <td>{id}</td>
                    <td>{nombre}</td>
                    <td>{inscriptos}</td>
                </tr>
                """

    html += """
            </table>
            </html>            
    """
    conn.close
    return HttpResponse(html)   

def aero(request):
    html = """
            <html>            
                    <title>Lista de cursos</title>
                    
                    <table style='border:1px solid'>    
                    <thead>
                        <tr>
                            <th>id</th>
                            <th>Aeropuerto</th>
                            <th>Ciudad</th>
                            <th>Pais</th>
                            <th>Codigo</th>
                        </tr>
                    </thead>        
            """

    with open("aeropuertos.csv", encoding='utf8') as f:
        for linea in f:
            html += f"""
                <tr>
                    <td>{linea.split(',')[0].replace('"','')}</td>
                    <td>{linea.split(',')[1].replace('"','')}</td>
                    <td>{linea.split(',')[2].replace('"','')}</td>
                    <td>{linea.split(',')[3].replace('"','')}</td>
                    <td>{linea.split(',')[4].replace('"','')}</td>
                </tr>
                """

    html += """
            </table>
            </html>            
    """

    return HttpResponse(html)  

def aero_api(request):
    aeropuertos = []

    with open("aeropuertos.csv", encoding='utf8') as f:
        for linea in f:
            id     = linea.split(',')[0].replace('"','')
            nombre = linea.split(',')[1].replace('"','')
            ciudad = linea.split(',')[2].replace('"','')
            pais   = linea.split(',')[3].replace('"','')
            codigo = linea.split(',')[4].replace('"','')

            aeropuerto = {"id": id, "nombre": nombre, "ciudad": ciudad, "pais": pais, "codigo": codigo}
            aeropuertos.append(aeropuerto)
    
    return JsonResponse(aeropuertos, safe=False)   

def bienvenido(request):
    with open('myapp/templates/myapp/bienvenido.html') as f:
        html = f.read()
    return render(html)

def welcome(request):
    return render(request, 'myapp/bienvenido.html')

#___________________________________________
# 

def bienvenido2(request):
    ctx = {
        'nombre': 'Norman',
        'apellido': 'Beltran',
        'edad': 48,
        'cursos': [
            {'nombre': 'Python', 'inscriptos': 30},
            {'nombre': 'Django', 'inscriptos': 20},
            {'nombre': 'React', 'inscriptos': 10},
            {'nombre': 'HTML', 'inscriptos': 100},
            {'nombre': 'CSS', 'inscriptos': 110},
            {'nombre': 'JS', 'inscriptos': 120},
        ]
    }
    return render(request, 'myapp/bienvenido2.html', ctx)    

def unCurso(request, id):
    conn = sqlite3.connect("curso.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, nombre, inscriptos FROM cursos WHERE id = ?;", (id,))

    try:
        (id, nombre, inscriptos) = cursor.fetchone()
    except:
        return HttpResponse("Curso no encontrado en la BD")
        
    conn.close()
    ctx = {
        'id': id,
        'nombre': nombre,
        'inscriptos': inscriptos,
    }
    return render(request, 'myapp/uncurso.html', ctx)

def cursos_all(request):
    conn = sqlite3.connect("curso.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, inscriptos FROM cursos;")
    cursos =  cursor.fetchall()
    ctx = {"cursos": cursos}
    conn.close
    return render(request, 'myapp/cursos.html', ctx) 

def nuevoCurso(request):
    if  request.method == "POST":
        form = FormularioCurso(request.POST)
        if form.is_valid():
            #nombre = request.POST.get("nombre")
            #inscriptos = request.POST.get("inscriptos")

            nombre = form.cleaned_data["nombre"]
            inscriptos = form.cleaned_data["inscriptos"]

            conn = sqlite3.connect("curso.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO cursos (nombre, inscriptos) VALUES (?, ?);", (nombre, inscriptos))
            conn.commit()
            conn.close()
            return HttpResponseRedirect(reverse("cursos_all"))
    else:
        form = FormularioCurso()

    ctx = {'form': form}

    return render(request, 'myapp/nuevo_curso.html', ctx)

#___________________________________ ORM

def cursos_orm(request):
    cursos = Curso.objects.all()
    ctx = {"cursos": cursos}
    return render(request, 'myapp/cursos_orm.html', ctx) 

def nuevoCursoORM(request):
    if  request.method == "POST":
        form = FormularioCurso(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("cursos_orm"))
    else:
        form = FormularioCurso()

    ctx = {'form': form}
    return render(request, 'myapp/nuevo_curso.html', ctx)

def cursos_json(request):
    response = JsonResponse(list(Curso.objects.values()), safe=False)
    
    return response