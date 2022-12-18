mi_lista = ["hola", "como", "estas"]  # Corchetes
print(mi_lista[2])

persona = {  # Llaves / clave -> valor
    "nombre": "luis",
    "edad": 25,
    "altura": 1.75,
    "notas": [60, 70, 80, 90]  # Definimos una lista dentro del diccionario
}
print(persona['nombre'])
print(persona['edad'])
print(persona['altura'])
print(persona["notas"][2])  # Asi accederemos al segundo elemento de la lista

# Lista que almacene diccionarios

lista_personas = [
    {
        "nombre": "luis",
        "edad": 25,
        "altura": 1.75,
    },
    {
        "nombre": "pedro",
        "edad": 22,
        "altura": 1.40,
    }
]
print(lista_personas[1])  # Imprime el elemento 1 de la lista
print(lista_personas[1]["edad"])  # Imprime la edad del element 1

# Para recorrer los elementos de una lista
mi_lista = ["a", "b", "c"]
for elemento in mi_lista:
    print(elemento)

# Para leer la lista de personas...
for persona in lista_personas:
    print(persona)
# Imprimir todas las edades
for persona in lista_personas:
    print("Año de nacimiento: ", 2022 - persona["edad"])

# Tenemos una 'base de datos' donde guardaremos la informacion
base_de_datos = []

for i in range(3):  # Para que se repita 3 veces
    persona = {}  # Definimos un diccionario vacio
    edad = input("Ingrese la edad: ")
    nombre = input("Ingrese el nombre: ")
    persona["nombre"] = nombre
    persona["edad"] = edad
    base_de_datos.append(persona)  # Para meter lo que queramos
    
print(base_de_datos)
