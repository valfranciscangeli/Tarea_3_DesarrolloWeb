from db import DB
import json

db = DB('localhost', 'root', '', 'tarea3')

# ========================================================================================
# creamos diccionario con comunas y cantidad de fotos (solo >0) ====================

comunas_id = db.get_comuna3()
fotos_por_comuna = dict()

for id_ in comunas_id:
    cantidad_fotos = db.get_cantidad_imagenes_por_comuna_id(id_)
    if cantidad_fotos > 0:
        fotos_por_comuna[id_] = cantidad_fotos

# ========================================================================================
# abrimos el template de la informacion de cada marcador, el total se guardara en marcadores

marcadores = ""
formato_popup = open("./templates/popup-tmp.html", mode="r", encoding="utf-8").read()
"""
        formato: 
        0: coordenada 1
        1: coordenada 2
        2: hover title
        3: popup title
        4: popup body
        5: numero de popup
"""

# ========================================================================================
"""
fotos por comuna ej: {80103: 1}
"""

f = open("./js/chile2.json", mode='r', encoding="utf-8")
data = json.load(f)
"""
data ejemplo: {'name': 'Laguna Blanca', 'lng': '-71.9166667', 'lat': '-52.2500000', 'id':12345}
"""
contador = 1
for elemento in data:
    if elemento['id'] in fotos_por_comuna:
        # si llega acá es que la comuna tiene fotos, entonces creamos un popup
        marcadores += formato_popup.format(elemento['lat'],
                                           elemento['lng'],
                                           str(fotos_por_comuna[elemento['id']]) + ' foto(s) disponibles',
                                           elemento['name'],
                                           'inserte cuerpo',
                                           contador)
        contador += 1
