def obtener_t(registro: dict[str, str | float]) -> float:
    temperatura = registro["temperatura"]
    if not isinstance(temperatura, (int, float)):
        raise TypeError(f"Temperatura inválida: {temperatura}")
    
    return temperatura

def obtener_sensor(registro: dict[str, str | float]) -> str:
    sensor = registro["sensor_id"]
    if not isinstance(sensor, str):
        raise TypeError(f"Sensor inválido: {sensor}")
    return sensor

def generar_resumen_sensores(
          lista_sensores_limpios: list[dict[str,str | float]], 
          umbral_temperatura: float) -> tuple[list[str], float]:

    if not lista_sensores_limpios:
        return [],0.0

    acum_t = 0.0
    alertas:list[str] = []

    for registro in lista_sensores_limpios:
        temperatura = obtener_t(registro)
        acum_t += temperatura

        if temperatura > umbral_temperatura:
            alertas.append(obtener_sensor(registro))


    promedio = round((acum_t / len(lista_sensores_limpios)),2)

    return alertas, promedio