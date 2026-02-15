from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

days_of_week = {
    "monday": "Piendo, luego existo",
    "tuesday": "La vida es un sueño",
    "wednesday": "El conocimiento es poder",
    "thursday": "Se el cambio que quieres ver",
    "friday": "Solo sé que no sé nada",
    "saturday": "Vive como si fuera el último día",
    "sunday": "Da un poquito más todos lod días"
}


def days_week_with_number(request, day):
    return HttpResponse(day)


def days_week(request, day):
    try:
        quote_text = days_of_week[day]
        return HttpResponse(quote_text)
    except:
        return HttpResponseNotFound("No hay frase ara ese día")
