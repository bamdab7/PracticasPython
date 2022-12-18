# Expresiones regulares
import re

# Las expresiones regulares inspeccionan una cadena de texto


my_string = "Esta es la leccion numero 7: Leccion llamada expresiones regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de ficheros "

# MATCH
match = re.match("Esta es la leccion", my_string, re.I)
print(match)
start, end = match.span()  # Rango donde encuentra
print(my_string[start:end])  # Tupla?

match = re.match("Esta no es la leccion", my_other_string)
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

print(re.match("Expresiones regulares", my_string))  # Empieza a buscar por el principio, por tanto dice error

# SEARCH
search = re.search("leccion", my_string, re.I)  # Nos busca en cualquier sitio
print(search)
start, end = search.span()
print(my_string[start:end])

# FIND ALL
findall = re.findall("leccion", my_string, re.I)  # Listado de las veces que lo encontró y lo mete en un array
print(findall)

# SPLIT
split = re.split(":", my_string)  # Nos separa en funcion de lo que nosotros le indiquemos
print(split)

# SUB
sub = re.sub("[L|l]eccion", "LECCION", my_string)  # Sustituye expresiones
print(sub)

# PATRONES
pattern = r"[l|L]eccion"  # Asi se crea el patron
print(re.findall(pattern, my_string))

pattern = r"[l|L]eccion | expresiones"
print(re.findall(pattern, my_string))

pattern = r"[a-z]"
print(re.findall(pattern, my_string))  # Todas las letras que coinciden de la a a la z

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"  # Caracteres numericos
print(re.findall(pattern, my_string))
pattern = r"\D"  # Caracteres no numericos
print(re.findall(pattern, my_string))

pattern = r"[l]."
print(re.findall(pattern, my_string))  # Busca la palabra y justo lo siguiente que le sigue
pattern = r"[l].*"
print(re.findall(pattern, my_string))  # Busca la palabra y lo demas que le sigue hacia delante

email = "nereapena42@gmail.com"
pattern = r"^[a-zA-Z0-9_.*-]+@[a-zA-z0-9-]+\.[a-zA-z0-9-.]+$"  # EMAIL
print(re.match(pattern, email))
print(re.findall(pattern, email))
