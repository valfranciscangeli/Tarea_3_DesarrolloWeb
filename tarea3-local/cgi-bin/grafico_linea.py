#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

import cgi

import sys
import cgi
import json
import datetime

from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding="utf-8")

db = DB('localhost', 'root', '', 'tarea3')

"""
el grafico de linea es fecha vs cantidad de actividades
"""

data = db.get_actividades_por_dia()

# procesamos la data para separar en orden cantidad y fecha

datosY = list()
datosX = list()

for elemento in data:
    fecha = elemento[1]
    dia = fecha.day
    mes = fecha.month
    anho = fecha.year
    fecha = f"{anho}-{mes}-{dia}"
    cantidad = elemento[0]
    datosY.append(cantidad)
    datosX.append(fecha)

data_set = [{"fechas": datosX, "cantidades": datosY}]

print(json.dumps(data_set))
