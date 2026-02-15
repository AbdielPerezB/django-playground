from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "landing/landing.html", {
        "name": "Abdiel"
    }) 
    
    
    
    
# NOtad del -----return render(request, "landing/landing.html", dict) ------
# En realidad la ruta sería "templates/landing/landing.hmtl"
# Sin embargo, django ya sabe que es en la carpeta templates, así que solo
# agregamos la subcarpeta landing y el nombre del archivo landing.html.

# El dict que le pasamos como 3er parámetro son variables a las
# que podemos acceder desde el template en DTL (Django Templeta Language)
# (Interpolación de datos)