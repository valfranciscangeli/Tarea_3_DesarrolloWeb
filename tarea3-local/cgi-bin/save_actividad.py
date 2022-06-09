#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

import cgi
import re

from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'tarea3')

form = cgi.FieldStorage()

template = open('../templates/respuesta-recibida.html', mode='r',
                encoding="utf-8").read()  # abrimos el template de respuesta


# ====================== revisamos que se hayan ingresado todos los campos obligatorios===============================================

# funcion que revisa si string se construye con una ER
def check(regex, value):
    return re.fullmatch(regex, value)


# string que suma todas las alertas de error
errores = "<ul>Su formulario tiene errores:</ul>"
largo_inicial = len(errores)

# REGION :========================
if 'region' not in form:
    errores += '<li>Por favor, seleccione una REGION del menú.</li>'
else:
    region = form['region'].value
    if int(region) < 1 or int(region) > 16:
        errores += '<li>Ha seleccionado una REGION no permitida.</li>'

# COMUNA :========================
if 'comuna' not in form:
    errores += '<li>Por favor, seleccione una COMUNA del menú.</li>'
else:
    comuna = form['comuna'].value
    comunas = ['10101', '10102', '10201', '10202', '10301', '10302', '10303', '10304', '10305', '10306', '10307',
               '20101', '20102', '20201', '20202', '20203', '20301', '20302', '20303', '20304', '30101', '30102',
               '30201', '30202', '30203', '30301', '30302', '30303', '30304', '40101', '40102', '40103', '40104',
               '40105', '40106', '40201', '40202', '40203', '40204', '40205', '40301', '40302', '40303', '40304',
               '50101', '50102', '50103', '50104', '50105', '50201', '50202', '50203', '50204', '50205', '50206',
               '50301', '50302', '50303', '50304', '50305', '50306', '50307', '50401', '50402', '50403', '50404',
               '50501', '50502', '50503', '50504', '50505', '50506', '50507', '50508', '50509', '50601', '50701',
               '50702', '50703', '50704', '50705', '50706', '60101', '60102', '60103', '60104', '60105', '60106',
               '60107', '60108', '60109', '60110', '60111', '60112', '60113', '60114', '60115', '60116', '60117',
               '60201', '60202', '60203', '60204', '60205', '60206', '60301', '60302', '60303', '60304', '60305',
               '60306', '60307', '60308', '60309', '60310', '70101', '70102', '70103', '70104', '70105', '70106',
               '70107', '70108', '70109', '70201', '70202', '70203', '70204', '70205', '70206', '70207', '70208',
               '70209', '70210', '70301', '70302', '70303', '70304', '70305', '70306', '70307', '70308', '70401',
               '70402', '70403', '80101', '80102', '80103', '80104', '80105', '80106', '80107', '80108', '80109',
               '80110', '80111', '80112', '80113', '80114', '80115', '80116', '80117', '80118', '80119', '80120',
               '80121', '80201', '80202', '80203', '80204', '80205', '80206', '80207', '80208', '80209', '80210',
               '80211', '80212', '80301', '80302', '80303', '80304', '80305', '80306', '80307', '80308', '80309',
               '80310', '80311', '80312', '80313', '80314', '80401', '80402', '80403', '80404', '80405', '80406',
               '80407', '90101', '90102', '90103', '90104', '90105', '90106', '90107', '90108', '90109', '90110',
               '90111', '90201', '90202', '90203', '90204', '90205', '90206', '90207', '90208', '90209', '90210',
               '90211', '90212', '90213', '90214', '90215', '90216', '90217', '90218', '90219', '90220', '90221',
               '100101', '100102', '100103', '100104', '100105', '100106', '100107', '100108', '100109', '100110',
               '100111', '100112', '100201', '100202', '100203', '100204', '100205', '100206', '100207', '100301',
               '100302', '100303', '100304', '100305', '100306', '100307', '100308', '100309', '100401', '100402',
               '100403', '100404', '100405', '100406', '100407', '100408', '100409', '100410', '100501', '100502',
               '100503', '100504', '110101', '110102', '110103', '110201', '110202', '110301', '110302', '110401',
               '110402', '110403', '120101', '120102', '120201', '120202', '120203', '120204', '120301', '120302',
               '120303', '120401', '130101', '130102', '130103', '130201', '130202', '130203', '130204', '130205',
               '130206', '130207', '130208', '130209', '130210', '130211', '130212', '130213', '130214', '130215',
               '130216', '130217', '130218', '130219', '130220', '130221', '130222', '130223', '130224', '130225',
               '130226', '130227', '130228', '130229', '130230', '130231', '130232', '130301', '130302', '130303',
               '130401', '130402', '130403', '130404', '130501', '130502', '130503', '130504', '130601', '130602',
               '130603', '130604', '130605', '130606']

    if comuna not in comunas:
        errores += '<li>Ha seleccionado una COMUNA no permitida.</li>'

