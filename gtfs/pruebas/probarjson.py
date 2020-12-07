import json

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'d':4, 'e':5, 'f':6}
d3 = {'g':7, 'h':8, 'i':9}

lista = [d1, d2, d3]

app = 'rutas'

coleccion = json.dumps({'San': 'José', 'd1': d1, 'd2': d2, 'd3': d3}, indent=4)
print(coleccion)

with open(app + '.json', 'w') as JSON:
	JSON.write('[\n')
	for i in lista:
		objeto = json.dumps(i, indent=4)
		JSON.write(objeto)
		JSON.write(',\n')
	JSON.write(']')