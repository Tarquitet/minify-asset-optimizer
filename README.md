# ⚡ Asset Optimizer (CSS / JS Minifier)

> **Un script de automatización en Python que escanea tu proyecto, corrige errores comunes de sintaxis y genera versiones ultra-comprimidas de tus recursos web.**

**Asset Optimizer** es una herramienta de terminal que recorre el árbol de directorios de tu proyecto para localizar archivos `.css` y `.js` sin minificar. A diferencia de las extensiones estándar, este script procesa y repara errores de formato (saltos de línea y espacios en blanco) que suelen causar fallos en minificadores populares como Terser o las extensiones de VSCode, generando archivos `.min.css` y `.min.js` altamente optimizados.

## ✨ Características Principales

- **🛠️ Corrección y Compatibilidad Superior:** Arregla de forma nativa los errores provocados por saltos de línea y espacios problemáticos que hacen fallar a otras herramientas (como Terser.org o VSCode Minify).
- **🤖 Auto-Instalador Inteligente:** Si el usuario no tiene las dependencias necesarias (`csscompressor`, `jsmin`), el script las instala automáticamente y se reinicia solo para continuar el proceso sin interrupciones.
- **📊 Analítica de Compresión:** Calcula y muestra en la terminal la reducción exacta de tamaño (en peso y porcentaje) lograda por cada archivo procesado.
- **🛡️ Búsqueda Inteligente (Smart Exclusion):** Recorre el proyecto recursivamente pero ignora carpetas de desarrollo o versiones antiguas configuradas por el usuario.

---

## ⚙️ Requisitos e Instalación

**Requisitos del sistema:**

- Python 3.8 o superior.

**Dependencias (gestionadas automáticamente):**

- `csscompressor`
- `jsmin`
  _(Nota: No necesitas instalar nada manualmente. El script detectará si faltan estos paquetes, los instalará vía `pip` y reiniciará el intérprete para cargarlos)._

---

## 📖 Guía de Uso

El uso es directo mediante la terminal desde la raíz de tu proyecto.

1. **Configuración (Opcional):**
   Abre el archivo `minify_assets.py` y ajusta la variable `EXCLUDE_DIRS` si necesitas omitir carpetas específicas (por defecto excluye: `dev`, `node_modules`, `ver1`, `ver2.5_fail`).
2. **Ejecutar el optimizador:**

   ```bash
   python dev/scripts/asset-optimizer/
   minify-asset-optimizer.py

    Resultado: El script sobrescribirá (o creará) los archivos .min.* junto a los originales y te mostrará el reporte de ahorro de espacio.
   ```

📈 Evolución del Proyecto (Changelog)

v1.0: Implementación inicial con soporte base para CSS y JS.

v1.1: Mejora en el sistema de exclusión de carpetas (EXCLUDE_DIRS) y manejo de errores por archivo.

v1.2: Incorporación del cálculo de reducción de tamaño y reportes visuales en terminal.

v2.0 (Actual): Adición del auto-instalador de dependencias con reinicio automático y parches para la corrección de errores de sintaxis/espaciado.
