# ⚡ Asset Optimizer (Minificador CSS / JS)

> **Un script que recorre el proyecto, corrige errores comunes de sintaxis y genera versiones `.min.css` y `.min.js` altamente comprimidas.**

Asset Optimizer es una herramienta de terminal que localiza archivos `.css` y `.js` sin minificar, repara errores de formato y crea los archivos `.min.*` junto a los originales.

## ✨ Características

- **Corrección y compatibilidad:** Arregla saltos de línea y espacios que hacen fallar a otros minificadores.
- **Auto-instalador:** Instala `csscompressor` y `jsmin` automáticamente y se reinicia.
- **Analítica de compresión:** Muestra la reducción de tamaño por archivo.
- **Exclusión inteligente:** Ignora carpetas de desarrollo o versiones antiguas configuradas.

---

## ⚙️ Requisitos

- Python 3.8 o superior.

Las dependencias se gestionan automáticamente: `csscompressor`, `jsmin`.

Ejecútalo desde la raíz del proyecto y ajusta `EXCLUDE_DIRS` en `minify_assets.py` si es necesario.

[![Read in English](https://img.shields.io/badge/Read%20in%20English-EN-blue?style=flat-square&logo=github)](README.md)

## Uso

1. Selecciona la carpeta de imágenes que quieres optimizar.
2. Elige el formato de salida (AVIF, WEBP, JPG) y la calidad deseada.
3. Revisa la vista previa y confirma para procesar en lote.
4. Los archivos optimizados se guardarán en una carpeta `output/` dentro de la carpeta seleccionada.

## Changelog

- v0.1: Versión inicial con soporte básico para conversión a WebP/AVIF.
- v0.2: Añadida opción de calidad y ajustes por lotes.
- v0.3: Mejoras en la detección de subcarpetas y preservación de metadatos.
- v0.4: Corrección de errores en nombres con espacios y compatibilidad Windows mejorada.
