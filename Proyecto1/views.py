from django.http import HttpResponse
import datetime

document= """
<html>
<body>
<h1>Hola este es mi primer hola mundo con django, for today sunday 7 of july</h1>
</body>
</html>
"""

document_time= """
<html>
<body>
<h1>Hola este es mi primer hola mundo con django, for today sunday 7 of july</h1>
</body>
</html>
"""

current_date=datetime.datetime.now()

def saludo(request):#vista
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

