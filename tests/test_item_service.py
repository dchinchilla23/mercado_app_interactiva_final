import pytest
from app.servicios.item_service import ServicioItem
from app.modelos.producto import Item

@pytest.fixture
def servicio_temporal(tmp_path):
    ruta = tmp_path / "productos.json"
    datos = [{
        "id": 1,
        "titulo": "Test Item",
        "descripcion": "Descripción de prueba",
        "precio": 100.0,
        "metodos_pago": ["Tarjeta", "Efectivo"],
        "vendedor": "Tienda Test",
        "stock": 10,
        "imagenes": ["https://test.com/imagen.jpg"]
    }]
    ruta.write_text(str(datos).replace("'", '"'), encoding="utf-8")
    return ServicioItem(str(ruta))

def test_cargar_productos(servicio_temporal):
    productos = servicio_temporal.cargar_productos()
    assert len(productos) == 1
    assert productos[0].titulo == "Test Item"

def test_obtener_producto_por_id(servicio_temporal):
    producto = servicio_temporal.obtener_producto_por_id(1)
    assert producto is not None
    assert producto.descripcion == "Descripción de prueba"

def test_producto_no_encontrado(servicio_temporal):
    producto = servicio_temporal.obtener_producto_por_id(999)
    assert producto is None
