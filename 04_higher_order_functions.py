# Practica con funciones de orden superior (funciones que son capaces de ejecutar otras funciones)

def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


# LA funcion fue capaz de recibir una funcion que nososotros quisieramos, llamando a sum
def sum_two_values_and_add1(first_value, second_value, f):
    return f(first_value + second_value)


print(sum_two_values_and_add1(1, 8, sum_one))
print(sum_two_values_and_add1(1, 8, sum_five))


# Closures (funcion que define una funcion y devuelve una funcion)

def sum_ten():
    # Funcion con otra funcion dentro que hace algo
    def add(value):
        return value + 10

    return add  # La posibilidad de poder devolver una funcion (funcion que retorna otra funcion)


add_closure = sum_ten()  # Esto devolvera una funcion
print(add_closure(5))
