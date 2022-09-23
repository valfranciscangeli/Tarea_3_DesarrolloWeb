#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

import cgi

from db import DB
import math

print("Content-type: text/html; charset=UTF-8")
print()

sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'cc500279_u', 'llainInhac', 'cc500279_db')

try:
    form = cgi.FieldStorage()
    pagina = form.getvalue("page")
    pagina = int(pagina)

except:
    pagina = 1

# ===================================================================================

total_actividades = int(db.contar_actividades()[0][0])  # cuenta el total de actividades registradas

cantidadBotones = math.ceil(total_actividades / 5)


def generarBotones(total, actual):
    if actual == 1:
        prev = 1
    else:
        prev = actual - 1

    if actual == total:
        sig = total
    else:
        sig = actual + 1

    left = f"<a href='./listado.py?page={prev}' class='w3-bar-item w3-button w3-hover-theme'>«</a>"
    right = f"<a href='./listado.py?page={sig}' class='w3-bar-item w3-button w3-hover-theme'>»</a>"
    selected = f"<input type='submit' value='{actual}' class='w3-bar-item w3-button w3-theme w3-hover-theme'>"
    otro = "<input type='submit' value='{0}' name='page' class='w3-bar-item w3-button w3-hover-theme'>"
    result = left

    for i in range(total):
        if i + 1 == actual:
            result += selected
        else:
            result += otro.format(i + 1)

    return result + right


botones = generarBotones(cantidadBotones, pagina)


# ===================================================================================

def getFilas(offset):
    data = db.get_data_listado(offset)  # retorna las tuplas en un rango
    return data


def prepareRows(offset):
    filas = ''
    alldatos = getFilas(offset)
    for i in range(len(alldatos)):
        datos = alldatos[i]
        #  datos:
        #         (120, 'Padre Hurtado', 'Estadio Comunal', 'Dante Torobolino', 'dante@juegostorobolino.cl', '+56955555555', datetime.datetime(2022, 4, 13, 13, 0), datetime.datetime(2022, 4, 13, 19, 0), 'juegos de ayer y hoy', 'juegos') 

        filas += f'''
            <tr class="w3-white" onclick="window.open('../actividad{datos[0]}.html')">
                <td>{datos[6]}</td>
                <td>{datos[7]}</td>
                <td>{datos[1].title()}</td>
                <td>{datos[2]}</td>
                <td>{datos[9].title()}</td>
                <td>{datos[3].title()}</td>
                <td>{db.contar_fotos(int(datos[0]))} foto(s) cargada(s)</td>
            </tr>
                '''
        
    return filas


# ===================================================================================

head = '''
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">

            <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
            <link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-blue-grey.css">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.3.0/css/font-awesome.min.css">

            <title>HobbyApp - Listado de actividades</title>
            <link rel="icon" href="../img/icono-nf2.ico" type="image/icon"> <!-- icono-->

        </head>

        '''

header = '''
        <!--- links -->
            <div class="w3-bar w3-theme-light">
                <a href="./portada.py" class="w3-bar-item w3-button w3-padding-16">Inicio</a>
                <a href="./formulario.py" class="w3-bar-item w3-button w3-padding-16">Informar actividad</a>
                <a href="#" class="w3-bar-item w3-button w3-padding-16">Ver listado de Actividades</a>
                <a href="../estadisticas.html" class="w3-bar-item w3-button w3-padding-16">Estadísticas</a>
            </div>


            <!-- Header -->
            <header class="w3-container w3-theme w3-padding" id="myHeader">
                <div class="w3-center">
                    <h1 class="w3-xxxlarge w3-animate-bottom">HobbyApp</h1>
                    <h4>Bienvenide a HobbyApp! Aquí puedes encontrar entretenidas actividades para conectarte con tu comunidad y
                        crear nuevas amistades</h4>
                </div>
            </header>
        '''

paginador = f'''
            <form action="listado.py" method="get">
                {botones}
            </form>
            '''

footer = '''
       <!-- Footer -->
    <footer class="w3-container w3-theme-dark w3-padding-16">
        <h3>HobbyApp - 2022</h3>
        <p>Plantillas de <a href="https://www.w3schools.com/w3css/default.asp" target="_blank">w3.css</a></p>
        <a href="../cgi-bin/portada.py" class='w3-bar-item w3-button w3-theme w3-hover-theme' style="text-align: center;">Home</a>
        <div style="position:relative;bottom:55px;" class="w3-tooltip w3-right">
            <span class="w3-text w3-theme-light w3-padding">Go To Top</span> 
            <a class="w3-text-white" href="#myHeader"><span class="w3-xlarge">
                    <i class="fa fa-chevron-circle-up"></i></span></a>
        </div>
    </footer>
        '''

body = f'''
        <body>
                {header}

        <!---#####################################################################-->
        <div class="w3-container">
            <hr>
            <div class="w3-center">
                <h2>Actividades recientemente agregadas</h2>
            </div>
            <div class="w3-responsive w3-card-4">
                <table class="w3-table w3-striped w3-bordered">
                    <thead>
                        <tr class="w3-theme">
                            <th>Inicio</th>
                            <th>Término</th>
                            <th>Comuna</th>
                            <th>Sector</th>
                            <th>Tema</th>
                            <th>Nombre organizador</th>
                            <th>Total fotos</th>
                        </tr>
                    </thead>
                    <tbody>
                        {prepareRows((pagina - 1)*5)}
                    </tbody>
                </table>
            </div> <br> <br>
        </div>
        <!---#####################################################################-->
        <div class="w3-center w3-padding-32">
                {paginador}
        </div>
        <!---#####################################################################-->
                {footer}
        </body>

        </html>
        '''

print(head + body)

# ============================================================================
