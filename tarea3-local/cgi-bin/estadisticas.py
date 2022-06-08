#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

import cgi

from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'tarea3')

# ====================================

template = open("./templates/estadisticas-template.html", mode="r", encoding="utf-8").read()

"""
canvas id's:  linea,  barra, torta
"""

print(template)
