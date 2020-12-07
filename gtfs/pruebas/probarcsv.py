import os
import csv

ubicaciones = [a for a in os.listdir('gtfs/')]

nombres = []
for u in ubicaciones:
	nombres.append(u[0:-4])

print(nombres)

archivos = []

# Leer cada archivo y crear lista
for u in ubicaciones:
	with open('gtfs/' + u, newline='') as CSV:
		contenido = []
		lectura = csv.reader(CSV)
		for registro in lectura:
			contenido.append(registro)

	archivos.append(contenido)

print(archivos[0][0])
print(len(archivos[0][0]))