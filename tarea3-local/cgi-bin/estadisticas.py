# -*- coding: utf-8 -*-

import sys

from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'tarea3')

# ====================================

template = open("./templates/estadisticas-template.html", mode="r", encoding="utf-8").read()

glinea = open("./templates/grafico-linea-tmp.html", mode="r", encoding="utf-8").read()
gbarra = open("./templates/grafico-barra-tmp.html", mode="r", encoding="utf-8").read()
gtorta = open("./templates/grafico-torta-tmp.html", mode="r", encoding="utf-8").read()


print(template.format(glinea, gbarra, gtorta))
