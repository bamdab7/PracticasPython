# Creacion de listas comprimidas de manera rapida

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print("Lista original declarada:", my_original_list)

# Guardamos el rango en una variable
my_range = range(8)
print(list(my_range))

# Al fin y al cabo es un iterador (el valor se modifica antes de guardarlo)

my_list = [i + 1 for i in range(8)]
# Pasa por cada uno de los elementos que guarda y le suma 1 antes de añadirlo a la lista
print("Lista +1:", my_list)

my_list2 = [i * 2 for i in range(8)]
# Pasa por cada uno de los elementos que guarda y le multiplica 2 antes de añadirlo a la lista
print("Lista *2:", my_list2)

my_list3 = [i * i for i in range(8)]  # Multiplica cada numero por su mismo numero
print("Lista multiplica si mismo:", my_list3)


# A las listas le podemos pasar funciones tambien para poder modificarlas
def sum_five(number):
    return number + 5


my_list4 = [sum_five(i) for i in range(8)]
print("Lista con funcion +5:", my_list4)
