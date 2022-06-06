from db import DB
import json

db = DB('localhost', 'root', '', 'tarea3')

# ========================================================================================
# creamos diccionario con comunas y cantidad de fotos (solo >0) ====================

comunas_id = db.get_comuna3()
fotos_por_comuna = dict()

for id in comunas_id:
    cantidad_fotos = db.get_cantidad_imagenes_por_comuna_id(id)
    if cantidad_fotos > 0:
        fotos_por_comuna[id] = cantidad_fotos

# ========================================================================================
# abrimos el template de la informacion de cada marcador, el total se guardara en marcadores

marcadores = ""
formato_popup = open("../templates/popup-tmp.html", mode="r", encoding="utf-8").read()
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





