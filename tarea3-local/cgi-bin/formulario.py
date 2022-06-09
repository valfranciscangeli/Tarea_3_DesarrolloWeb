#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'tarea3')

# ======================== CREAMOS OPCIONES DE SELECT =================================
regiones_opt = ""
regiones = db.get_regiones()
for region in regiones:
    regiones_opt += f"                  <option value='{region[0]}'>{region[1].title()}</option>\n"

comunas_opt = ""
comunas = db.get_comunas(region[0])
for comuna in comunas:
    comunas_opt += f"                   <option value='{comuna[0]}'>{comuna[1].title()}</option>\n"

temas_opt = ""
temas = db.get_temas()
for tema in temas:
    temas_opt += f"                    <option value='{tema[0]}'>{tema[1].title()}</option>\n"
temas_opt += "                    <option value='otro'>Otro</option>"

# ======================== CREAMOS PARTES DEL FORMULARIO =================================
head_footer = open('./templates/header+footer_formulario.html', mode='r', encoding='utf-8').read()

titulo = "HobbyApp - Agregar actividad"

funcion = "onload='fecha()'"

form1 = """
     <div class="w3-container">
        <form id="formulario" class="w3-container w3-card-4" action="save_actividad.py" method="POST" enctype = "multipart/form-data">
            <h2>Ingresa una nueva actividad:</h2>

            <!-- ########### seccion 1 ########### -->

            <h3>¿Dónde?</h3>

            <!-- region -->
            <div class="w3-section">
                <label for="region">Región(*):</label>
                <select name="region" id="region" onchange="input_comuna()">
                    <option value="" disabled selected>Seleccione una región</option>
"""

form1 += regiones_opt

form1 += """
    </select>
            </div>

            <!-- comuna -->
            <div class="w3-section">
                <label for="comuna">Comuna(*):</label>
                <select name="comuna" id="comuna"></select><br>
"""

# form1+= comunas_opt

form1 += """
    </div>

            <!-- sector -->
            <div class="w3-section">
                <label for="sector">Sector:</label>
                <input type="text" class="w3-input" name="sector" id="sector"
                    placeholder="Calle Principal 123, sector plaza." size="100"><br>
            </div>

            <!-- ########### seccion 2 ########### -->
            <h2>¿Quién organiza?</h2>

            <!-- nombre -->
            <div class="w3-section">
                <label for="nombre">Nombre(*):</label>
                <input type="text" class="w3-input" name="nombre" id="nombre" size="100" placeholder="Juan Pérez"><br>
            </div>

            <!-- email -->
            <div class="w3-section">
                <label for="email">Correo electrónico(*):</label>
                <input type="text" class="w3-input" name="email" id="email" placeholder="hola@correo.com"
                    size="100"><br>
            </div>

            <!-- numero de celular -->
            <div class="w3-section">
                <label for="celular">Teléfono celular:</label>
                <input type="text" class="w3-input" name="celular" id="celular" size="15"
                    placeholder="+56 9 1234 5678"><br>
            </div>

            <!-- contactar por -->
            <div class="w3-section">
                <div id="div-contactar-por">
                    <label>Contacto: (seleccione máximo 5)</label><br><br>

                    <input type="checkbox" id="whatsapp" name="contactar-por" value="whatsapp"
                        onclick="agregaUsuarioURL('whatsapp', 'ws-input')">
                    <label for="whatsapp" id="whatsapp-label">WhatsApp</label>
                    <div id="ws-input" style="display:none">
                        <label for="whatsapp-usuario">Usuario / URL:</label>
                        <input type="text" name="whatsapp-usuario" id="whatsapp-usuario"><br>
                    </div><br>

                    <input type="checkbox" id="telegram" name="contactar-por" value="telegram"
                        onclick="agregaUsuarioURL('telegram', 'tl-input')">
                    <label for="telegram">Telegram</label>
                    <div id="tl-input" style="display:none">
                        <label for="telegram-usuario">Usuario / URL:</label>
                        <input type="text" name="telegram-usuario" id="telegram-usuario"><br>
                    </div><br>

                    <input type="checkbox" id="twitter" name="contactar-por" value="twitter"
                        onclick="agregaUsuarioURL('twitter', 'tw-input')">
                    <label for="twitter">Twitter</label>
                    <div id="tw-input" style="display:none">
                        <label for="twitter-usuario">Usuario / URL:</label>
                        <input type="text" name="twitter-usuario" id="twitter-usuario"><br>
                    </div><br>

                    <input type="checkbox" id="instagram" name="contactar-por" value="instagram"
                        onclick="agregaUsuarioURL('instagram', 'ig-input')">
                    <label for="instagram">Instagram</label>
                    <div id="ig-input" style="display:none">
                        <label for="instagram-usuario">Usuario / URL:</label>
                        <input type="text" name="instagram-usuario" id="instagram-usuario"><br>
                    </div><br>

                    <input type="checkbox" id="facebook" name="contactar-por" value="facebook"
                        onclick="agregaUsuarioURL('facebook', 'fb-input')">
                    <label for="facebook">Facebook</label>
                    <div id="fb-input" style="display:none">
                        <label for="facebook-usuario">Usuario / URL:</label>
                        <input type="text" name="facebook-usuario" id="facebook-usuario"><br>
                    </div> <br>

                    <input type="checkbox" id="tiktok" name="contactar-por" value="tiktok"
                        onclick="agregaUsuarioURL('tiktok', 'tt-input')">
                    <label for="tiktok">TikTok</label>
                    <div id="tt-input" style="display:none">
                        <label for="tiktok-usuario">Usuario / URL:</label>
                        <input type="text" name="tiktok-usuario" id="tiktok-usuario"><br>
                    </div> <br>

                    <input type="checkbox" id="otro" name="contactar-por" value="otro"
                        onclick="agregaUsuarioURL('otro', 'otro-input')">
                    <label for="otro">Otro</label>
                    <div id="otro-input" style="display:none">
                        <label for="otro-usuario">URL:</label>
                        <input type="text" name="otro-usuario" id="otro-usuario">
                    </div> <br>

                </div>
            </div>

            <!-- ########### seccion 3 ########### -->
            <h2>¿Cuándo y de qué trata?</h2>

            <!-- dia hora inicio -->
            <div class="w3-section">
                <label for="dia-hora-inicio">Día y hora de inicio(*):</label>
                <input type="text" class="w3-input" id="dia-hora-inicio" name="dia-hora-inicio" size="20"><br>
            </div>

            <!-- dia hora termino -->
            <div class="w3-section">
                <label for="dia-hora-termino">Día y hora de termino:</label>
                <input type="text" class="w3-input" id="dia-hora-termino" name="dia-hora-termino" size="20"><br>
            </div>

            <!-- descripcion -->
            <div class="w3-section">
                <label for="descripcion-evento">Descripción:</label><br>
                <textarea name="descripcion-evento" id="descripcion-evento" cols="50" rows="10"></textarea><br>
            </div><br>

            <!-- tema -->
            <div class="w3-section">
                <label for="tema">Tema(*):</label>
                <select name="tema" id="tema" onchange="nuevo_tema()">
                    <option value="" disabled selected>Seleccione un tema</option>
            """

