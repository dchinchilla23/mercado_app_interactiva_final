import json
from typing import List, Optional
from app.models.item import Item

class ItemService:
    def __init__(self, ruta_archivo: str):
        self.ruta_archivo = ruta_archivo

    def cargar_items(self) -> List[Item]:
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                return [Item.desde_diccionario(p) for p in datos]
        except FileNotFoundError:
            return []

    def obtener_item_por_id(self, id_item: int) -> Optional[Item]:
        items = self.cargar_items()
        for item in items:
            if item.id == id_item:
                return item
        return None
