#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

import cgi

import json

from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding="utf-8")

db = DB('localhost', 'root', '', 'tarea3')

"""
el grafico de barra es cantidad de actividades en la mañana, mediodia y tarde
"""

data = db.get_actividades_por_hora()
"""
ej: [(1, 4, 10), (1, 4, 14), (2, 4, 16), (1, 4, 17), (1, 4, 20), (1, 6, 0), (1, 6, 3)] -> cantidad, mes, hora
"""

# procesamos la data para separar en orden cantidad y fecha

manhana = list()
mediodia = list()
tarde = list()

for i in range(1, 13):  # revisamos mes a mes
    total_mes_manhana = 0
    total_mes_mediodia = 0
    total_mes_tarde = 0

    for elemento in data:
        cantidad = elemento[0]
        mes = elemento[1]
        hora = elemento[2]

        if mes == i:  # si el mes de la actividad corresponde al que estamos revisando nos fijamos en la hr y cantidad
            if hora < 11:
                total_mes_manhana += cantidad
            elif hora < 15:
                total_mes_mediodia += cantidad
            else:
                total_mes_tarde += cantidad

    # guardamos los totales del mes en su arreglo correspondiente
    manhana.append(total_mes_manhana)
    mediodia.append(total_mes_mediodia)
    tarde.append(total_mes_tarde)

data_set = [{"manhana": manhana, "mediodia": mediodia, "tarde": tarde}]

print(json.dumps(data_set))
