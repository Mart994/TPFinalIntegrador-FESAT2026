
def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo")
    return consumo_kwh * factor_emision

def obtener_metricas_consumo(registros):
    metricas_por_planta = {}
    planta_maxima = None
    consumo_maximo = 0
    total_emisiones = 0

    for registro in registros:
        planta = registro["planta"]
        consumo = registro["consumo_kwh"]

        emision = calcular_emisiones_carbono(consumo_kwh=consumo)

        if planta not in metricas_por_planta:
            metricas_por_planta[planta] = {
                "consumo_kwh": 0,
                "emisiones_carbono": 0
            }

        metricas_por_planta[planta]["consumo_kwh"] += consumo
        metricas_por_planta[planta]["emisiones_carbono"] += emision

        consumo_actual = metricas_por_planta[planta]["consumo_kwh"]

        if consumo_actual > consumo_maximo:
            consumo_maximo = consumo_actual
            planta_maxima = planta

        total_emisiones += emision
        

    return {
        "metricas_por_planta": metricas_por_planta,
        "planta_maxima": planta_maxima,
        "consumo_maximo": consumo_maximo,
        "total_emisiones": total_emisiones
    }