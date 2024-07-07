from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

document_time= """
<html>
<body>
<h1>Hola este es mi primer hola mundo con django, for today sunday 7 of july</h1>
</body>
</html>
"""
current_date=datetime.datetime.now()

temas_delCurso=["plantilla", "listas","cargadores", "comentarios"]

def saludo(request):#vista
    p1=Persona("Jesus","vergara")
    #doc_exteno=open("/Volumes/harkdisk/Projects/Django/Proyecto1/Proyecto1/Plantillas/miplantilla.html")
    #plt=Template(doc_exteno.read())
    #doc_exteno.close()
    doc_exteno = get_template("miplantilla.html")
    #ctx=Context({"main_name": p1.nombre, "main_surname": p1.apellido, "temas": temas_delCurso})
    document=doc_exteno.render({"main_name": p1.nombre, "main_surname": p1.apellido, "temas": temas_delCurso})
    return HttpResponse(document)

def despedida(request):
    return HttpResponse("Adios")

def gitmeDate(request):
    current_date=datetime.datetime.now()

    document_time= """
    <html>
    <body>
     <h3>Fecha y hora actuales %s </h3>
    </body>
    </html>
     """%current_date
    
    return HttpResponse(document_time)

def calcula_edad(request, age, year_):
    #current_age=age
    period=year_-current_date.year
    future_age=age+period
    document_age="""
    <html>
    <body>
     <h3>El el año {} tendras {} años </h3>
    </body>
    </html>
    """.format(year_,future_age)
    return HttpResponse(document_age)

