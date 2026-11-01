import json
from pathlib import Path


class GestorInventario:
    
    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        ruta = Path(ruta_archivo)
        datos = [dispositivo.to_diccionario() for dispositivo in lista_dispositivos]

        try:
            # crea el directorio si no existe
            ruta.parent.mkdir(parents=True, exist_ok=True)
            # crea el archivo
            with ruta.open("w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
        except OSError as e:
            print(f"Error al guardar el catálogo: {e}")
            return False

        return True
        
        