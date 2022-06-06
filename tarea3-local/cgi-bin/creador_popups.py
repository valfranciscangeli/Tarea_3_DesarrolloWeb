
from db import DB

db = DB('localhost', 'root', '', 'tarea2')

# ============================================

marcadores = ""

comunas_id = db.get_comuna3()
fotos_por_comuna = dict()

for id in comunas_id:
    cantidad_fotos = db.get_cantidad_imagenes_por_comuna_id(id)
    if cantidad_fotos>0:
        fotos_por_comuna[id] = cantidad_fotos
    
print(fotos_por_comuna)