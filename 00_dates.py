#FECHAS

from datetime import datetime
fecha = datetime.now()
print("El dia de hoy es", fecha.day, "del mes", fecha.month, "del año", fecha.year)

# Representacion unica de un tiempo ( poder recuperar una fecha etc, sin tener que hacer un objeto completo)
timestamp = fecha.timestamp()
print(timestamp)

