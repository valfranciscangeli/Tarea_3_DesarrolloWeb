#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

import cgi

import sys
import cgi
import json

from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding="utf-8")

#gtorta = open("./templates/grafico-torta-tmp.html", mode="r", encoding="utf-8").read()

#print(json.dumps(gtorta))
#print(gtorta)

########################

db = DB('localhost', 'root', '', 'tarea3')

"""
el grafico de torta es cantidad de actividades por tema
"""

data = db.get_actividades_por_tema()
"""
ej: [(1, 3), (1, 4), (3, 9), (1, 10), (1, 11), (1, 12)] --> cantidad, tema_id
"""
temas = db.get_temas()
"""
ej: [(8, 'baile'), (3, 'ciencias'), (9, 'comida'), (12, 'Cultural'), (2, 'deporte'), (7, 'juegos'),
 (10, 'Juegos de Mesa'), (11, 'Karaoke'), (1, 'música'), (5, 'política'),
  (4, 'religión'), (6, 'tecnología')] -> tema_id, nombre
"""

# procesamos la data para separar en orden cantidad y fecha

temas2 = list()
cantidad = list()

for elemento in data:
    numero_actividades = elemento[0]
    tema_id = elemento[1]
    for tema in temas:
        if tema_id == tema[0]:
            temas2.append(tema[1].title())
            cantidad.append(numero_actividades)

data_set = [{"temas": temas2, "cantidad": cantidad}]

print(json.dumps(data_set))

