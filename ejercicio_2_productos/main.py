from pathlib import Path

from gestor import GestorInventario
from stock import DispositivoEcologico, PanelSolar, StockInvalidoError

DIR_BASE = Path(__file__).parent
DIR_DATOS = DIR_BASE / "datos"
RUTA_CATALOGO = DIR_DATOS / "catalogo_ecotech.json"

def crear_catalogo_valido() -> list:
    return [
        DispositivoEcologico("E01", "Horno Solar",1234.5, 5),
        DispositivoEcologico("E02", "Termotanque Solar", 1999.9, 8),
        PanelSolar("P02", "Panel Solar", 2000.0, 5, 15.5, 47)
    ]

def probar_catalogo_invalido(catalogo: list) -> None:
    # Caso de stock negativo
    try:
        panel_malo = PanelSolar("P99", "Panel Trucho", 5000, -5, 10.0, 50)
        catalogo.append(panel_malo)
    except StockInvalidoError as e:
        print(f"Error: {e}")

    # Caso stock negativo al modificar uno existente
    producto = catalogo[0]
    try:
        producto.stock = -8
    except StockInvalidoError as e:
        print(f"Error capturado al asignar: {e}")

    print(f"El stock de {producto.nombre} no fue modificado, stock = {producto.stock}")


def guardar(catalogo: list):
    gestor = GestorInventario()
    if gestor.guardar_catalogo_json(catalogo, RUTA_CATALOGO):
        print(f"Se exportaron {len(catalogo)} productos a {RUTA_CATALOGO}")

if __name__ == "__main__":
    catalogo = crear_catalogo_valido()

    for producto in catalogo:
        print(producto.generar_ficha_tecnica())

    probar_catalogo_invalido(catalogo)
    guardar(catalogo)