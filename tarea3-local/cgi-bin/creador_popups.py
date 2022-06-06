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

tabla = open("./templates/map-list-tmp.html", mode='r', encoding='utf-8').read()

def crearInfoMapa(id_actividad):
    info = db.get_info_actividad_mapa(id_actividad)[0]
    tema= info[0].title()
    inicio= info[1]
    sector = info[2].title().replace('"', "'")
    fotos = db.get_fotos(id_actividad)
    foto = ""
    for imagen in fotos:
        foto+=f"<img src='../media/{imagen[1]}' style='width: 90%'><br><br>"

    ver_mas = f"<a href='../actividad{id_actividad}.html'> + info</a>"
    return tabla.format(tema, inicio, sector, foto, ver_mas)


contador = 1
for elemento in data:
    if elemento['id'] in fotos_por_comuna:
        #creamos el cuerpo con la info
        # cuerpo="""
        #         <table>
        #         <tr>
        #         <th>Tema</th>
        #         <th>Inicio</th>
        #         <th>Sector</th>
        #         <th>Fotos</th>
        #         <th>Ver más</th>
        #         </tr>
        # """
        cuerpo = ""
        actividades_en_comuna = db.get_id_actividades_comuna(elemento['id'])
        for actividad in actividades_en_comuna:
             identificador = actividad[0]
             cuerpo += crearInfoMapa(identificador)

        # cuerpo += "</table>"

        # si llega acá es que la comuna tiene fotos, entonces creamos un popup
        marcadores += formato_popup.format(elemento['lat'],
                                           elemento['lng'],
                                           str(fotos_por_comuna[elemento['id']]) + ' foto(s) disponibles',
                                           elemento['name'],
                                           cuerpo,
                                           contador)
        contador += 1

print(marcadores)