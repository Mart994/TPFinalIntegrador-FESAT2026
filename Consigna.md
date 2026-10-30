# ECOTECH SOLUTIONS – EVALUACIÓN TÉCNICA DE DESARROLLO

## Especificaciones generales de entrega

El proyecto final debe cumplir estrictamente con los siguientes lineamientos de organización y despliegue:

- **Modalidad de entrega:** mediante un enlace a un repositorio público de GitHub o a través de un archivo comprimido en formato ZIP.
- **Estructura del proyecto:** el código fuente debe estar modularizado y segmentado en carpetas separadas e independientes para cada uno de los tres ejercicios:
  - `ejercicio_1_sensores/`
  - `ejercicio_2_productos/`
  - `ejercicio_3_auditoria_web/`
- **Framework de pruebas:** para las pruebas automatizadas del ecosistema Django, se autoriza y promueve el uso del framework `pytest` (o, en su defecto, el módulo nativo `unittest`).
- **Arquitectura de vistas (Django):** se permite la libertad de implementar la capa de presentación web mediante Vistas Basadas en Clases (**CBV**) o Vistas Basadas en Funciones (**FBV**), según el criterio del desarrollador.
- **Simulación de datos:** para el procesamiento y renderizado de métricas en el panel web, los datos de entrada pueden ser consumidos desde un archivo CSV, un diccionario o mediante un JSON inventado con registros realistas de prueba.

**¡Buena suerte!**

---

# Ejercicio 1: Sanitización y análisis estadístico de sensores

**Puntaje: 20 puntos**

Los microcontroladores de EcoTech Solutions transmiten lecturas térmicas en formato heterogéneo, con espacios indeseados, textos mezclados con unidades de medida y atributos incompletos.

Se necesita un componente que normalice estos registros individuales y genere un reporte consolidado para la toma de decisiones.

### Punto A: Normalización de lecturas (`limpiar_registro_sensor`)

Diseñá la función `limpiar_registro_sensor(registro_raw)`, encargada de procesar un diccionario con datos crudos de un sensor.

Por ejemplo:

```python
{
    "sensor_id": " SENSOR-001 ",
    "temperatura": "24.5C",
    "ubicacion": "Planta Norte"
}
```

La función debe transformar la información para retornar un nuevo diccionario estandarizado, garantizando que:

- El identificador quede sin espacios sobrantes.
- La temperatura sea un valor numérico de tipo `float`, sin sufijos de unidad.
- La ubicación posea un valor por defecto seguro en caso de no haberse registrado.

### Punto B: Monitoreo y mapeo estadístico (`generar_resumen_sensores`)

Desarrollá la función `generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura)`, que tome una colección de registros sanitizados previamente con la función del Punto A y un valor límite.

La función debe retornar una tupla:

```python
(lista_sensores_alerta, promedio_temperatura)
```

Esta tupla debe contener:

- **`lista_sensores_alerta`:** los IDs de los dispositivos que superan el umbral estipulado.
- **`promedio_temperatura`:** el promedio térmico global de la planta.

Incluí un bloque de ejecución que demuestre el flujo completo, desde la limpieza de registros crudos hasta la impresión formateada del reporte final.

---

# Ejercicio 2: Modelo de productos, excepciones y persistencia

**Puntaje: 40 puntos**

Para la división de equipamiento sustentable de EcoTech Solutions, se requiere un módulo de software que gestione los productos del catálogo, impida inconsistencias en el inventario mediante validaciones de negocio y garantice la persistencia del stock en disco.

### Punto A: Dominio del catálogo y reglas de inventario

Construí la jerarquía orientada a objetos para los productos ecológicos.

Los requisitos son los siguientes:

1. Diseñá una clase de excepción personalizada `StockInvalidoError`.
2. Aplicá dicha excepción dentro de la clase base `DispositivoEcológico` para impedir que el stock tome valores negativos mediante encapsulamiento explícito.
3. Desarrollá la clase especializada `PanelSolar`, incorporando sus atributos específicos mediante herencia y aplicando polimorfismo para personalizar la emisión de su ficha técnica comercial.

### Punto B: Persistencia y gestión del catálogo

Implementá la clase `GestorInventario` con el método:

```python
guardar_catalogo_json(lista_dispositivos, ruta_archivo)
```

Este método debe ser capaz de serializar y almacenar en `catalogo_ecotech.json` las instancias creadas en el Punto A.

Incluí un bloque de prueba en el que se verifique:

- La captura controlada de `StockInvalidoError` ante un intento de asignación de stock erróneo.
- La exportación exitosa de los productos válidos al archivo JSON.

---

# Ejercicio 3: Auditoría con tests unitarios e integración web

**Puntaje: 40 puntos**

Previo a la puesta en producción, EcoTech Solutions debe certificar la precisión del algoritmo de cálculo de huella de carbono industrial.

Tras auditar su comportamiento mediante pruebas automatizadas, dicho algoritmo debe integrarse en la tubería de datos que alimenta la interfaz web administrativa de la empresa.

### Punto A: Auditoría de algoritmo de emisiones (`unittest`)

A partir de la función:

```python
calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4)
```

La función eleva una excepción `ValueError` si el consumo es negativo.

Implementá la clase de prueba:

```python
class TestCalculoEmisiones(unittest.TestCase):
```

Diseñá los casos de prueba necesarios para validar:

- La exactitud numérica del cálculo ante valores nominales.
- La correcta elevación de la excepción ante consumos fuera de rango.

### Punto B: Procesamiento de métricas y renderizado web

Incorporá la función `calcular_emisiones_carbono` en la función:

```python
obtener_metricas_consumo(registros)
```

Esta función debe procesar un historial de consumos por planta industrial para determinar:

- El total global de emisiones.
- La planta de mayor consumo.

Por último, diseñá la función de vista en Django:

```python
vista_panel_sustentabilidad(request)
```

Esta vista debe invocar dicho procesamiento y proporcionar el diccionario de contexto listo para ser renderizado en la plantilla:

```text
sustentabilidad/panel.html
```