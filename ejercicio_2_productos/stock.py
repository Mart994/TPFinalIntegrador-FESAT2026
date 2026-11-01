class StockInvalidoError(Exception):
    
    def __init__(self, mensaje: str = "El stock no puede ser un valor negativo."):
        super().__init__(mensaje)

class DispositivoEcologico:
    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self._stock = 0
        self.stock = stock

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, nuevo_stock):
        if nuevo_stock < 0:
            raise StockInvalidoError(
                mensaje=f"El stock de {self.nombre} no puede ser negativo. Ingresó {nuevo_stock}"
                )
        
        self._stock = nuevo_stock

    def generar_ficha_tecnica(self):
        return {
            "ID": self.id_producto,
            "Nombre": self.nombre,
            "Precio": f"${self.precio:,.2f}",
            "Stock": self.stock,
        }

    def to_diccionario(self) -> dict:
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
        }

class PanelSolar(DispositivoEcologico):
    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int, eficiencia: float, potencia_w: float):
        super().__init__(id_producto, nombre, precio, stock)
        self.eficiencia = eficiencia
        self.potencia_w = potencia_w

    def generar_ficha_tecnica(self):
        ficha = super().generar_ficha_tecnica()
        ficha.update({
            "Tipo": "Panel Solar",
            "Potencia": f"{self.potencia_w} W",
            "Eficiencia": f"{self.eficiencia:.1f}%",
        })
        return ficha

    

    def to_diccionario(self) -> dict:
        datos = super().to_diccionario()
        datos.update({
            "eficiencia": self.eficiencia,
            "potencia_w": self.potencia_w,
        })
        return datos