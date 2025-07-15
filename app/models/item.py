from typing import List

class Item:
    """
    Clase que representa un producto estilo MercadoLibre.
    """
    def __init__(self, id: int, titulo: str, descripcion: str, precio: float,
                 metodos_pago: List[str], vendedor: str, stock: int, imagenes: List[str]):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.precio = precio
        self.metodos_pago = metodos_pago
        self.vendedor = vendedor
        self.stock = stock
        self.imagenes = imagenes

    def a_diccionario(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "metodos_pago": self.metodos_pago,
            "vendedor": self.vendedor,
            "stock": self.stock,
            "imagenes": self.imagenes
        }

    @staticmethod
    def desde_diccionario(data: dict):
        return Item(
            id=data["id"],
            titulo=data["titulo"],
            descripcion=data["descripcion"],
            precio=data["precio"],
            metodos_pago=data["metodos_pago"],
            vendedor=data["vendedor"],
            stock=data["stock"],
            imagenes=data["imagenes"]
        )
