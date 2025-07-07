# Arquitectura de Extracción y Validación de Teléfonos

Este documento resume la propuesta para una solución escalable que permite procesar archivos PDF, extraer números telefónicos y notificarlos automáticamente. La idea principal es desacoplar cada etapa en microservicios comunicados por colas para lograr alta disponibilidad y trazabilidad.

## Flujo General
```
UI/API -> Ingesta PDFs -> Extracción de texto -> Normalización y validación -> Mensajería -> Logging y Dashboard
```
Cada módulo funciona de manera asíncrona para repartir la carga y reintentar fallos sin bloquear el flujo.

## Herramientas Clave
- **FastAPI** para la API de ingesta.
- **pdfplumber / pdfminer.six** para extraer texto de PDFs.
- **pytesseract** para OCR de PDFs escaneados.
- **phonenumbers** y expresiones regulares para detectar y normalizar teléfonos.
- **Twilio Lookup** (u otra API) para validar la existencia de los números.
- **WhatsApp Business API**, **SMS** o **Email** para notificaciones.
- **Celery + RabbitMQ** (o AWS SQS) para colas de trabajo.
- **Logging** estructurado con almacenamiento en PostgreSQL.
- **Streamlit** o React para un dashboard de monitoreo.

## Métricas para la PoC
- Porcentaje de PDFs procesados sin errores.
- Precisión de extracción de teléfonos (>95%).
- Tiempo promedio de procesamiento por PDF.

La implementación inicial puede concentrarse en la ingesta, extracción de texto y detección básica de teléfonos. Posteriormente se añadirán la validación externa, la mensajería multicanal y un sistema de monitoreo más robusto.

## Implementación de referencia

En esta PoC se incluyó un pequeño servicio basado en **FastAPI** que expone un endpoint `/ingest` para subir un PDF. El flujo de procesamiento se realiza de manera secuencial mediante los siguientes módulos:

- `pdf_ingester.ingestion` guarda el archivo en disco.
- `pdf_ingester.extraction` utiliza `pdfminer.six` para obtener el texto.
- `pdf_ingester.phone` detecta y normaliza los números telefónicos mediante `phonenumbers`.
- `pdf_ingester.pipeline` orquesta los pasos anteriores.

Este código sirve como punto de partida para evolucionar hacia una arquitectura de microservicios con colas de mensajes y procesos asíncronos.
