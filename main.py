import csv

try:
    # Abrir el archivo CSV en modo lectura
    with open('data.csv') as File:
        # Crear un objeto lector de CSV
        reader = csv.DictReader(File)
        
        # Iterar sobre cada fila del archivo CSV
        for row in reader:
            # Imprimir los valores de las columnas "nombre" y "edad"
            print(row['nombre'], row['edad'])

except FileNotFoundError:
    print("El archivo no existe.")

except csv.Error:
    print("Error al procesar el archivo CSV.")