# Pdf-ingester

Este repositorio contiene una prueba de concepto para ingerir archivos PDF, extraer números de teléfono y notificarlos de forma automática. Consulta [docs/ARQUITECTURA.md](docs/ARQUITECTURA.md) para una descripción de la arquitectura propuesta.

## Uso rápido

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Ejecuta la API con Uvicorn:
   ```bash
   uvicorn app:app --reload
   ```

3. Envía un PDF al endpoint `/ingest` para obtener los teléfonos detectados.

## Pruebas

Ejecuta `pytest` para correr las pruebas unitarias.
