#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

import cgi

from db import DB
import math

from detalles import *

db = DB('localhost', 'root', '', 'tarea3')


def createActividadInfo(datos, region, fotos, contactos):
    # datos:
    # (120, 'Padre Hurtado', 'Estadio Comunal', 'Dante Torobolino', 'dante@juegostorobolino.cl', '+56955555555', date.timedatetime(2022, 4, 13, 13, 0), datetime.datetime(2022, 4, 13, 19, 0), 'juegos de ayer y hoy', 'juegos')

    # fotos:
    # id, ruta_archivo, nombre_archivo, actividad_id

    actividad = datos[0]
    comuna = datos[1]
    sector = datos[2]
    organizador = datos[3]
    email = datos[4]
    celular = datos[5]
    inicio = datos[6]
    termino = datos[7]
    descripcion = datos[8]
    tema = datos[9]

    informacion = open(f"../actividad{actividad}.html", mode="w+", encoding="utf-8")

    head = """
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">

                    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
                    <link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-blue-grey.css">
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.3.0/css/font-awesome.min.css">
                    <link rel="stylesheet" href="../css/style-actividades.css">

                    <!--- lo que se ve en la pestaña del navegador -->
                    <title>HobbyApp - Últimas actividades agregadas</title>
                    <link rel="icon" href="../img/icono-nf2.ico" type="image/icon"> <!-- icono-->
                </head>
        
        """

    header = """
                    <!--- links -->
                    <div class="w3-bar w3-theme-light">
                        <a href="./cgi-bin/portada.py" class="w3-bar-item w3-button w3-padding-16">Inicio</a>
                        <a href="./cgi-bin/formulario.py" class="w3-bar-item w3-button w3-padding-16">Informar actividad</a>
                        <a href="./cgi-bin/listado.py" class="w3-bar-item w3-button w3-padding-16">Ver listado de Actividades</a>
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
        """

    footer = '''
                <!-- Footer -->
                <footer class="w3-container w3-theme-dark w3-padding-16">
                    <h3>HobbyApp - 2022</h3>
                    <p>Plantillas de <a href="https://www.w3schools.com/w3css/default.asp" target="_blank">w3.css</a></p>
                    <div style="position:relative;bottom:55px;" class="w3-tooltip w3-right">
                        <a href="./cgi-bin/portada.py" class='w3-bar-item w3-button w3-theme w3-hover-theme' style="text-align: center;">Home</a>
                        <span class="w3-text w3-theme-light w3-padding">Go To Top</span>
                        <a class="w3-text-white" href="#myHeader"><span class="w3-xlarge">
                                <i class="fa fa-chevron-circle-up"></i></span></a>
                    </div>
                </footer>
                '''

    # ruta, nombre archivo, n° de foto
    modal = '''
        <!-- ############  MODAL {2} ============================ -->

                <!-- Trigger the Modal -->
                <img id="imagen{2}" class="imagenes" src="../media/{0}" alt="{1}">

                <!-- The Modal -->
                <div id="myModal{2}" class="modal">

                    <!-- The Close Button -->
                    <span class="close{2}">&times;</span>

                    <!-- Modal Content (The Image) -->
                    <img class="modal-content" id="img0{2}" src="../media/{0}" alt="{1}">

                    <!-- Modal Caption (Image Text) -->
                    <div id="caption{2}"></div>
                </div>

                <script>
                    // ############  MODAL {2}=====================-

                    // Get the modal
                    let modal{2} = document.getElementById("myModal{2}");

                    // Get the image and insert it inside the modal - use its "alt" text as a caption
                    let img{2} = document.getElementById("imagen{2}");
                    let modalImg{2} = document.getElementById("img0{2}");
                    let captionText{2} = document.getElementById("caption{2}");
                    img{2}.onclick = function () {{
                        modal{2}.style.display = "block";
                        modalImg{2}.src = this.src;
                        captionText{2}.innerHTML = this.alt;
                    }}

                    // Get the <span> element that closes the modal
                    let span{2} = document.getElementsByClassName("close{2}")[0];

                    // When the user clicks on <span> (x), close the modal
                    span{2}.onclick = function () {{
                        modal{2}.style.display = "none";
                    }}
                </script> <br>
        '''

    imagenes = ''

    for i in range(len(fotos)):
        foto = fotos[i]
        imagenes += modal.format(foto[1], foto[2], i + 1)

    # id, nombre, identificador, actividad_id     
    contacto = ''

    for i in range(len(contactos)):
        red = contactos[i]
        if "." in str(red[2]):
            contacto += f"<li>{red[1].title()}: <a href='{red[2]}'>{red[2]}</a></li>"
        else:
            contacto += f"<li>{red[1].title()}: {red[2]}</li>"

    html = f"""
                <!DOCTYPE html>
                <html lang="en">

                {head}

                <body>

                {header}
                    <div>
                        <hr>
                        <h2 class="w3-center">{tema.title()}</h2>
                    </div>
                    <div class="w3-row-padding">

                        <div class="w3-half">
                            <div class="w3-card white">
                                <div class="w3-container w3-blue-grey">
                                    <h3>Información</h3>
                                </div>
                                <div class="w3-container">
                                    <h3 class="w3-text-blue-grey">¿Dónde?</h3>
                                </div>
                                <ul class="w3-ul w3-border-top">
                                    <li>
                                        <h3>Región</h3>
                                        <p>{region.title()}</p>
                                    </li>
                                    <li>
                                        <h3>Comuna</h3>
                                        <p>{comuna.title()}</p>
                                    </li>
                                    <li>
                                        <h3>Sector</h3>
                                        <p>{sector}</p>
                                    </li>
                                </ul>

                                <div class="w3-container">
                                    <h3 class="w3-text-blue-grey">¿Cuándo y de qué trata?</h3>
                                </div>
                                <ul class="w3-ul w3-border-top">
                                    <li>
                                        <h3>Día y hora de inicio</h3>
                                        <p>{inicio}</p>
                                    </li>
                                    <li>
                                        <h3>Día y hora de término</h3>
                                        <p>{termino}</p>
                                    </li>
                                    <li>
                                        <h3>Descripción</h3>
                                        <p>{descripcion}</p>
                                    </li>

                                </ul>

                                <div class="w3-container">
                                    <h3 class="w3-text-blue-grey">¿Quién organiza?</h3>
                                </div>
                                <ul class="w3-ul w3-border-top">
                                    <li>
                                        <h3>Nombre</h3>
                                        <p>{organizador.title()}</p>
                                    </li>
                                    <li>
                                        <h3>Correo electrónico</h3>
                                        <p>{email}</p>
                                    </li>
                                    <li>
                                        <h3>Celular</h3>
                                        <p>{celular}</p>
                                    </li>
                                    <li>
                                        <h3>Contacto</h3>
                                        <ul>
                                        {contacto}
                                        </ul>
                                    </li>
                                </ul>

                                <div class="w3-container w3-blue-grey w3-large"></div>
                            </div>
                        </div>



                        <div class="w3-half">
                            <div class="w3-card white">
                                <div class="w3-container w3-blue-grey">
                                    <h3>Imágenes cargadas</h3>
                                </div> <br>
                                <div class="w3-content">

                                    <!---#######################   MODALS   ###################################-->

                                    {imagenes}

                                    <!---########################  FIN MODALS  #############################-->

                                    <div class="w3-container w3-blue-grey w3-large"></div>
                                </div>

                            </div>
                        </div>

                    </div>
                    <hr>

                    <!-- =========================================================== -->

                    {footer}
                    
                    <!-- =========================================================== -->

                </body>

                </html>        
                """

    informacion.write(html)

    # ====================================


def crearDetalles():
    data = db.get_todas_actividades()  # retorna las tuplas en un rango
    for i in range(len(data)):
        datos = data[i]
        #  datos:
        #         (120, 'Padre Hurtado', 'Estadio Comunal', 'Dante Torobolino', 'dante@juegostorobolino.cl', '+56955555555', datetime.datetime(2022, 4, 13, 13, 0), datetime.datetime(2022, 4, 13, 19, 0), 'juegos de ayer y hoy', 'juegos') 

        region = db.get_region(datos[1])
        fotos = db.get_fotos(datos[0])
        contactos = db.get_contacto(datos[0])

        createActividadInfo(datos, region, fotos, contactos)
