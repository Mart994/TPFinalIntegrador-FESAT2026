# Trabajo Final Integrador – EcoTech Solutions

Resolución de los tres ejercicios de la evaluación técnica. Cada ejercicio está en su propia carpeta y se ejecuta de forma independiente.

```
ejercicio_1_sensores/        Sanitización y análisis estadístico de sensores
ejercicio_2_productos/       Modelo de productos, excepciones y persistencia JSON
ejercicio_3_auditoria_web/   Tests unitarios y panel web con Django
```

## Requisitos

- Python 3.12 o superior (Django 6.1 lo requiere; los ejercicios 1 y 2 solo usan la biblioteca estándar)

---

## Ejercicio 1 – Sanitización de sensores

```bash
cd ejercicio_1_sensores
python3 main.py
```

| Archivo | Contenido |
|---|---|
| `limpiar.py` | `limpiar_registro_sensor()` y sus funciones auxiliares de limpieza |
| `reporte.py` | `generar_resumen_sensores()`: alertas por umbral y promedio |
| `dicc_raw.py` | 12 registros crudos de prueba con distintos casos de error |
| `main.py` | Flujo completo: limpieza → resumen → reporte formateado |

**Decisiones de diseño**

- **Temperatura:** acepta `int`, `float` o texto (`"24.5C"`, `"31.2°C"`, `"41 ºC"`). Se contemplan los dos símbolos de grado (`°` U+00B0 y `º` U+00BA), que son caracteres distintos.
- **Valores inválidos o ausentes:** la temperatura toma `0.0` (según la guía), y esos sensores también entran en el promedio y lo bajan. La ubicación faltante o vacía toma `"Área No Asignada"`.
- **Fahrenheit:** se quita la unidad pero **no se convierte** a Celsius (por ejemplo, `"45°F"` queda en `45.0`). Es una limitación conocida.
- **Alertas:** un sensor está en alerta si su temperatura es **estrictamente mayor** que el umbral (30 °C en la demostración). El promedio se redondea a 2 decimales.

---

## Ejercicio 2 – Productos, excepciones y persistencia

```bash
cd ejercicio_2_productos
python3 main.py
```

| Archivo | Contenido |
|---|---|
| `stock.py` | `StockInvalidoError`, `DispositivoEcologico` (clase base) y `PanelSolar` (subclase) |
| `gestor.py` | `GestorInventario.guardar_catalogo_json()` |
| `main.py` | Demostración: fichas técnicas, captura de errores y exportación |

**Qué muestra la demostración**

1. Fichas técnicas de todos los productos. La de `PanelSolar` incluye potencia y eficiencia (polimorfismo).
2. Captura controlada de `StockInvalidoError` en dos casos:
   - al **crear** un producto con stock negativo;
   - al **asignar** stock negativo a un producto existente. El stock anterior se conserva.
3. Exportación de los productos válidos a JSON.

**Decisiones de diseño**

- **Encapsulamiento:** el stock se guarda en `_stock` y solo se modifica a través de la propiedad `stock`. El constructor también usa el setter, así que la validación se aplica desde la creación del objeto.
- **Serialización:** cada clase tiene `to_diccionario()`, que guarda los valores **sin formato** (por ejemplo, el precio como número). Así el JSON sirve como datos. La ficha técnica, en cambio, está pensada para mostrarse.
- **Archivo de salida:** se genera en `ejercicio_2_productos/datos/catalogo_ecotech.json`. La ruta se calcula a partir de la ubicación del script, así que funciona desde cualquier directorio. El archivo **no se incluye en el repositorio**: se crea al ejecutar el programa.

---

## Ejercicio 3 – Auditoría con tests y panel web

### Instalación

