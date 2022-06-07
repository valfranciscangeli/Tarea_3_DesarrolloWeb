import sys
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

data= db.get_actividades_por_hora()
"""
ej: [(1, 4, 10), (1, 4, 14), (2, 4, 16), (1, 4, 17), (1, 4, 20), (1, 6, 0), (1, 6, 3)] -> cantidad, mes, hora
"""

# procesamos la data para separar en orden cantidad y fecha

manhana = dict()
mediodia = dict()
tarde = dict()



for elemento in data:

    manhana.append( )
    mediodia.append( )
    tarde.append( )

data_set = [{"manhana": manhana, "mediodia": mediodia, "tarde": tarde}]

print(json.dumps(data_set))