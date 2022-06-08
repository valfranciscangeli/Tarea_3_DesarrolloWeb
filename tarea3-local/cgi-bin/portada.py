#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

import cgi

import sys
import detalles
import creador_popups

from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'tarea3')

"""
-- seleccionar ultimas 5 actividades agregadas, con nombre de comuna y nombre de tema:

(id actividad,
comuna, 
sector,
nombre organizador,
email,
celular,
hora inicio,
hora termino,
descripción, 
tema, 
)
SELECT AC.id, CO.nombre, AC.sector, AC.nombre, AC.email, AC.celular, AC.dia_hora_inicio, AC.dia_hora_termino, AC.descripcion, TE.nombre FROM actividad AC, comuna CO, tema TE WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id ORDER BY id DESC LIMIT 5
"""

data = db.get_data_portada()  # retorna una lista de tuplas formato (nombre, experiencia, especialidad, email, celular, path)

tabla = ""

header_tabla = """
             <div class="w3-container">
        <hr>
        <div class="w3-center">
            <h2>Actividades recientemente agregadas</h2>
        </div> <br>
        <div class="w3-responsive w3-card-4">
            <table class="w3-table w3-striped w3-bordered">
                <thead>
                    <tr class="w3-theme">
                        <th>Inicio</th>
                        <th>Término</th>
                        <th>Comuna</th>
                        <th>Sector</th>
                        <th>Tema</th>
                        <th>Foto</th>
                    </tr>
                </thead>
                <tbody>
        """

tabla += header_tabla

fila_tabla = open("./templates/fila-tabla-portada.html", mode="r", encoding="utf-8").read()

for p in data:
    """
    ([0] id actividad,
     [1] comuna, 
     [2] sector,
     [3] nombre organizador,
     [4] email,
     [5] celular,
     [6] hora inicio,
     [7] hora termino,
     [8] descripción, 
     [9] tema)
    """
    fecha_hora_inicio = p[6]
    fecha_hora_termino = p[7]
    comuna = p[1].title()
    sector = p[2]
    tema = p[9].title()

    fotos = db.get_fotos(p[0])  # DEVUELVE = (id, ruta_archivo, nombre_archivo, actividad_id)
    texto_alt_de_imagen = ""

    tabla += fila_tabla.format(fecha_hora_inicio, fecha_hora_termino, comuna, sector, tema, fotos[0][1],
                               texto_alt_de_imagen)

tabla += """
    </tbody>
    </table>
    </div> 
    <br>
    """


with open('./templates/header+footer_portada.html', mode='r', encoding="utf-8") as template:
    file = template.read()
    print(file.format(tabla, creador_popups.marcadores))

# ========================
detalles.crearDetalles()
# =======================