```bash
cd ejercicio_3_auditoria_web
python3 -m venv venv
source venv/bin/activate          # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Ejecutar los tests

```bash
python manage.py test -v 2
```

Se ejecutan 14 tests:

| Clase | Archivo | Qué verifica |
|---|---|---|
| `TestCalculoEmisiones` | `tests/test_calculos.py` | Exactitud del cálculo (factor por defecto, factor personalizado, decimales, consumo cero) y el `ValueError` ante consumo negativo |
| `TestMetricasConsumo` | `tests/test_calculos.py` | Agrupación por planta, total de emisiones, planta de mayor consumo, lista vacía y propagación del error |
| `TestVistaPanelSustentabilidad` | `sustentabilidad/tests.py` | Respuesta 200, plantilla utilizada, contenido del contexto y datos visibles en el HTML |

> Se usa `python manage.py test` en lugar de `python -m unittest` porque los tests de la vista necesitan la configuración de Django.

### Levantar el panel

```bash
python manage.py runserver
```

Abrir http://127.0.0.1:8000/. Django avisa sobre migraciones sin aplicar; se puede ignorar, porque el proyecto no usa base de datos.

### Estructura

| Ruta | Contenido |
|---|---|
| `utils/calculos.py` | `calcular_emisiones_carbono()` y `obtener_metricas_consumo()`, en Python puro e independientes de Django |
| `registros/anio_26.py` | Historial de consumos de prueba |
| `sustentabilidad/views.py` | `vista_panel_sustentabilidad()` (vista basada en función) |
| `sustentabilidad/templates/sustentabilidad/panel.html` | Plantilla del panel |
| `config/` | Configuración del proyecto Django |

**Decisiones de diseño**

- **"Planta de mayor consumo"** se calcula por **consumo acumulado** de cada planta, no por el registro individual más alto. Los datos de prueba están armados para que ambos criterios den resultados distintos (Norte tiene el registro más alto; Sur, el mayor total), y hay un test que lo verifica.
- **Emisiones:** `obtener_metricas_consumo()` llama a `calcular_emisiones_carbono()` en cada registro. Devuelve las emisiones por planta, el total global y la planta de mayor consumo.
- **Funciones independientes de Django:** los cálculos viven en `utils/`, así se pueden testear sin levantar el servidor.
- **Interfaz:** usa Bootstrap **6.0.0-alpha.1** desde CDN, elegido a propósito para probar la nueva versión. Algunas clases difieren de Bootstrap 5 (por ejemplo, `theme-success` en lugar de `table-success`). La fila de la planta de mayor consumo aparece resaltada.

---

## Uso responsable de la IA

Este trabajo se realizó con la asistencia de **Claude Code** (Anthropic). Antes de empezar se fijaron reglas de uso: la IA actuaría como **tutor**, dando pistas sobre el siguiente paso, sin dar soluciones completas y **sin modificar los archivos del proyecto**. Todo el código fue escrito o incorporado manualmente por mí. La IA leía los archivos y ejecutaba el código y los tests para verificar, revisar y señalar errores.

La excepción acordada desde el inicio fue el ejercicio 3, donde la ayuda con Django y con los tests fue mayor.

| Parte | Rol de la IA |
|---|---|
| **Ejercicio 1** (completo) | Pistas y revisión. Señaló errores (nombres de variables, tipo de dato pasado a la función, directorio de ejecución) y planteó preguntas sobre decisiones de diseño (Fahrenheit, valores `0.0`, `if __name__ == "__main__"`). **Sin código escrito por la IA.** |
| **Ejercicio 2** (completo) | Pistas y revisión: encapsulamiento con `@property` y recursión infinita en el setter, uso de `super()`, serialización con `to_diccionario()`, rutas con `pathlib`, ubicación del `try/except`. **Sin código escrito por la IA.** |
| **Ej. 3: `calcular_emisiones_carbono` y `obtener_metricas_consumo`** | Pistas y revisión (agrupar con un diccionario, inicializar variables, diseño de datos de prueba que distingan los dos criterios de "mayor consumo"). **Sin código escrito por la IA.** |
| **Ej. 3: tests** | **Código escrito por la IA:** las clases `TestCalculoEmisiones`, `TestMetricasConsumo` y `TestVistaPanelSustentabilidad`, con la explicación de cada técnica (`assertAlmostEqual`, `assertRaises`, `setUp`, `patch`, cliente de pruebas de Django). La elección de los casos límite se discutió en conjunto. |
| **Ej. 3: Django** | **Código parcial de la IA:** comandos de creación del proyecto y la app, esqueleto de la vista (el contexto lo completé yo), configuración de `urls.py` y esqueleto de la plantilla (las filas de la tabla las completé yo). También explicó los conceptos de Django en relación con FastAPI, que es lo que yo conocía. |
| **Ej. 3: estilos con Bootstrap** | La elección de Bootstrap 6 alfa fue mía. La IA escribió la versión final de la plantilla con las clases de esa versión, a pedido mío, como mejora estética fuera de lo que pide la consigna. |
| **README** | Redactado por la IA a partir del código y de las decisiones tomadas durante el desarrollo, y revisado por mí. |

Todas las decisiones de diseño (estructura de módulos, nombres, datos de prueba, manejo de errores, criterios de cálculo) fueron mías o se discutieron antes de implementarse.