import sys
import cgi
import json

from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding="utf-8")

gtorta = open("./templates/grafico-torta-tmp.html", mode="r", encoding="utf-8").read()

#print(json.dumps(gtorta))
#print(gtorta)
