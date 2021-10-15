import pandas as pd
import collections
import csv
import json
import time
from django.core import serializers

def HandleShapes(shapes_table):
    serializedFields=('shape_id', 'pt_lat', 'pt_lon', 'pt_alt', 'dist_traveled')
    renamingColumns={'fields.shape_id': 'shape_id','fields.pt_lat': 'shape_pt_lat',
                    'fields.pt_lon': 'shape_pt_lon', 'fields.pt_alt': 'shape_pt_alt',
                    'fields.dist_traveled': 'shape_dist_traveled'}
    serializerShapes = serializers.serialize('json', shapes_table, fields=serializedFields)
    shape_json=json.loads(serializerShapes)
    shape_df=pd.json_normalize(shape_json)
    shape_df=shape_df.drop(columns=['model', 'pk'])
    shape_df = shape_df.rename(columns=renamingColumns)
    jsonObj=shape_df.to_json(orient='records')
    return jsonObj

def HandleRoutes(routes_table):
    serializedFields = ('short_name', 'color')
    renamingColumns = {'pk': 'route_id', 'fields.short_name':'route_short_name',
                       'fields.color': 'route_color'}
    serializerRoutes = serializers.serialize('json', routes_table, fields=serializedFields)
    route_json=json.loads(serializerRoutes)
    route_df=pd.json_normalize(route_json)
    route_df=route_df.drop(columns=['model'])
    route_df = route_df.rename(columns=renamingColumns)
    jsonObj=route_df.to_json(orient='columns')
    json_dict=json.loads(jsonObj)
    new_json_dict={}
    for key in json_dict:
        new_json_dict[key]=list(json_dict[key].values())
    new_jsonObj=json.dumps(new_json_dict)
    return new_jsonObj

def HandleTrips(trips_table):
    serializedFields=('route', 'shape', 'headsign')
    renamingColumns={'fields.route': 'route_id','fields.shape': 'shape_id',
                    'fields.headsign': 'trip_headsign'}
    serializerTrips = serializers.serialize('json', trips_table, fields=serializedFields)
    trip_json=json.loads(serializerTrips)
    trip_df=pd.json_normalize(trip_json)
    trip_df=trip_df.drop(columns=['model', 'pk'])
    trip_df = trip_df.rename(columns=renamingColumns)
    jsonObj=trip_df.to_json(orient='columns')
    json_dict=json.loads(jsonObj)

    new_json_dict={'route_shape_id_relation':{}, 'headsign_shape_id_relation':{}}
    for key in json_dict['route_id'].keys():
        route_id = json_dict['route_id'][key]
        shape_id = json_dict['shape_id'][key]
        trip_headsign = json_dict['trip_headsign'][key]
        if route_id not in new_json_dict['route_shape_id_relation'].keys():
            new_json_dict['route_shape_id_relation'][route_id]=[shape_id]
        elif ((route_id in new_json_dict['route_shape_id_relation']) and (shape_id not in new_json_dict['route_shape_id_relation'][route_id])):
            new_json_dict['route_shape_id_relation'][route_id].append(shape_id)

        if shape_id not in new_json_dict['headsign_shape_id_relation'].keys():
            new_json_dict['headsign_shape_id_relation'][shape_id]=trip_headsign
    new_jsonObj=json.dumps(new_json_dict)
    return new_jsonObj

def HandleStops(stops_table):
    serializedFields = ('lat', 'lon', 'name')
    renamingColumns = {'pk': 'stop_id', 'fields.lat':'stop_lat',
                       'fields.lon': 'stop_lon', 'fields.name': 'stop_name'}
    serializerStops = serializers.serialize('json', stops_table, fields=serializedFields)
    stop_json=json.loads(serializerStops)
    stop_df=pd.json_normalize(stop_json)
    stop_df=stop_df.drop(columns=['model'])
    stop_df = stop_df.rename(columns=renamingColumns)
    jsonObj=stop_df.to_json(orient='columns')
    json_dict=json.loads(jsonObj)
    new_json_dict={}
    for key in json_dict:
        new_json_dict[key]=list(json_dict[key].values())
    new_jsonObj=json.dumps(new_json_dict)
    return new_jsonObj

def HandleLabelsConfig(labelsConfig_table):
    serializedLabels=('shape_id', 'towns')
    serializerLabels = serializers.serialize('json', labelsConfig_table, fields=serializedLabels)
    labels_json=json.loads(serializerLabels)
    labels_json_ordered = {'shape_id':{}}
    for dict in labels_json:
        for item in dict['fields']:
            if item == 'shape_id':
                shape_id=dict['fields']['shape_id']
                labels_json_ordered['shape_id'].update({dict['fields']['shape_id']:{}})
            if item == 'towns':
                labels_json_ordered['shape_id'][shape_id].update(dict['fields']['towns'])
    jsonObj=json.dumps(labels_json_ordered)
    return jsonObj
