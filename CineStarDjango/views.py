from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from django.db import connection

#Vistas
def Index(request):
  return render(request,'index.html')

def Peliculas(request,id):
  if id == "cartelera":
    parametro = 1
  else:
    parametro = 2
  cursor = connection.cursor()
  cursor.execute('call sp_getPeliculas(%s)', [parametro])
  resultados = cursor.fetchall()
  cursor.close()
  context = {
        'peliculas': resultados,
        }
  return render(request,'peliculas.html', context)

def Pelicula(request,id):
    cursor = connection.cursor()
    cursor.execute('call sp_getPelicula(%s)', [id])
    resultados = cursor.fetchall()
    cursor.close()
    context = {
    'pelicula': resultados,
    }
    return render(request,'pelicula.html', context)


def Cines(request):
    cursor = connection.cursor()
    cursor.execute('call sp_getCines')
    resultados = cursor.fetchall()
    cursor.close()
    context = {
      'cines': resultados,
    }
    return render(request,'cines.html', context)


def Cine(request,id):
    cursor = connection.cursor()
    cursor.execute('call sp_getCine(%s)', [id])
    resultCine = cursor.fetchall()

    cursor.execute('call sp_getCineTarifas(%s)', [id])
    resultTarifas = cursor.fetchall()

    cursor.execute('call sp_getCinePeliculas(%s)', [id])
    resultPeliculas = cursor.fetchall()

    cursor.close()

    context = {
      'cine': resultCine,
      'tarifas' : resultTarifas,
      'peliculas' : resultPeliculas,
    }
    return render(request,'cine.html', context)