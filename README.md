# ⚡ Asset Optimizer (CSS / JS Minifier)

> **An automation script that scans your project, fixes common syntax issues and generates highly compressed `.min.css` and `.min.js` files.**

Asset Optimizer is a terminal tool that walks your project tree to find non-minified `.css` and `.js` files. It repairs common formatting issues that break some minifiers and produces `.min.*` files alongside originals.

## ✨ Features

- **Syntax Repair & Compatibility:** Fixes problematic line breaks and whitespace that cause other minifiers to fail.
- **Auto-Installer:** Installs dependencies (`csscompressor`, `jsmin`) automatically and restarts.
- **Compression Analytics:** Reports size reduction (bytes and percent) per file.
- **Smart Exclusion:** Recursively scans but ignores configured dev or legacy folders.

---

## ⚙️ Requirements

- Python 3.8 or newer.

Dependencies are managed automatically: `csscompressor`, `jsmin`.

Run the optimizer from project root; adjust `EXCLUDE_DIRS` in `minify_assets.py` if needed.

## Usage

1. (Optional) Edit `minify_assets.py` and set `EXCLUDE_DIRS` if you need to ignore folders (defaults may include `dev`, `node_modules`, `ver1`, `ver2.5_fail`).
2. Run the optimizer from the project root:

```bash
python dev/scripts/asset-optimizer/minify-asset-optimizer.py
```

The script will create or overwrite `.min.*` files next to the originals and print a compression report.

[![Leer en Español](https://img.shields.io/badge/Leer%20en%20Espa%C3%B1ol-ES-blue?style=flat-square&logo=github)](README_es.md)

## Changelog

- v1.0: Initial implementation with basic CSS/JS support.
- v1.1: Improved exclusion logic (`EXCLUDE_DIRS`) and per-file error handling.
- v1.2: Added compression analytics and terminal reports.
- v2.0: Auto-installer for dependencies and fixes for formatting edge-cases.