# NOMBRE DEL ORGANIZADOR :========================
if 'nombre' not in form:
    errores += '<li>Por favor, ingrese el NOMBRE del organizador.</li>'
else:
    nombre = form['nombre'].value
    if nombre == '':
        errores += '<li>El ingreso de NOMBRE es obligatorio.</li>'
    elif len(nombre) > 200:
        errores += '<li>Por favor, ingrese un NOMBRE de largo menor a 200 caracteres.</li>'

# CORREO ELECTRONICO :========================
if 'email' not in form:
    errores += '<li>Por favor, ingrese un EMAIL de contacto.</li>'
else:
    email = form['email'].value
    regex1 = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if email == '':
        errores += '<li>El ingreso de CORREO ELECTRONICO es obligatorio.</li>'
    elif not (check(regex1, email)):
        errores += '<li>Por favor, ingrese un CORREO de formato válido.</li>'

# DIA-HORA INICIO :========================
if 'dia-hora-inicio' not in form:
    errores += '<li>Por favor, ingrese una HORA DE INICIO.</li>'
else:
    inicio = form['dia-hora-inicio'].value
    regex3 = '^(\d\d\d\d)-(0?[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])\s(00|0[0-9]|1[0-9]|2[0-3]):(0[0-9]|[0-5][0-9])$'
    if inicio == '':
        errores += '<li>El ingreso de FECHA Y HORA DE INICIO es obligatorio.</li>'
    if not (check(regex3, inicio)):
        errores += '<li>Por favor, ingrese un HORARIO DE INICIO de formato correcto.</li>'

# TEMA :========================
if 'tema' not in form:
    errores += '<li>Por favor, seleccione un TEMA del menú.</li>'
else:
    tema = form['tema'].value
    regex4 = '^\d+$'
    if tema != 'otro' and not (check(regex4, tema)):
        errores += '<li>Ha seleccionado un TEMA no permitido.</li>'
    if tema == 'otro':
        if 'nuevo-tema' not in form:
            errores += '<li>Debe ingresar un NUEVO TEMA.</li>'
        else:
            otro_tema = form['nuevo-tema'].value
            if len(otro_tema) < 3 or len(otro_tema) > 15:
                errores += '<li>Debe ingresar un NUEVO TEMA de tamaño entre 3 y 15 caracteres.</li>'


# FOTOS :========================
def revisar_foto(imagen):
    alert = ''
    MAX_FILE_SIZE = 1000000
    blanks = 0
    if imagen.filename:
        tipo = imagen.type
        size = os.fstat(imagen.file.fileno()).st_size
        if not (tipo == 'image/jpeg' or tipo == 'image/png' or tipo == 'image/gif'):
            alert += '<li>Error, formato no válido.{}</li>'.format(tipo)
        if size > MAX_FILE_SIZE:
            alert += '<li>Error, archivo muy grande.</li>'
    else:
        blanks += 1

    return alert, blanks


if 'foto-actividad' not in form:  # no hay input de foto en el form recibido
    errores += '<li>Por favor, carge al menos 1 IMAGEN.</li>'
else:
    fotos = form['foto-actividad']  # todas las fotos

    if type(fotos) == list:  # significa que se cargo + de 1 archivo
        # print('es lista')  # test
        contador = 0
        for foto in fotos:
            resultado = revisar_foto(foto)
            errores += resultado[0]
            if resultado[1] > 0:
                contador += 1
                errores += f'<li>Error, archivo de IMAGEN {contador} no subido.</li>'

    else:  # se subio solo 1 archivo
        # print('no es lista')  # test
        resultado = revisar_foto(fotos)
        errores += resultado[0]
        if resultado[1] > 0:
            errores += f'<li>Error, ningún archivo de IMAGEN subido.</li>'

# # ====================== recuperamos los valores de los inputs que aparecen aunque esten vacios =================================

# lugar
sector = form['sector'].value
if len(sector) > 100:
    errores += f'<li>Por favor, ingrese un SECTOR de menos de 100 caracteres. ({len(sector)} caracteres usados).</li>'

# contacto
celular = form['celular'].value
regex2 = '^[+][5][6]\s[2-9]\s[0-9]{4}\s[0-9]{4}$'
if celular != '' and not (check(regex2, celular)):
    errores += '<li>Por favor, ingrese un número CELULAR de formato válido. (+56 9 1234 5678).</li>'

# sobre la actividad
termino = form['dia-hora-termino'].value
regex3 = '^(\d\d\d\d)-(0?[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])\s(00|0[0-9]|1[0-9]|2[0-3]):(0[0-9]|[0-5][0-9])$'
if termino != '' and not (check(regex3, termino)):
    errores += '<li>Por favor, ingrese un HORARIO DE TERMINO de formato correcto.</li>'
