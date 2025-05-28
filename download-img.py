import urllib.request
import os

# Nombre del archivo que contiene la lista de URLs
urls_file = "lista_urls.txt"

# Crea una carpeta para guardar las imágenes descargadas
if not os.path.exists("imagenes"):
    os.makedirs("imagenes")

# Inicializa el contador en 1
counter = 1

# Abre el archivo en modo lectura
with open(urls_file, "r") as f:
    # Lee cada línea del archivo
    for line in f:
        # Elimina el caracter de nueva línea al final de cada línea
        line = line.strip()

        # Si la línea no está vacía
        if line:
            image_file_name = f"imagen_{counter}.jpg"
            image_path = os.path.join("imagenes", image_file_name)

            try:
                # Muestra mensaje de progreso
                print(f"[{counter}] Descargando: {line}")
                
                # Descarga la imagen
                urllib.request.urlretrieve(line, image_path)

                print(f"    ✔ Guardada como {image_path}")
            except Exception as e:
                print(f"    ❌ Error al descargar {line}: {e}")

            # Incrementa el contador
            counter += 1
