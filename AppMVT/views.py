from django.shortcuts import render
from .models import Familiares
import datetime
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def familiares(request):
    fecha=datetime.datetime.today()
    padre=Familiares(nombre="Enrique", apellido="Mosquera", edad=64)
    padre.save()
    madre=Familiares(nombre="Alicia", apellido="Ortega", edad=61)
    madre.save()
    hermano1=Familiares(nombre="Julian", apellido="Mosquera", edad=43)
    hermano1.save()
    hermano2=Familiares(nombre="Luciana", apellido="Mosquera", edad=22)
    hermano2.save()
    texto="Hoy es" + str(fecha), f"---Les presento a mi familia: " + f" Ellos son mis padres:--- {padre.nombre} {padre.apellido} tiene {padre.edad} anios y" + f" {madre.nombre} {madre.apellido} tiene {madre.edad} anios.", f"----Mis hermanos son", f" {hermano1.nombre} {hermano1.apellido} tiene {hermano1.edad} anios y", f" {hermano2.nombre} {hermano2.apellido} tiene {hermano2.edad} anios"
    return HttpResponse(texto)

def templateHtml(request):
    fecha=datetime.datetime.today()
    padre=Familiares(nombre="Enrique", apellido="Mosquera", edad=64)
    padre.save()
    madre=Familiares(nombre="Alicia", apellido="Ortega", edad=61)
    madre.save()
    hermano1=Familiares(nombre="Julian", apellido="Mosquera", edad=43)
    hermano1.save()
    hermano2=Familiares(nombre="Luciana", apellido="Mosquera", edad=22)
    hermano2.save()
    texto1=f" {padre.nombre} {padre.apellido} {padre.edad}"
    texto2=f" {madre.nombre} {madre.apellido} {madre.edad}"
    texto3=f" {hermano1.nombre} {hermano1.apellido} {hermano1.edad}"
    texto4=f" {hermano2.nombre} {hermano2.apellido} {hermano2.edad}"
    diccionario={"date" :fecha, "tex1" :texto1, "tex2" :texto2, "tex3" :texto3, "tex4" :texto4}
    plantilla=loader.get_template("templateMVT.html")
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)
    