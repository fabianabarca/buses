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

# Información
print('Creación de un nuevo fixture\n----------------------------\nDebe elegirse un archivo modificado a la vez \ndesde una versión del feed GTFS en esta misma carpeta.')

# Versión GTFS
version = input('Elegir versión (nombre de carpeta): ')

# Nombre del archivo TXT a convertir
archivo = input('Elegir archivo (nombre sin la extensión .txt): ')

# Convertir nombre de archivo en nombre de tabla en Django
tabla = archivo[0:-1].replace('_', '') if archivo[-1] == 's' else archivo.replace('_', '')

# Directorio donde buscar el archivo
directorio = '../' + version

# Extraer contenido del archivo
contenido = []

with open(os.path.join(directorio, archivo + '.txt'), newline='') as CSV:
	lectura = csv.reader(CSV)
	for registro in lectura:
		contenido.append(registro)

# Separar nombres de los campos de los valores
nombres = contenido[0]
valores = contenido[1:None]

# Identificar el primary_key (pk) y suprimir el '_id' excepto para el pk
id_pos = -1
for i, n in enumerate(nombres):
	if n[-3:None] == '_id':
		# En el caso especial de shapes que "no tiene" id
		if tabla == 'shape' and n == 'shape_id':
			continue
		# Cuando el id tiene el nombre tabla_id
		if n == (tabla + '_id'):
			id_pos = i
			continue
		# En los casos especiales de que el id no tiene el nombre de la tabla
		if (tabla == 'calendar' and n == 'service_id') or (tabla == 'fareattribute' and n == 'fare_id'):
			id_pos = i
			continue
		else:
			nombres[i] = nombres[i].replace('_id', '')

# Número de campos (columnas) y registros (filas)
campos = len(nombres)
registros = len(valores)

# Aplicación en la que se van a importar los datos
app = 'rutas'

# Crear y escribir en un archivo JSON
with open(tabla + '.json', 'w') as JSON:
	
	# Crear los objetos JSON y añadirlos
	JSON.write('[\n')

	# Llenar los valores de los campos en cada registro
	for i in range(registros):
		# Crear los "fields" como un diccionario
		fields = {}
		
		# Revisar los campos para identificar el pk y cambiar nombres para eliminar el 'tabla_'
		for j in range(campos):
			
			# Revisar si no es el pk
			if j != id_pos:
				# Suprimir el 'tabla_' menos en casos especiales
				if nombres[j] != 'route_type' and nombres[j] != 'shape_id':
					nombres[j] = nombres[j].replace(tabla + '_', '')
				if nombres[j][0:4] == 'feed':
					nombres[j] = nombres[j].replace('feed' + '_', '')
				
				# Guardar los valores de "fields" en el JSON
				if nombres[j][-4:None] == 'date':
					fields[nombres[j]] = datetime.strptime(valores[i][j], '%Y%m%d').strftime('%Y-%m-%d')
				else:
					fields[nombres[j]] = valores[i][j]

		# Asignación del valor de "pk" en el JSON
		if id_pos == -1:
			pk = i + 1
		else:
			pk = valores[i][id_pos]

		objeto = json.dumps({
						'model': app + '.' + tabla,
				  		'pk': pk,
				  		'fields': fields
				  	}, indent=4)

		# Escribir cada objeto JSON en el archivo
		JSON.write(objeto)
		if i != registros - 1:
			JSON.write(',\n')
		else:
			JSON.write('\n')

	JSON.write(']')

print('El archivo {} de la versión {} de GTFS estará en la misma carpeta de este programa.'.format(tabla + '.json', version))