import sys
import os
from collections import Counter
import matplotlib.pyplot as plt

def analiza_texto(nombre_fichero, palabra_clave):
    if not os.path.isfile(nombre_fichero):
        print(f"Error: El archivo '{nombre_fichero}' no existe.")
        return

    if not palabra_clave:
        print("Error: La palabra clave no puede estar vacía.")
        return

    try:
        with open(nombre_fichero, "r", encoding='utf-8') as fichero:
            linias = fichero.readlines()
    except Exception as e:
        print(f"Error en leer el archivo: {e}")
        return

    texto_completo = ' '.join(linias)
    palabras = texto_completo.split()
    total_palabras = len(palabras)
    total_lineas = len(linias)
    veces_palabra = sum(1 for palabra in palabras if palabra.lower() == palabra_clave.lower())

    contador_palabras = Counter(palabras)
    palabras_mas_frecuentes = contador_palabras.most_common(10)

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

    # Se genera el grafico
    try:
        palabras, frequencias = zip(*palabras_mas_frecuentes)
        plt.figure(figsize=(8,5))
        plt.bar(palabras, frequencias, color='skyblue')
        plt.xlabel('Palabras')
        plt.ylabel('Frequencia')
        plt.title('Las 10 palabras más frequentes')
        plt.savefig('freq_grafico.png')
        print("Gràfico generado como 'freq_grafico.png'")
    except Exception as e:
        print(f"Error en generar el gràfico: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso correcto: python script.py <nombre fichero.txt> <palabra_clave>")
    else:
        analiza_texto(sys.argv[1], sys.argv[2])
