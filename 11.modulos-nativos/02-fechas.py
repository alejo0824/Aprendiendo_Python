# import time

# # time() = tiempo en segundo desde el 1 enero de 1970 en UTC (England)
# print(time.time())

from datetime import datetime

fecha = datetime(2023, 1, 1)
fecha2 = datetime(2023, 2, 1)

ahora = datetime.now()

# pagina para ver las directrices de las fechas https://docs.python.org/3/library/time.html
fechaStr = datetime.strptime("2023-01-03", "%Y-%m-%d")


print(fecha.strftime("%Y-%m-%d"))
print(fecha > fecha2)

print(
    ahora.year,
    ahora.month,
    ahora.day,
    ahora.hour,
    ahora.minute
)
