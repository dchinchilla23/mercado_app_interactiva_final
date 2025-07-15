# Proyecto Mercado App

Aplicación de detalle de productos estilo MercadoLibre.

## Estructura
- Backend con FastAPI
- Arquitectura basada en Programación Orientada a Objetos
- Datos simulados en archivo JSON

## Levantar
- Instalar dependencias: pip install -r requirements.txt
- Ejecutar: uvicorn main:app --reload

1. ejecución desde la raíz. backend
uvicorn app.api.main:app --reload

para acceder a los productos debemos ingresar a 
http://localhost:8000/productos (lista completa)
http://localhost:8000/productos/1 (detalle)

## Autor
Diego Chinchilla