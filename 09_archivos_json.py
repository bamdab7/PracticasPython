# Archivos jsons
import json

base_de_datos = []

for i in range(3):
    persona = {}
    edad = input("Ingrese la edad: ")
    nombre = input("Ingrese el nombre: ")
    persona["nombre"] = nombre
    persona["edad"] = edad
    base_de_datos.append(persona)

print(base_de_datos)

with open("base_de_datos.json", "w") as archivo:  # Escribir ese archivo, si no existe lo crea (w)
    json.dump(base_de_datos, archivo, indent=4)  # Guardaremos la info en nuestro archivo json
    print("Archivo exportado")


# Leeremos un archivo que esta generado
with open("base_de_datos.json", "r") as archivo:  # Lectura del archivo
    base_de_datos = json.load(archivo)
    print("Archivo leido con exito")
print(base_de_datos)
