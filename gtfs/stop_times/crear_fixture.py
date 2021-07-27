'''
Crea un archivo JSON desde un archivo TXT de
GTFS que puede ser utilizado como "fixture"
para llenar la base de datos del app "rutas".

Dataset: archivos
Record: registro
Field: campo
Field value: valor

Referencia: https://gtfs.org/reference/static
'''

import os
import csv
import json
from datetime import datetime

# Nombre del archivo TXT a convertir
archivo = input('¿Cuál es el archivo TXT a convertir? (sin la extención .txt): ')

# Examinar los archivos presentes en el directorio
directorio = 'gtfs'
ubicaciones = [u for u in os.listdir(directorio) if u[0] != '.']

# Nombres de tablas de la base de datos (sin el '.txt')
tablas = []
for u in ubicaciones:
	tablas.append(u[0:-4])

# Importar todos los archivos CSV y guardarlos en una variable
archivos = []
for u in ubicaciones:
	with open(os.path.join(directorio, u), newline='') as CSV:
		contenido = []
		lectura = csv.reader(CSV)
		for registro in lectura:
			contenido.append(registro)
	archivos.append(contenido)

# Aplicación en la que se van a importar los datos
app = 'rutas'

# Crear y escribir en un archivo JSON
with open(app + '.json', 'w') as JSON:

	JSON.write('[\n')
	
	id_pos = -1
	
	# Para cada archivo crear los objetos JSON y añadirlos
	for a, archivo in enumerate(archivos):

		# Separar nombres de los campos de los valores
		nombres = archivo[0]
		valores = archivo[1:None]

		# Suprimir el '_id' excepto para el primary_key
		for i, n in enumerate(nombres):
			if n[-3:None] == '_id':
				if n == tablas[a] + '_id' or (tablas[a] == 'calendar' and n == 'service_id'):
					id_pos = i
				else:
					nombres[i] = nombres[i].replace('_id', '')

		# Encontrar la columna con el primary_key (si tiene)
		# id_pos = [0 if i.find('_id') == -1 else 1 for i in nombres].index(1)

		# Número de campos (columnas) y registros (filas)
		campos = len(nombres)
		registros = len(valores)

		# Llenar los valores de los campos en cada registro
		for i in range(registros):
			fields = {}
			for j in range(campos):
				if j == id_pos:
					continue
				if nombres[j] != 'route_type':
					nombres[j] = nombres[j].replace(tablas[a] + '_', '')
				if nombres[j][-4:None] == 'date':
					fields[nombres[j]] = datetime.strptime(valores[i][j], '%Y%m%d').strftime('%Y-%m-%d')
				else:
					fields[nombres[j]] = valores[i][j]

			if id_pos == -1:
				pk = i + 1
			else:
				pk = valores[i][id_pos]

			objeto = json.dumps({
							'model': app + '.' + tablas[a],
					  		'pk': pk,
					  		'fields': fields
					  	}, indent=4)

			# Escribir cada objeto JSON en el archivo
			JSON.write(objeto)
			if i != registros - 1:
				JSON.write(',\n')
			else:
				JSON.write('\n')

		id_pos = -1

	JSON.write(']')
