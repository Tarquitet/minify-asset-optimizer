import os
import re
import glob

# CONFIGURACIÓN
TARGET_DIR = "./"  # Directorio donde buscar (./ es la carpeta actual)
IGNORE_DIRS = ["node_modules", ".git", "__pycache__", "venv"]

def protect_strings(content):
    """
    Encuentra todos los strings (comillas simples, dobles y backticks)
    y los reemplaza con un placeholder ###STR_N###.
    Retorna el contenido enmascarado y la lista de strings guardados.
    """
    protected_strs = []
    
    def replace_match(match):
        s = match.group(0)
        protected_strs.append(s)
        return f"###STR_{len(protected_strs)-1}###"

    # Regex robusto para strings JS/CSS, maneja caracteres escapados (\")
    # Captura: "..." O '...' O `...`
    pattern = r'''((?:\"(?:[^\"\\]|\\.)*\"|'(?:[^'\\]|\\.)*'|`(?:[^`\\]|\\.)*`))'''
    masked_content = re.sub(pattern, replace_match, content, flags=re.DOTALL)
    
    return masked_content, protected_strs

def restore_strings(content, protected_strs):
    """Restaura los strings originales en sus placeholders."""
    for i, s in enumerate(protected_strs):
        content = content.replace(f"###STR_{i}###", s)
    return content

def minify_logic(content, file_ext):
    # 1. ENMASCARAR STRINGS (Protección total)
    masked, strings = protect_strings(content)

    # 2. ELIMINAR COMENTARIOS (Seguro ahora que no hay strings)
    # Bloque /* ... */
    masked = re.sub(r'/\*.*?\*/', '', masked, flags=re.DOTALL)
    # Línea // ... (Solo para JS)
    if file_ext == 'js':
        masked = re.sub(r'(?<!:)//.*', '', masked) # (?<!:) evita romper http:// fuera de strings (aunque ya no debería haber)

    # 3. LIMPIEZA DE ESPACIOS (Segura)
    # Reemplazar todos los saltos de línea y tabs por UN espacio
    masked = re.sub(r'\s+', ' ', masked)

    # 4. MINIFICACIÓN AGRESIVA (Solo alrededor de operadores)
    # Eliminar espacios alrededor de: { } ( ) [ ] ; : , = ! < > ? & |
    # Esto reduce: "function ( ) {" -> "function(){"
    operators = r'([{};,:!=\+\-\*\/\%&\|\(\)\[\]<>?])'
    masked = re.sub(r'\s*' + operators + r'\s*', r'\1', masked)

    # 5. RESTAURAR STRINGS
    final_content = restore_strings(masked, strings)
    
    return final_content.strip()

def process_file(file_path):
    filename = os.path.basename(file_path)
    base_name, ext = os.path.splitext(filename)
    ext = ext.lower().replace('.', '')
    
    # Ignorar archivos que ya son .min
    if ".min." in filename: return

    output_path = os.path.join(os.path.dirname(file_path), f"{base_name}.min.{ext}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"⚠️ No se pudo leer {filename}: {e}")
        return

    # Procesar
    if ext in ['js', 'css']:
        try:
            minified = minify_logic(content, ext)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(minified)
            print(f"✅ Minificado OK: {filename} -> {os.path.basename(output_path)}")
        except Exception as e:
            print(f"❌ Error minificando {filename}: {e}")

def main():
    print(f"🛡️  Iniciando Minificador Seguro (Protección de Strings activada)")
    extensions = ['js', 'css']
    found_files = []

    for ext in extensions:
        pattern = os.path.join(TARGET_DIR, "**", f"*.{ext}")
        found_files.extend(glob.glob(pattern, recursive=True))

    for file_path in found_files:
        # Saltar carpetas ignoradas
        parts = file_path.split(os.sep)
        if any(ignored in parts for ignored in IGNORE_DIRS): continue
        
        process_file(file_path)

if __name__ == "__main__":
    main()