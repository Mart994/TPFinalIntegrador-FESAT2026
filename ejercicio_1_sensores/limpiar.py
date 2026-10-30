def limpiar_temperatura(t: str | float | None ) -> float:
    if not t:
        return 0.0

    if isinstance(t, (int, float)):
        return float(t)

    #normalizo a mayusculas para el str
    temp = t.upper()
    # descubrí que ° es U+00B0 y º es U+00BA, son caracteres diferentes
    temp = temp.strip().replace("º", "").replace("°", "").replace("C", "").replace("F", "")

    try:
        return float(temp)
    except ValueError:
        return 0.0


def limpiar_ubicacion( u ):
    if u:
        u = u.strip()
    
    return u or "Área No Asignada"

# -----------

def limpiar_registro_sensor(
    registro_raw: dict[str, str | float],
) -> dict[str, str | float]:

    sensor_id = str(registro_raw.get("sensor_id", "")).strip() 

    temperatura= limpiar_temperatura(registro_raw.get("temperatura"))

    ubicacion = limpiar_ubicacion(registro_raw.get("ubicacion"))

    registro_limpio: dict[str, str | float] = {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion,
    }

    return registro_limpio