# por simplicidad no vamos a revisar con cgi que sea posterior a la fecha de inicio

descripcion = form['descripcion-evento'].value  # no tiene restricciones


# ========================
# redes sociales

def validar_user(usuario):
    return 4 <= len(usuario) <= 50


wspUser = form['whatsapp-usuario'].value  # user whatsapp
tlgUser = form['telegram-usuario'].value  # user telegram
twUser = form['twitter-usuario'].value  # user twitter
igUser = form['instagram-usuario'].value  # user instagram
fbUser = form['facebook-usuario'].value  # user facebook
tkUser = form['tiktok-usuario'].value  # user tiktok
otroUser = form['otro-usuario'].value  # user otra rrss

if 'contactar-por' in form:  # si no se selecciona en el checkbox no hay contactar por
    contacto = form['contactar-por']
    if type(contacto) == list:
        if len(contacto) > 5:
            errores += f'<li>Por favor, ingrese un MAXIMO de 5 RRSS de contacto. ({len(contacto)} actividades seleccionadas).</li>'
        else:
            for rrss in contacto:
                red = rrss.value
                if red == 'whatsapp':
                    if not (validar_user(wspUser)):
                        errores += f'<li>Al seleccionar como contacto WHATSAPP debe ingresar un ID o URL para esta red de 4 a 50 caracteres. ({len(wspUser)} caracteres ingresados).</li>'

                elif red == 'telegram':
                    if not (validar_user(tlgUser)):
                        errores += f'<li>Al seleccionar como contacto TELEGRAM debe ingresar un ID o URL para esta red de 4 a 50 caracteres. ({len(tlgUser)} caracteres ingresados).</li>'

                elif red == 'twitter':
                    if not (validar_user(twUser)):
                        errores += f'<li>Al seleccionar como contacto TWITTER debe ingresar un ID o URL para esta red de 4 a 50 caracteres. ({len(twUser)} caracteres ingresados).</li>'

                elif red == 'instagram':
                    if not (validar_user(igUser)):
                        errores += f'<li>Al seleccionar como contacto INSTAGRAM debe ingresar un ID o URL para esta red de 4 a 50 caracteres. ({len(igUser)} caracteres ingresados).</li>'

                elif red == 'facebook':
                    if not (validar_user(fbUser)):
                        errores += f'<li>Al seleccionar como contacto FACEBOOK debe ingresar un ID o URL para esta red de 4 a 50 caracteres. ({len(fbUser)} caracteres ingresados).</li>'

                elif red == 'tiktok':
                    if not (validar_user(tkUser)):
                        errores += f'<li>Al seleccionar como contacto TIKTOK debe ingresar un ID o URL para esta red de 4 a 50 caracteres. ({len(tkUser)} caracteres ingresados).</li>'

                elif red == 'otro':
                    if not (validar_user(otroUser)):
                        errores += f'<li>Al seleccionar como contacto OTRO debe ingresar un ID o URL para esta red de 4 a 50 caracteres. ({len(otroUser)} caracteres ingresados).</li>'

# ========================================================

if len(errores) > largo_inicial:
    print(template.format(errores, '') + ' </div>  </div> <br> <br>')
    sys.exit()

""" ================================================================ 
si llega aqui es que todos los datos pasaron la validación. 
 ================================================================ """

if tema == 'otro':
    # print(otro_tema)
    db.guardar_tema(otro_tema)
    nuevo_temaID = db.get_temaID(otro_tema)
    tema = nuevo_temaID[0][
        0]  # cambiamos el string con el nombre del tema por un string con el id del nuevo tema agregado

actividad = {'comuna': comuna,
             'sector': sector,
             'nombre': nombre,
             'email': email,
             'celular': celular,
             'inicio': inicio,
             'termino': termino,
             'descripcion': descripcion,
             'tema': tema
             }

#                 nombre      identificador
redes_sociales = {'whatsapp': wspUser,
                  'telegram': tlgUser,
                  'twitter': twUser,
                  'instagram': igUser,
                  'facebook': fbUser,
                  'tiktok': tkUser,
                  'otroUser': otroUser
                  }

if not (type(fotos) == list):
    fotos = [fotos]

data = (actividad, redes_sociales, fotos)

db.save_data(data)  # ejecutamos consulta para guardar la actividad

todoOk = """
            <h1>¡Tu formulario ha sido recibido!</h1>
            <h2>Gracias por agregar tu actividad.</h2>
            <h3>HobbyApp te desea mucho éxito.</h3>
"""

print(template.format(todoOk, '  <meta http-equiv="refresh" content="1; url=./portada.py">'))
