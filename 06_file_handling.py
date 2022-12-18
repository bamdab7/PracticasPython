# Manejo de ficheros
import os

# w+ lo va a volver a crear de 0, lo va a asobreescribir
# r+ lo que hara sera poder leer lo que tiene y poder escribir, no lo sobreescribe

# .txt file
txt_file = open("my_file.txt", "w+")  # Leer y escribir
txt_file.write("Mi nombre es Lucas\nMi apellido es Perez\nTengo 45 años\nMe encanta Java")
# print(txt_file.read())
# print(txt_file.readline())  # Lectura linea a linea
# print(txt_file.readline())

# Lectura de todas las lineas
for line in txt_file.readlines():
    print(line)

txt_file.write("\nMucho mas texto que ponemos")

# txt_file.close()
# os.remove("my_file.txt")

# .json file
import json

json_file = open("my_file.json", "w+")
# json es un estilo tipo diccionario en
json_test = {"name": "Nerea",
             "surname": "Pena",
             "age": 20,
             "languages": ["Java", "Kotlin", "Pyhton"],
             "website": "https:hola"}

json.dump(json_test, json_file, indent=4)

json_file.close()
# Es como necesario cerrar el fichero para luego poder abrirlo(?
with open("my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

#Leer el fichero y transformarlo en un diccionario, recuperar los valores
json_dict = json.load(open("my_file.json"))
print(json_dict)
print(type(json_dict))

#Me permite acceder a valores concretos
print(json_dict["name"])
print(json_dict["languages"])