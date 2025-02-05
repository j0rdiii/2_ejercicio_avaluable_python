import sys
import os
from collections import Counter
import matplotlib.pyplot as plt

# Función que analiza un archivo de texto en busca de una palabra clave
def analiza_texto(nombre_fichero, palabra_clave):
    # Verifica si el archivo existe
    if not os.path.isfile(nombre_fichero):
        print(f"Error: El archivo '{nombre_fichero}' no existe.")
        return

    # Verifica si la palabra clave no está vacía
    if not palabra_clave:
        print("Error: La palabra clave no puede estar vacía.")
        return

    # Intenta leer el archivo
    try:
        with open(nombre_fichero, "r", encoding='utf-8') as fichero:
            linias = fichero.readlines() # Lee todas las líneas del archivo
    except Exception as e:
        print(f"Error en leer el archivo: {e}")
        return

    # Une las líneas en un solo texto y separa en palabras
    texto_completo = ' '.join(linias)
    palabras = texto_completo.split()
    total_palabras = len(palabras) # Cuenta el total de palabras en el texto
    total_lineas = len(linias)

    # Cuantas veces aparece la palabra clave en el texto (sin distinción de mayúsculas y minúsculas)
    veces_palabra = sum(1 for palabra in palabras if palabra.lower() == palabra_clave.lower())

    # Cuenta la frecuencia de todas las palabras y obtiene las 10 más frecuentes
    contador_palabras = Counter(palabras)
    palabras_mas_frecuentes = contador_palabras.most_common(10)

    # Intenta escribir un resumen en un archivo de salida
    try:
        with(open('resumen.txt', 'w', encoding='utf-8')) as fichero_resumen:
            fichero_resumen.write(f"Nombre total de palabras: {total_palabras}\n")
            fichero_resumen.write(f"Nombre de líneas: {total_lineas}\n")
            fichero_resumen.write(f"Veces de la palabra: '{palabra_clave}': {veces_palabra}\n")
            fichero_resumen.write(f"Las 10 palabras más frequentes\n")
            for palabra, freq in palabras_mas_frecuentes:
                fichero_resumen.write(f"{palabra}: {freq}\n")
        print("Resumen generado correctamente a 'resumen.txt'")
    except Exception as e:
        print(f"Error en escribir el archivo: {e}")

    # Se genera el grafico con las palabras más frecuentes
    try:
        palabras, frequencias = zip(*palabras_mas_frecuentes) # Desempaqueta las palabras
        plt.figure(figsize=(8,5)) # Configura el tamaño del gráfico
        plt.bar(palabras, frequencias, color='skyblue') # Crea un gráfico de barras
        plt.xlabel('Palabras')
        plt.ylabel('Frequencia')
        plt.title('Las 10 palabras más frequentes')
        plt.savefig('freq_grafico.png')
        print("Gràfico generado como 'freq_grafico.png'") # Guarda el gráfico como imagen
    except Exception as e:
        print(f"Error en generar el gràfico: {e}")

# Verifica si el script se ejecuta con los argumentos correctos
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso correcto: python script.py <nombre fichero.txt> <palabra_clave>")
    else:
        analiza_texto(sys.argv[1], sys.argv[2])
