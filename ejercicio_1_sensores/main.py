from dicc_raw import sensores_crudos
from limpiar import limpiar_registro_sensor
from reporte import generar_resumen_sensores


def main():

    UMBRAL = 30.0
    
    sensores_limpios = [
        limpiar_registro_sensor(registro)
        for registro in sensores_crudos
    ]

    print("\n========== REPORTE DE SENSORES ==========\n")

    print(f"Total de sensores procesados: {len(sensores_limpios)}")
    print(f"Umbral de temperatura: {UMBRAL:.1f} °C")

    print("\n--- Sensores limpios ---")

    for sensor in sensores_limpios:
        print(
            f"Sensor: {sensor['sensor_id']:<10} | "
            f"Temperatura: {sensor['temperatura']:>6.1f} °C | "
            f"Ubicación: {sensor['ubicacion']}"
        )

    alertas, promedio = generar_resumen_sensores(sensores_limpios, UMBRAL)

    print("\n--- Resumen ---")
    print(f"Sensores en alerta: {len(alertas)}")

    if alertas:
        print(f"Identificadores: {', '.join(alertas)}")
    else:
        print("No hay sensores en alerta.")

    print(f"Temperatura promedio: {promedio:.2f} °C")

    print("\n=========================================\n")

if __name__ == "__main__":
    main()