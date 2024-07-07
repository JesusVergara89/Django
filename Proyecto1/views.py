from django.http import HttpResponse
import datetime
from django.template import Template, Context

document_time= """
<html>
<body>
<h1>Hola este es mi primer hola mundo con django, for today sunday 7 of july</h1>
</body>
</html>
"""
current_date=datetime.datetime.now()

def saludo(request):#vista
    doc_exteno=open("/Volumes/harkdisk/Projects/Django/Proyecto1/Proyecto1/Plantillas/miplantilla.html")
    plt=Template(doc_exteno.read())
    doc_exteno.close()
    ctx=Context()
    document=plt.render(ctx)
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

