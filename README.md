# Asset Optimizer — `minify_assets.py`

Descripción

- Escanea el árbol del proyecto en busca de archivos `.css` y `.js` no minificados y genera las versiones minificadas (`.min.css` / `.min.js`).

Características

- Recorrido recursivo desde la raíz del repositorio, ignorando carpetas configuradas en `EXCLUDE_DIRS`.
- Calcula y muestra la reducción de tamaño por archivo.
- Auto-instala dependencias (`csscompressor`, `jsmin`) si faltan y reinicia el script para cargarlas.

Requisitos

- Python 3.8+
- Paquetes: `csscompressor`, `jsmin` (el script se encargará de instalarlos si es necesario).

Uso

- Ejecutar desde la raíz del proyecto:

```bash
python dev/scripts/asset-optimizer/minify_assets.py
```

Detalles técnicos

- `EXCLUDE_DIRS` controla carpetas omitidas (por defecto incluye `dev`, `node_modules`, `ver1`, `ver2.5_fail`). Ajusta según tu estructura.
- El script sobrescribe la salida `.min.*` si ya existe.
- Si una dependencia falta, el script intentará instalarla y luego reiniciará el intérprete para cargar los módulos instalados.

Evolución (resumen)

- Implementación inicial con soporte para CSS y JS.
- Añadido autoinstalador de dependencias y reinicio automático.
- Cálculo de reducción de tamaño y mensajes informativos.
- Mejora en exclusiones de carpetas y manejo de errores por archivo.
