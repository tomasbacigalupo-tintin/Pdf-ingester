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
