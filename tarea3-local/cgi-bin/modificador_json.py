#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

import cgi

from db import DB
import json

db = DB('localhost', 'root', '', 'tarea3')

# abrimos archivo json que contiene las comunas y sus coordenadas
"""
ejemplo: {'name': 'Laguna Blanca', 'lng': '-71.9166667', 'lat': '-52.2500000'}
"""

f = open("../js/chile.json", mode='r', encoding="utf-8")
data = json.load(f)
f2 = open("../js/chile2.json", mode='w+', encoding="utf-8")
f2.write('[')

for comuna in data:
    print(comuna)
    identificador = db.get_comuna_por_nombre(comuna['name'].title())
    comuna['id'] = identificador
    # print(comuna)
    f2.write(str(comuna) + ', \n')

f2.write(']')
