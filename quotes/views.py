from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
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


def index(request):
    days = list(days_of_week.keys())
    return render(request, "quotes/index.html", {
        "days": days
    })


def days_week_with_number(request, day):
    days = list(days_of_week.keys())
    if day > len(days):
        return HttpResponseNotFound("El día no existe")
    redirect_days = days[day-1]
    # EL argumento de <str:day>
    redirect_path = reverse("day-quote", args=[redirect_days])
    # return HttpResponseRedirect(f"/quotes/{redirect_days}") #Sin reverse
    return HttpResponseRedirect(redirect_path)  # Con reverse


def days_week(request, day):
    try:
        quote_text = days_of_week[day]
        return HttpResponse(quote_text)
    except:
        return HttpResponseNotFound("No hay frase ara ese día")
