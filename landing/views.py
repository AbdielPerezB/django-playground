from datetime import date

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    today = date.today()
    stack = [
        {'id': 'python', 'name': 'Python'},
        {'id': 'django', 'name': 'Django'},
        {'id': 'javascript', 'name': 'JavaScript'},
        {'id': 'react', 'name': 'React'}
    ]
    return render(request, "landing/landing.html", {
        "name": "Abdiel",
        "age": 25,
        "today": today,
        "stack": stack,
    }) 
    
# Notad del -----return render(request, "landing/landing.html", dict) ------
# En realidad la ruta sería "templates/landing/landing.hmtl"
# Sin embargo, django ya sabe que es en la carpeta templates, así que solo
# agregamos la subcarpeta landing y el nombre del archivo landing.html.

# El dict que le pasamos como 3er parámetro son variables a las
# que podemos acceder desde el template en DTL (Django Templeta Language)
# (Interpolación de datos)

def stack_detail(request, tool: str):
    return HttpResponse(f"Tecnología: {tool}")