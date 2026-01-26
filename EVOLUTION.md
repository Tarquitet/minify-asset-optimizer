# Evolución detallada — `minify_assets.py`

Motivación

- Automatizar la creación de versiones minificadas para mejorar tiempos de carga y reducir tamaño de entrega en producción.

Hitos técnicos

- Auto-installer: `setup_dependencies()` verifica imports y, si faltan, intenta instalar paquetes (`csscompressor`, `jsmin`) y reinicia el proceso con `os.execv` para cargar los módulos instalados.
- Recorrido controlado: durante `os.walk` se filtran directorios definidos en `EXCLUDE_DIRS` para evitar procesar dependencias o scripts de desarrollo.
- Minificación: usa `csscompressor.compress` para CSS y `jsmin.jsmin` para JS; genera archivos `.min.<ext>` y calcula reducción absoluta y porcentual.
- Resiliencia: captura excepciones por archivo y continúa con el resto (no detiene todo el proceso por un error aislado).

Consideraciones y mejoras propuestas

- Añadir opciones para mantener comentarios o generar sourcemaps.
- Agregar una lista blanca/negra de rutas o patrones por proyecto.
- Soporte incremental (procesar solo archivos cambiados) para acelerar ejecuciones repetidas.
