import json

from db import DB

db = DB('localhost', 'root', '', 'tarea3')

numero = db.get_cantidad_imagenes_por_comuna_id(130606)

print(numero)

print("________________")

todas_las_comunas = db.get_comuna3()

print(todas_las_comunas)

print("________________")

santiago_id = db.get_comuna_por_nombre("santiago")

print(santiago_id)

print("________________")

actividades_santiago = db.get_id_actividades_comuna(130603)

print(actividades_santiago)

print("________________")
actividad_info = db.get_info_actividad_mapa(1)[0]

print(actividad_info)

tabla = open("../templates/map-list-tmp.html", mode='r', encoding='utf-8').read()


def crearInfoMapa(id_actividad):
    info = db.get_info_actividad_mapa(id_actividad)[0]
    print(type(info[2]))
    return tabla.format(info[0], info[1], info[2], "", "")


print(crearInfoMapa(1))

print("________________")

data = db.get_actividades_por_dia()
print(data)

data = json.dumps(data)

print(data)