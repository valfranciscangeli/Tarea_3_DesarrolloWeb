#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

import cgi

import json

from db import DB

# print("Content-type: text/html; charset=UTF-8")
# print()
# sys.stdout.reconfigure(encoding="utf-8")

db = DB('localhost', 'root', '', 'tarea3')

# form = cgi.FieldStorage()
# name = form.getvalue("nombreDr")
#
# if (
#     len(name) >= 2
# ):  # implementamos esto para poder buscar substrings del nombre del medico mayores a 1 caracter
#     results = db.search(name)
#     print(json.dumps(results))

print("hola mundo!")
