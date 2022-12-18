# Ejercicios de Python

""""
Escribe un programa que muestre por consola (con un print)  los numeros de 1 a 100
(ambos incluidos y con un salto de linea entre cada impresion), sustituyendo los siguientes:
    Multiplos de 3 por la palabra "fizz"
    Multiplos de 5 por la palabra "buzz"
    Multiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"
"""""


def fizzbuzz():
    # Mostraremos por consola numeros del 1 al 100, iteraremos 100 veces un elemento
    for index in range(1, 101):
        # Una vez imprimidos los numeros, cambiar y hacer condiciones...
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:  # Caso por defecto
            print(index)


fizzbuzz()

""""
Escribe una funcion que reciba dos palabras y retorne un verdadero o falso segun sean o no anagramas
    Un anagrama consiste en formar una palabra reordenando todas las letras de otra palabra incial
    no hace falta comprobar que ambas palabras existan
    dos palabras exactamente iguales no son anagramas
"""""


# Funcion que detecta si es anagrama (habria que ordenar las letras y comparar)
def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    # sorter ordena en base a un criterio fijo (ambas palabras de la misma forma)
    # La pasamos a minuscula y la ordenaremos y compararemos
    return sorted(word_one.lower()) == sorted(word_two.lower())


print(is_anagram("amor", "roma"))

"""""
Escribe un programa que imprima los primeros 50 numeros de la sicsion de Fibonacci empezando en 0
    La series de Fibonacci se compone por una sicesion de numeros en la que la siguiente siempre es la sima de os dos
    anteriores.
"""""


def fibonacci():
    prev = 0
    next = 1
    # El siguiente numero siempre es la suma de los dos anteriores
    for index in range(1, 50):
        print(prev)
        # Cada numero se calcula en base a la suma de los dos anteriores
        fib = prev + next
        prev = next
        next = fib


fibonacci()

"""""
Escribe un porgrama que se encargue de comprobar si un numero es o no primo
    Hecho esto, imprime los numeros primos entre 1 y 100
"""""


# Numero primo, para saber si es divisible entre si mismo hay que hacer el modulo
def is_prime():
    for number in range(1, 101):
        # Mayor que 1
        if number >= 2:
            is_divisible = False
            # Comprobar los divisores del numero (entre si mismo y por 1)
            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
            # Si no es divisible se imprime. ya que es primo
            if not is_divisible:
                print(number)


is_prime()

"""""
Crea un programa que invierta el orden de una cadena de texto
    Si le pasamos "hola mundo" nos tendria que devolver "odnum aloh"
"""""


# Le pasamos una cadena de texto y devolvera el reves de esta

def reverse(text):
    print(list(reversed(text)))

reverse("hola mundo")

