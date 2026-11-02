from django.shortcuts import render

from registros.anio_26 import registros
from utils.calculos import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    metricas = obtener_metricas_consumo(registros)

    contexto = {
         "metricas": metricas,
    }

    return render(request, "sustentabilidad/panel.html", contexto)