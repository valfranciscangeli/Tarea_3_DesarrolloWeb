
from db import DB

db = DB('localhost', 'root', '', 'tarea2')

numero = db.get_cantidad_imagenes_por_comuna_id(130606)

print(numero)

print("________________")

todas_las_comunas = db.get_comuna3()

print(todas_las_comunas)
      
      
