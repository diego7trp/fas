# Migración inicial de Spring Boot a Django

Este módulo contiene una **base funcional en Django** para empezar la migración del sistema F.A.S.

## Qué ya quedó migrado

- Proyecto Django (`fas`) y app principal (`core`).
- Modelos de dominio equivalentes a las entidades Java:
  - `User`, `Lider`, `Jugador`
  - `Escuela`, `Categoria`, `Cancha`, `Entrenamiento`
  - `Ubicacion`, `Torneo`, `InscripcionTorneo`
- Configuración para reutilizar templates y estáticos existentes en `src/main/resources/...`.
- Rutas iniciales para landing, login y registro.
- Registro de modelos en el admin.

## Ejecutar local

```bash
cd django_fas
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Próximos pasos de migración

1. Migrar controladores Spring a views Django (CBV/FBV).
2. Reemplazar seguridad de Spring Security por autenticación/autorización Django.
3. Crear formularios Django para CRUDs.
4. Adaptar templates Thymeleaf a sintaxis Django (`{% %}` y `{{ }}`).
5. Configurar MySQL en `settings.py` para apuntar a la misma base (o nueva base de transición).
6. Crear estrategia de migración de datos (ETL) desde tablas actuales.
