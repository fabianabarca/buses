'''


IMPORTANTE: es necesaria la coincidencia
entre los campos en los archivos y los
campos en el modelo de Django (y no hay
verificación aquí).
'''

import os
import shutil

# ----
# Cambiar los nombres para que coincidan con el modelo de Django
# ----

directorio = 'GTFS_TSG'
txts = [a for a in os.listdir(directorio)]
csvs = []

for t in txts:
	aux = t.replace('s.', '.')
	aux = aux.replace('.txt', '')
	aux = aux.replace('_', '')
	csvs.append(aux)

# ----
# Copiar y cambiar nombre a archivos TXT
# ----

# Crear nuevo directorio
os.mkdir('gtfs')

for i, txt in enumerate(txts):
	shutil.copyfile(
			os.path.join(directorio + '_txt', txt),
			os.path.join(directorio, csvs[i] + '.csv')
		)

# ----
# Filtrar los campos que sí están en Django
# ----

