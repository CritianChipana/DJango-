from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def saludo(request):
    estudiantes = [
        'SERGIO DANIEL VITE COCHACHIN',
        'ANTHONY GERARDO BENDEZU SANTISTEBAN',
        'CRISTIAN ALEXIS CHIPANA HUAMAN',
        'CARLOS GUSTAVO OYOLA SAAVEDRA',
        'GERARDO MANUEL CASTILLO TORDOYA'
    ]
    
    

    return render(request,"saludo.html",{"estudiantes":estudiantes})


def index(request):
    return render(request,"index.html")

def rango(request,a=10,b=20):

    a = 10
    b= 20
    rango_numeros = range(a,b+1)
    return render(request,"rango.html",{'a':a,'b':b,"rango_numeros":rango_numeros})


def rango2(request,a=0, b=100):

    if a>b:
        return redirect('rango2',a=b,b=a)

    resultado = f"""
        <h2> Rango con parámetros </h2>
        <h2> Número de [{a},{b}] </h2>
        Resultado: <br>
        <ul>
    """
    while a<=b:
        resultado+= f"<li>{a}</li>"
        a+=1
    resultado += "</ul>"
    return HttpResponse(resultado)