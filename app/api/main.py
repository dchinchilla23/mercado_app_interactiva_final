from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.services.item_service import ItemService

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

servicio = ItemService("app/data/items.json")

#listado de productos.
@app.get("/productos/{id_item}")
def obtener_item(id_item: int):
    item = servicio.obtener_item_por_id(id_item)
    if item is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return item.a_diccionario()
# se agregan la lista de productos
@app.get("/productos")
def obtener_todos_los_items():
    items = servicio.cargar_items()
    return [item.a_diccionario() for item in items]