form1 += temas_opt

form1 += """
                    </select>
                <div id="otro_tema"></div>
            </div> <br>

            <!-- foto -->
            <label for="foto-actividad1">Fotos(*): (puede cargar de 1 a 5 imágenes) </label><br>
            <div class="w3-section" id="fotos">

                <div id="contenedor-foto1">
                    <input type="file" id="foto-actividad1" name="foto-actividad" accept="image/*">
                    <button type="button" class="w3-button w3-theme w3-round-xxlarge" onclick="agregarImagen()">Agregar
                        otra
                        foto</button>
                </div>

                <div id="contenedor-foto2"></div>
                <div id="contenedor-foto3"></div>
                <div id="contenedor-foto4"></div>
                <div id="contenedor-foto5"></div>

            </div><br>
            <!-- ########################################################## -->
            <!-- SUBMIT-->

            <div class="w3-section">
                <input type="submit" class="w3-button w3-black" value="Agregar esta actividad">
            </div>


            <small>(*) Datos obligatorios.</small>

        </form><br> <br>

    </div>
    <!-- ###################### confirmación de formulario #################################### -->

    <div id="capa" class="capaModal">
        <div>
            <h1>Confirma el envio del formulario</h1>
            <p>¿Está seguro que desea agregar esta actividad?</p>
            <div class="buttons">
                <input type="button" class="w3-button w3-theme" value="Sí, estoy seguro" id="ok">&nbsp;
                <input type="button" class="w3-button w3-theme-light"
                    value="No, no estoy seguro. Quiero volver al formulario" id="ko">
            </div>
        </div>
    </div>
"""

js = """
<script>
        // ###################### confirmacion de envio del formulario   ################################
        document.getElementById("formulario").addEventListener("submit", submit);
        document.getElementById("ok").addEventListener("click", enviar);
        document.getElementById("ko").addEventListener("click", cancelar);

        // Funcion que se ejecuta al pulsar el botón enviar el formulario
        function submit(e) {
            // Cancelams el envio a la espera de que valide el formulario
            e.preventDefault();

            // Mostramos la capa con el formulario de validacion si es que el formulario es valido
            if (validateForm()) {
                document.getElementById("capa").style.display = "block";
            }
        }

        // Funcion que se ejecuta al pulsar el boton Enviar de cuadro de dialogo
        function enviar(e) {
            // Escondemos la capa
            document.getElementById("capa").style.display = "none";

            // Enviamos el formulario
            document.forms["formulario"].submit();
        }

        // Funcion que se ejecuta al pulsar el boton Cancelar de cuadro de dialogo
        function cancelar(e) {
            // Simplemente escondemkos el formulario
            document.getElementById("capa").style.display = "none";
        }
    </script>
"""

# ======================= PRINT FINAL ==================================
print(head_footer.format(titulo, funcion, form1, js))
