from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import sqlite3

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
    return HttpResponse(html)

def welcome(request):
    return render(request, 'myapp/bienvenido.html')