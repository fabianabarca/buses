# TCU tropicalización de la tecnología 
# Mike Mai Chen
# script que convierte datos tabulados en un archivo en formato
# JSON para la base de datos con información de las ferias del agricultor

import pandas

# leer csv y quitar todas las filas que no tenga un marketplace_url
table = pandas.read_csv("trips.csv")
table = table[table["trip_id"].notnull()]

# Cambiar nombres de columnas para hacer coincidir con los nombres de los campos
table = table.rename(columns={
    "route_id": "route",
    "service_id": "service",
    "trip_departure_time": "departure_time",
    "trip_arrival_time": "arrival_time",
    "trip_headsign": "headsign",
    "trip_short_name": "short_name",
    "direction_id": "direction",
    "shape_id": "shape",
})

# dividir el dataframe en dos, uno para los fields del JSON...
table_fields = table.drop(columns=["trip_id"])
table_fields = table_fields.transpose()

# ... y otro que contiene solo el model y el marketplace_url.
# insertar "model":"marketplaces.marketplace" para cada feria 
table.insert(0, "model", ["rutas.trip" for x in range(table.shape[0])], True)
table = table[["model", "trip_id"]]

# renombrar "marketplace_url" a "pk"
table = table.rename(columns={"trip_id": "pk"})

# unir ambos dataframe para crear uno con tres columnas: model, marketplace_url y fields
table["fields"] = [table_fields[i].to_dict() for i in range(table.shape[0])]

# exportar dataframe a JSON
table.to_json("trips_test.json", orient="records")