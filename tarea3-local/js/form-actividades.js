/* Código JavaScript para página de formulario. 

Aquí se encuentra tanto validación del formulario como otras funciones utilizadas para su implementación. 

Por Valeria Vallejos Franciscangeli 
Para CC5002- otoño 2022 */


/* =========================INICIO DEL DOCUMENTO================================ */

// Arreglos con las comunas por region ##########################

const tarapaca = [
    ['10307', 'Alto Hospicio'],
    ['10301', 'Camiña'],
    ['10306', 'Colchane'],
    ['10302', 'Huara'],
    ['10304', 'Iquique'],
    ['10305', 'Pica'],
    ['10303', 'Pozo Almonte'],
];
const antofagasta = [
    ['20303', 'Antofagasta'],
    ['20202', 'Calama'],
    ['20102', 'Maria Elena'],
    ['20302', 'Mejillones'],
    ['20201', 'Ollague'],
    ['20203', 'San Pedro Atacama'],
    ['20301', 'Sierra Gorda'],
    ['20304', 'Taltal'],
    ['20101', 'Tocopilla'],
];
const atacama = [
    ['30304', 'Alto del Carmen'],
    ['30201', 'Caldera'],
    ['30102', 'Chañaral'],
    ['30202', 'Copiapo'],
    ['30101', 'Diego de Almagro'],
    ['30302', 'Freirina'],
    ['30301', 'Huasco'],
    ['30203', 'Tierra Amarilla'],
    ['30303', 'Vallenar'],
];
const coquimbo = [
    ['40106', 'Andacollo'],
    ['40205', 'Combarbala'],
    ['40105', 'Coquimbo'],
    ['40302', 'Illapel'],
    ['40101', 'La Higuera'],
    ['40102', 'La Serena'],
    ['40304', 'Los Vilos'],
    ['40301', 'Mincha'],
    ['40203', 'Monte Patria'],
    ['40202', 'Ovalle'],
    ['40104', 'Paihuano'],
    ['40204', 'Punitaqui'],
    ['40201', 'Rio Hurtado'],
    ['40303', 'Salamanca'],
    ['40103', 'Vicuña'],
];
const ohiggins = [
    ['60309', 'Chepica'],
    ['60304', 'Chimbarongo'],
    ['60102', 'Codegua'],
    ['60109', 'Coinco'],
    ['60110', 'Coltauco'],
    ['60107', 'Doñihue'],
    ['60103', 'Graneros'],
    ['60202', 'La Estrella'],
    ['60112', 'Las Cabras'],
    ['60205', 'Litueche'],
    ['60310', 'Lolol'],
    ['60104', 'Machali'],
    ['60116', 'Malloa'],
    ['60203', 'Marchigue'],
    ['60101', 'Mostazal'],
    ['60306', 'Nancagua'],
    ['60201', 'Navidad'],
    ['60106', 'Olivar'],
    ['60305', 'Palmilla'],
    ['60206', 'Paredones'],
    ['60302', 'Peralillo'],
    ['60114', 'Peumo'],
    ['60115', 'Pichidegua'],
    ['60204', 'Pichilemu'],
    ['60303', 'Placilla'],
    ['60308', 'Pumanque'],
    ['60111', 'Quinta Tilcoco'],
    ['60105', 'Rancagua'],
    ['60113', 'Rengo'],
    ['60108', 'Requinoa'],
    ['60301', 'San Fernando'],
    ['60117', 'San Vicente'],
    ['60307', 'Santa Cruz'],
];
const valparaiso = [
    ['50701', 'Algarrobo'],
    ['50102', 'Cabildo'],
    ['50403', 'Calle Larga'],
    ['50704', 'Cartagena'],
    ['50508', 'Casablanca'],
    ['50205', 'Catemu'],
    ['50509', 'Concon'],
    ['50702', 'El Quisco'],
    ['50703', 'El Tabo'],
    ['50303', 'Hijuelas'],
    ['50601', 'Isla de Pascua'],
    ['50507', 'Juan Fernandez'],
    ['50302', 'La Calera'],
    ['50304', 'La Cruz'],
    ['50104', 'La Ligua'],
    ['50307', 'Limache'],
    ['50206', 'Llay Llay'],
    ['50401', 'Los Andes'],
    ['50301', 'Nogales'],
    ['50306', 'Olmue'],
    ['50103', 'Papudo'],
    ['50204', 'Pencahue'],
    ['50101', 'Petorca'],
    ['50501', 'Puchuncavi'],
    ['50201', 'Putaendo'],
    ['50305', 'Quillota'],
    ['50505', 'Quilpue'],
    ['50502', 'Quintero'],
    ['50402', 'Rinconada'],
    ['50705', 'San Antonio'],
    ['50404', 'San Esteban'],
    ['50203', 'San Felipe'],
    ['50202', 'Santa Maria'],
    ['50706', 'Santo Domingo'],
    ['50506', 'Valparaiso'],
    ['50504', 'Villa Alemana'],
    ['50503', 'Viña del Mar'],
    ['50105', 'Zapallar'],
];
const maule = [
    ['70403', 'Cauquenes'],
    ['70401', 'Chanco'],
    ['70302', 'Colbun'],
    ['70207', 'Constitucion'],
    ['70202', 'Curepto'],
    ['70104', 'Curico'],
    ['70209', 'Empedrado'],
    ['70106', 'Hualañe'],
    ['70109', 'Licanten'],
    ['70305', 'Linares'],
    ['70306', 'Longavi'],
    ['70208', 'Maule'],
    ['70108', 'Molina'],
    ['70308', 'Parral'],
    ['70203', 'Pelarco'],
    ['70402', 'Pelluhue'],
    ['70205', 'Pencahue'],
    ['70103', 'Rauco'],
    ['70307', 'Retiro'],
    ['70201', 'Rio Claro'],
    ['70102', 'Romeral'],
    ['70105', 'Sagrada Familia'],
    ['70206', 'San Clemente'],
    ['70301', 'San Javier'],
    ['70210', 'San Rafael'],
    ['70204', 'Talca'],
    ['70101', 'Teno'],
    ['70107', 'Vichuquen'],
    ['70303', 'Villa Alegre'],
    ['70304', 'Yerbas Buenas'],
];
const biobio = [
    ['80314', 'Alto Bio Bio'],
    ['80304', 'Antuco'],
    ['80401', 'Arauco'],
    ['80301', 'Cabrero'],
    ['80405', 'Cañete'],
    ['80210', 'Chiguayante'],
    ['80205', 'Concepcion'],
    ['80406', 'Contulmo'],
    ['80207', 'Coronel'],
    ['80402', 'Curanilahue'],
    ['80202', 'Florida'],
    ['80212', 'Hualpen'],
    ['80206', 'Hualqui'],
    ['80306', 'Laja'],
    ['80404', 'Lebu'],
    ['80403', 'Los Alamos'],
    ['80308', 'Los Angeles'],
    ['80208', 'Lota'],
    ['80313', 'Mulchen'],
    ['80309', 'Nacimiento'],
    ['80310', 'Negrete'],
    ['80203', 'Penco'],
    ['80312', 'Quilaco'],
    ['80307', 'Quilleco'],
    ['80211', 'San Pedro de la Paz'],
    ['80305', 'San Rosendo'],
    ['80311', 'Santa Barbara'],
    ['80209', 'Santa Juana'],
    ['80204', 'Talcahuano'],
    ['80407', 'Tirua'],
    ['80201', 'Tome'],
    ['80303', 'Tucapel'],
    ['80302', 'Yumbel'],
];
const araucania = [
    ['90102', 'Angol'],
    ['90206', 'Carahue'],
    ['90221', 'Cholchol'],
    ['90103', 'Collipulli'],
    ['90210', 'Cunco'],
    ['90110', 'Curacautin'],
    ['90218', 'Curarrehue'],
    ['90106', 'Ercilla'],
    ['90211', 'Freire'],
    ['90202', 'Galvarino'],
    ['90214', 'Gorbea'],
    ['90203', 'Lautaro'],
    ['90219', 'Loncoche'],
    ['90111', 'Lonquimay'],
    ['90104', 'Los Sauces'],
    ['90107', 'Lumaco'],
    ['90207', 'Melipeuco'],
    ['90208', 'Nueva Imperial'],
    ['90220', 'Padre Las Casas'],
    ['90201', 'Perquenco'],
    ['90212', 'Pitrufquen'],
    ['90215', 'Pucon'],
    ['90209', 'Puerto Saavedra'],
    ['90105', 'Puren'],
    ['90101', 'Renaico'],
    ['90205', 'Temuco'],
    ['90213', 'Teodoro Schmidt'],
    ['90217', 'Tolten'],
    ['90109', 'Traiguen'],
    ['90108', 'Victoria'],
    ['90204', 'Vilcun'],
    ['90216', 'Villarrica'],
];
const lagos = [
    ['100401', 'Ancud'],
    ['100308', 'Calbuco'],
    ['100405', 'Castro'],
    ['100501', 'Chaiten'],
    ['100406', 'Chonchi'],
    ['100309', 'Cochamo'],
    ['100404', 'Curaco de Velez'],
    ['100403', 'Dalcahue'],
    ['100302', 'Fresia'],
    ['100301', 'Frutillar'],
    ['100502', 'Futaleufu'],
    ['100504', 'Hualaihue'],
    ['100303', 'Llanquihue'],
    ['100305', 'Los Muermos'],
    ['100307', 'Maullin'],
    ['100203', 'Osorno'],
    ['100503', 'Palena'],
    ['100306', 'Puerto Montt'],
    ['100207', 'Puerto Octay'],
    ['100304', 'Puerto Varas'],
    ['100410', 'Puqueldon'],
    ['100206', 'Purranque'],
    ['100204', 'Puyehue'],
    ['100407', 'Queilen'],
    ['100408', 'Quellon'],
    ['100402', 'Quemchi'],
    ['100409', 'Quinchao'],
    ['100205', 'Rio Negro'],
    ['100202', 'San Juan'],
    ['100201', 'San Pablo'],
];
const aysen = [
    ['110103', 'Aysen'],
    ['110302', 'Chile Chico'],
    ['110102', 'Cisnes'],
    ['110401', 'Cochrane'],
    ['110201', 'Coyhaique'],
    ['110101', 'Guaitecas'],
    ['110202', 'Lago Verde'],
    ['110403', "O'Higins"],
    ['110301', 'Rio Iba?ez'],
    ['110402', 'Tortel'],
];
const magallanes = [
    ['120401', 'Antartica'],
    ['120201', 'Laguna Blanca'],
    ['120301', 'Porvenir'],
    ['120302', 'Primavera'],
    ['120102', 'Puerto Natales'],
    ['120204', 'Punta Arenas'],
    ['120203', 'Rio Verde'],
    ['120202', 'San Gregorio'],
    ['120303', 'Timaukel'],
    ['120101', 'Torres del Paine'],
];
const santiago = [
    ['130605', 'Alhue'],
    ['130403', 'Buin'],
    ['130402', 'Calera de Tango'],
    ['130230', 'Cerrillos'],
    ['130232', 'Cerro Navia'],
    ['130102', 'Colina'],
    ['130201', 'Conchali'],
    ['130601', 'Curacavi'],
    ['130226', 'El Bosque'],
    ['130503', 'El Monte'],
    ['130229', 'Estacion Central'],
    ['130217', 'Huechuraba'],
    ['130216', 'Independencia'],
    ['130504', 'Isla de Maipo'],
    ['130213', 'La Cisterna'],
    ['130214', 'La Florida'],
    ['130215', 'La Granja'],
    ['130224', 'La Pintana'],
    ['130209', 'La Reina'],
    ['130103', 'Lampa'],
    ['130204', 'Las Condes'],
    ['130220', 'Lo Barrenechea'],
    ['130228', 'Lo Espejo'],
    ['130231', 'Lo Prado'],
    ['130221', 'Macul'],
    ['130212', 'Maipu'],
    ['130602', 'Maria Pinto'],
    ['130603', 'Melipilla'],
    ['130210', 'Ñuñoa'],
    ['130606', 'Padre Hurtado'],
    ['130404', 'Paine'],
    ['130227', 'Pedro Aguirre Cerda'],
    ['130501', 'Peñaflor'],
    ['130222', 'Peñalolen'],
    ['130303', 'Pirque'],
    ['130207', 'Providencia'],
    ['130205', 'Pudahuel'],
    ['130302', 'Puente Alto'],
    ['130202', 'Quilicura'],
    ['130206', 'Quinta Normal'],
    ['130218', 'Recoleta'],
    ['130203', 'Renca'],
    ['130401', 'San Bernardo'],
    ['130223', 'San Joaquin'],
    ['130301', 'San Jose de Maipo'],
    ['130211', 'San Miguel'],
    ['130604', 'San Pedro'],
    ['130225', 'San Ramon'],
    ['130208', 'Santiago'],
    ['130502', 'Talagante'],
    ['130101', 'Tiltil'],
    ['130219', 'Vitacura'],
];
const rios = [
    ['100107', 'Corral'],
    ['100109', 'Futrono'],
    ['100111', 'La Union'],
    ['100110', 'Lago Ranco'],
    ['100101', 'Lanco'],
    ['100106', 'Los Lagos'],
    ['100104', 'Mafil'],
    ['100102', 'Mariquina'],
    ['100108', 'Paillaco'],
    ['100103', 'Panguipulli'],
    ['100112', 'Rio Bueno'],
    ['100105', 'Valdivia'],
];
const arica = [
    ['10201', 'Arica'],
    ['10202', 'Camarones'],
    ['10101', 'Gral. Lagos'],
    ['10102', 'Putre'],
];
const nuble = [
    ['80114', 'Bulnes'],
    ['80110', 'Chillan'],
    ['80121', 'Chillan Viejo'],
    ['80101', 'Cobquecura'],
    ['80113', 'Coelemu'],
    ['80109', 'Coihueco'],
    ['80118', 'El Carmen'],
    ['80106', 'Ninhue'],
    ['80102', 'Ñiquen'],
    ['80119', 'Pemuco'],
    ['80112', 'Pinto'],
    ['80111', 'Portezuelo'],
    ['80117', 'Quillon'],
    ['80105', 'Quirihue'],
    ['80116', 'Ranquil'],
    ['80104', 'San Carlos'],
    ['80103', 'San Fabian'],
    ['80115', 'San Ignacio'],
    ['80108', 'San Nicolas'],
    ['80107', 'Trehuaco'],
    ['80120', 'Yungay'],
];

// #############################################################


// funcion para mostrar comunas por region ======================================

function input_comuna() {
    let region = document.getElementById('region').value;
    let respuesta = '<option value="" disabled selected>Seleccione una comuna</option>';

    // sumar las comunas por region----------------------------------------------------
    function sumarComunas(listaComunas) {
        let resultado = "";
        for (let i = 0; i < listaComunas.length; i++) {
            resultado += '<option value="' + listaComunas[i][0] + '">' + listaComunas[i][1] + '</option>';
        }
        return resultado;
    }

    // condiciones ----------------------------------------------------

    if (region === '1') { respuesta += sumarComunas(tarapaca) }
    if (region === '2') { respuesta += sumarComunas(antofagasta) }
    if (region === '3') { respuesta += sumarComunas(atacama) }
    if (region === '4') { respuesta += sumarComunas(coquimbo) }
    if (region === '5') { respuesta += sumarComunas(valparaiso) }
    if (region === '6') { respuesta += sumarComunas(ohiggins) }
    if (region === '7') { respuesta += sumarComunas(maule) }
    if (region === '8') { respuesta += sumarComunas(biobio) }
    if (region === '9') { respuesta += sumarComunas(araucania) }
    if (region === '10') { respuesta += sumarComunas(lagos) }
    if (region === '11') { respuesta += sumarComunas(aysen) }
    if (region === '12') { respuesta += sumarComunas(magallanes) }
    if (region === '13') { respuesta += sumarComunas(santiago) }
    if (region === '14') { respuesta += sumarComunas(rios) }
    if (region === '15') { respuesta += sumarComunas(arica) }
    if (region === '16') { respuesta += sumarComunas(nuble) }

    // RESPUESTA----------------------------------------------------
    document.getElementById('comuna').innerHTML = respuesta;
}

//################ FECHAS #################

function fecha() {
    let n = new Date();
    let y = n.getFullYear();
    let m = n.getMonth() + 1;
    let d = n.getDate();
    let h = n.getHours();
    let mm = n.getMinutes();
    let t = n.getTime();
    let f = new Date(1000 * 60 * 60 * 3 + t);
    let ny = f.getFullYear();
    let nm = f.getMonth() + 1;
    let nd = f.getDate();
    let nh = f.getHours();
    let nmm = f.getMinutes();

    function norm(num) {
        if (num < 10) {
            return "0" + num;
        }
        return num;
    }

    // funcion que entrega fecha actual ===========================
    function pre_fecha() {
        document.getElementById('dia-hora-inicio').value = y + '-' + norm(m) + '-' + norm(d) + ' ' + norm(h) + ':' + norm(mm);
    }

    // funcion que entrega fecha actual + 3 hrs ====================
    function pos_fecha() {
        document.getElementById('dia-hora-termino').value = ny + '-' + norm(nm) + '-' + norm(nd) + ' ' + norm(nh) + ':' + norm(nmm);
    }

    pre_fecha();
    pos_fecha();
}

//################ caso de que se elija OTRO TEMA #################=========================

function nuevo_tema() {
    if (document.getElementById('tema').value === 'otro') {
        document.getElementById('otro_tema').innerHTML = '<label for="nuevo-tema">Otro tema:</label><input type="text" id="nuevo-tema" name="nuevo-tema"><br>';
    } else {
        document.getElementById('otro_tema').innerHTML = ''
    }
}

//################ VALIDACION #################================================================

function validateForm() {

    /* buscamos los inputs que necesitamos validar */
    let region = document.getElementById('region').value;
    let comuna = document.getElementById('comuna').value;
    let sector = document.getElementById('sector').value;
    let nombre = document.getElementById('nombre').value;
    let email = document.getElementById('email').value;
    let celular = document.getElementById('celular').value;
    let dia_hora_inicio = document.getElementById('dia-hora-inicio').value;
    let dia_hora_termino = document.getElementById('dia-hora-termino').value;
    let descripcion = document.getElementById('descripcion-evento').value;
    let tema = document.getElementById('tema').value;
    let fotos = document.getElementsByName('foto-actividad');

    /* Errors contendrá todos los errores que vayamos encontrando y luego los escribiremos según corresponda*/
    let errors = 'Su formulario tiene fallas:\n';

    /* llamadas a funciones validadoras ################################################################*/

    const valores = [validar_region(region),
    validar_comuna(comuna),
    validar_sector(sector),
    validar_nombre(nombre),
    validar_email(email),
    validar_celular(celular),
    validar_contacto(),
    validar_hora_inicio(dia_hora_inicio),
    validar_hora_termino(dia_hora_termino, dia_hora_inicio),
    validar_descripcion(descripcion),
    validar_tema(tema),
    validar_fotos(fotos)];

    /* calculamos decision final: válido (true) o inválido (false) */

    let res = true;
    let aux;

    for (let i = 0; i < 12; i++) {
        // alert("entre en el for");
        aux = valores[i][0];
        // alert(" aux es: "+aux);
        res = res && aux;
        // alert("res es: "+res);
        errors += valores[i][1];
        // alert(errors);
        //alert(i);
    }

    // ======================== respuesta final ============================

    /*Finalmente si hay errores lo escribimos en una alerta */
    if (!res) {
        alert(errors);
    }

    /* respuesta final de validateForm */
    return res;

    // return true; // true para poder revisar con cgi-bin
}

/* funcion que valida que se haya seleccionado una de las regiones del menu ===========  */
function validar_region(region) {
    //alert("estoy validando region")
    if (region === "") {
        return [false, "- La selección de REGIÓN es OBLIGATORIA.\n"];
    }
    const regs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']

    if (regs.includes(region)) {
        return [true, ""];
    }
    return [false, "- Por favor, seleccione una de las regiones del menú.\n"];
}

/* funcion que valida que se haya seleccionado una de las comunas del menu  ======================*/
function validar_comuna(comuna) {
    if (comuna === "") {
        return [false, "- La selección de COMUNA es OBLIGATORIA.\n"];
    }
    let coms = ['10101', '10102', '10201', '10202', '10301', '10302', '10303', '10304', '10305', '10306', '10307', '20101', '20102', '20201', '20202', '20203',
        '20301', '20302', '20303', '20304', '30101', '30102', '30201', '30202', '30203', '30301', '30302', '30303', '30304', '40101', '40102', '40103',
        '40104', '40105', '40106', '40201', '40202', '40203', '40204', '40205', '40301', '40302', '40303', '40304', '50101', '50102', '50103', '50104',
        '50105', '50201', '50202', '50203', '50204', '50205', '50206', '50301', '50302', '50303', '50304', '50305', '50306', '50307', '50401', '50402',
        '50403', '50404', '50501', '50502', '50503', '50504', '50505', '50506', '50507', '50508', '50509', '50601', '50701', '50702', '50703', '50704',
        '50705', '50706', '60101', '60102', '60103', '60104', '60105', '60106', '60107', '60108', '60109', '60110', '60111', '60112', '60113', '60114',
        '60115', '60116', '60117', '60201', '60202', '60203', '60204', '60205', '60206', '60301', '60302', '60303', '60304', '60305', '60306', '60307',
        '60308', '60309', '60310', '70101', '70102', '70103', '70104', '70105', '70106', '70107', '70108', '70109', '70201', '70202', '70203', '70204',
        '70205', '70206', '70207', '70208', '70209', '70210', '70301', '70302', '70303', '70304', '70305', '70306', '70307', '70308', '70401', '70402',
        '70403', '80101', '80102', '80103', '80104', '80105', '80106', '80107', '80108', '80109', '80110', '80111', '80112', '80113', '80114', '80115',
        '80116', '80117', '80118', '80119', '80120', '80121', '80201', '80202', '80203', '80204', '80205', '80206', '80207', '80208', '80209', '80210',
        '80211', '80212', '80301', '80302', '80303', '80304', '80305', '80306', '80307', '80308', '80309', '80310', '80311', '80312', '80313', '80314',
        '80401', '80402', '80403', '80404', '80405', '80406', '80407', '90101', '90102', '90103', '90104', '90105', '90106', '90107', '90108', '90109',
        '90110', '90111', '90201', '90202', '90203', '90204', '90205', '90206', '90207', '90208', '90209', '90210', '90211', '90212', '90213', '90214',
        '90215', '90216', '90217', '90218', '90219', '90220', '90221', '100101', '100102', '100103', '100104', '100105', '100106', '100107', '100108', '100109', '100110', '100111', '100112', '100201', '100202', '100203', '100204', '100205', '100206', '100207', '100301', '100302', '100303', '100304', '100305', '100306', '100307', '100308', '100309', '100401', '100402', '100403', '100404', '100405', '100406', '100407', '100408', '100409', '100410', '100501', '100502', '100503', '100504', '110101', '110102', '110103', '110201', '110202', '110301', '110302', '110401', '110402', '110403', '120101', '120102', '120201', '120202', '120203', '120204', '120301', '120302', '120303', '120401', '130101', '130102', '130103', '130201', '130202', '130203', '130204', '130205', '130206', '130207', '130208', '130209', '130210', '130211', '130212', '130213', '130214', '130215', '130216', '130217', '130218', '130219', '130220', '130221', '130222', '130223', '130224', '130225', '130226', '130227', '130228', '130229', '130230', '130231', '130232', '130301', '130302', '130303', '130401', '130402', '130403', '130404', '130501', '130502', '130503', '130504', '130601', '130602', '130603', '130604', '130605', '130606'];

    if (coms.includes(comuna)) {
        return [true, ""];
    }
    return [false, "- Por favor, seleccione una de las comunas del menú.\n"];
}

/* funcion que valida que el sector cumpla con las condiciones pedidas (largo max 100) */
function validar_sector(sector) {
    let aux = sector.length <= 100;
    let mensaje = "";
    if (!aux) {
        mensaje = "- Ingrese un SECTOR de hasta 100 caracteres. (" + sector.length + " caracteres ingresados).\n";
    }
    return [aux, mensaje];
}

/* funcion que valida que el nombre cumpla con las condiciones pedidas (largo max 200) */
function validar_nombre(name) {
    if (name === "") {
        return [false, "- El ingreso de un NOMBRE es OBLIGATORIO.\n"];
    }
    let aux = name.length <= 200;
    let mensaje = "";
    if (!aux) {
        mensaje = "- Ingrese un NOMBRE de hasta 100 caracteres. (" + name.length + " caracteres ingresados).\n";
    }
    return [aux, mensaje];
}

/* funcion que valida que el email cumpla con las condiciones pedidas ======================*/
function validar_email(email) {
    if (email === "") {
        return [false, "- El ingreso de un CORREO ELECTRÓNICO es OBLIGATORIO.\n"];
    }
    let regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if (!regex.test(email)) {
        return [false, "- Ingrese un CORREO ELECTRÓNICO de formato válido. (hola@contacto.com)\n"];
    }

    return [true, ""];
}

/* funcion que valida que el celular sea de chile y empiece con el código de area +56, respetando espacios */
function validar_celular(celular) {
    let regex = /\D*([+56]\d [2-9])(\D)(\d{4})(\D)(\d{4})\D*/;
    if (celular !== "") {
        if (!regex.test(celular)) {
            return [false, "- Ingrese un NÚMERO CELULAR con formato válido. (+56 9 1234 5678)\n"];
        }
    }
    return [true, ""];
}

/* funcion que cuenta cuantas redes sociales se agregaron ============================================*/
function contarRRSS(checkBoxes) {
    let contador = 0;
    let checkBox;
    for (let i = 0; i < checkBoxes.length; i++) {
        checkBox = document.getElementById(checkBoxes[i]);
        if (checkBox.checked === true) {
            contador++;
        }
    }
    return contador;
}

/* funcion que chequea que si una red se selecciona, tenga usuario y del formato válido ===========*/
function tieneUsuario(checkBox, usuario) {
    let red = document.getElementById(checkBox);
    let user;
    if (red.checked === true) {
        user = document.getElementById(usuario).value;
        if (user === "" || user.length < 4 || user.length > 50) {
            return false;
        }
    }
    return true;
}

/* funcion que valida que los contactos dados cumplan con los requisitos =================================*/
function validar_contacto() {
    const checkBoxes = ["whatsapp", "telegram", "twitter", "instagram", "facebook", "tiktok", "otro"];
    const usuarios = ["whatsapp-usuario", "telegram-usuario", "twitter-usuario", "instagram-usuario", "facebook-usuario", "tiktok-usuario", "otro-usuario"];
    let mensaje = "";

    if (contarRRSS(checkBoxes) > 5) {
        mensaje += "- Debe seleccionar MÁXIMO 5 redes sociales de contacto.\n";
    }
    // if (document.getElementById("otro").checked) {
    //     if (document.getElementById("otra-red").value === "") {
    //         mensaje += "- Debe ingresar el nombre de OTRA red social de contacto.\n";
    //     }
    // }
    for (let i = 0; i < checkBoxes.length; i++) {
        if (!tieneUsuario(checkBoxes[i], usuarios[i])) {
            mensaje += "- Debe ingresar un nombre de usuario / URL para el contacto " + checkBoxes[i].toUpperCase() + " de 4 hasta 50 caracteres.\n";
        }
    }
    return [mensaje === "", mensaje];
}

/* funcion que valida que la hora de inicio cumpla con los requisitos y que no sea vacio (OBLIGATORIO) ===========*/
function validar_hora_inicio(inicio) {
    if (inicio === "") {
        return [false, "- El ingreso de HORA DE INICIO es OBLIGATORIO.\n"];
    }

    //let regex = /^(0[1-9]|1\d|2\d|3[01])-(0[1-9]|1\d|2\d|3[01])-(19|20)\d{2}\s+(0[0-9]|1[0-9]|2[0-3]):(0[0-9]|[1-5][0-9])$/;
    let regex = /[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]/;

    if (!regex.test(inicio)) {
        return [false, "- Ingrese una HORA DE INICIO de formato válido. (aaaa-mm-dd hh:mm).\n"];
    }
    return [true, ""];
}

/* funcion que valida que la hora de termino cumpla con los requisitos ============================================ */

function validar_hora_termino(termino, inicio) {
    if (termino === "") {
        return [true, ""];
    }
    //let regex = /^(0[1-9]|1\d|2\d|3[01])-(0[1-9]|1\d|2\d|3[01])-(19|20)\d{2}\s+(0[0-9]|1[0-9]|2[0-3]):(0[0-9]|[1-5][0-9])$/;
    let regex = /[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]/;

    if (!regex.test(termino)) {
        return [false, "- Ingrese una HORA DE INICIO de formato válido. (aaaa-mm-dd hh:mm).\n"];
    }


    let anhot = termino.substring(0, 4)
    let anhoi = inicio.substring(0, 4)
    let montt = termino.substring(5, 7) - 1
    let monti = inicio.substring(5, 7) - 1
    let diat = termino.substring(8, 10)
    let diai = inicio.substring(8, 10)
    let hrt = termino.substring(11, 13)
    let hri = inicio.substring(11, 13)
    let mint = termino.substring(14)
    let mini = inicio.substring(14)

    let d1 = new Date(anhoi, monti, diai, hri, mini)
    let d2 = new Date(anhot, montt, diat, hrt, mint)

    if (d1 >= d2) {
        return [false, "- Ingrese una HORA DE TERMINO posterior a la HORA DE INICIO.\n"]
    }

    return [true, ""];
}

/* funcion que valida la descripcion =============================================================================*/
function validar_descripcion(descripcion) {
    return [true, ""];
}

/* funcion que valida que el tema sea una de las opciones y si es "otro" que cumpla con los requisitos=========== */
function validar_tema(tema) {
    if (tema === ''){
        return [false, "- El ingreso de TEMA es OBLIGATORIO.\n"];
    }
    let regextemas = /^[0-9]*$/gm;
    if (regextemas.test(tema)) {
        return [true, ""];
    }
    if (tema === "otro") {
        nuevo_tema = document.getElementById('nuevo-tema').value;
        if (nuevo_tema.length >= 3 && nuevo_tema.length <= 15) {
            return [true, ""];
        }
        return [false, "- Ingrese un NUEVO TEMA de 3 a 15 caracteres. (" + nuevo_tema.length + " caracteres ingresados).\n"];
    }
    return [false, "- El ingreso de TEMA es OBLIGATORIO.\n"];
}

/* function que valida que se ingrese MINIMO 1 FOTO y que sean de tipo fotos ============================================*/
function validar_fotos(fotos) { //recibe una lista con las fotos

    if (fotos.length > 5) {
        return [false, "- Solo puede ingresar un máximo de 5 imágenes."];
    }

    let foto;
    let filename;
    let extension;
    let allowedExtensionsRegx = /(\.jpg|\.jpeg|\.png)$/i; //regex de las extensiones de imagen permitidas
    let valida;
    let contadorFotos = fotos.length;

    for (let i = 0; i < fotos.length; i++) {
        foto = fotos[i].files;
        if (foto.length === 0) {
            contadorFotos--;
        }
        if (foto.length !== 0) { // si se ingresan fotos, chequeamos su extensión en el nombre
            filename = foto[0].name;  //obtenemos el nombre
            extension = filename.substring(filename.lastIndexOf(".")); // extraemos la extension
            valida = allowedExtensionsRegx.test(extension); // revisamos la extension con regex test
            if (!valida) {
                return [false, "- Por favor, ingrese solo imágenes de tipo válido. (.jpg, .jpeg,  .png) "];
            }
        }
    }
    if (contadorFotos === 0) {
        return [false, "- Por favor, ingrese al menos 1 imagen."];
    }
    return [true, ""];
}

//############## ===========funciones para agregar usuario de los contactos=========== ##############################

function showInput(checkBox, input) {
    // si se selecciona checkbox, pedir usuario/url
    if (checkBox.checked === true) {
        input.style.display = "block";
    } else {
        input.style.display = "none";
    }
}

function agregaUsuarioURL(idCheckBox, idInput) {
    // pedir los elementos por id
    let checkBox = document.getElementById(idCheckBox);
    let input = document.getElementById(idInput);

    showInput(checkBox, input);
}

// ###################### ===========agregar más imágenes ===========  ################################

let contador = 1;

/* Finalmente agregarImagen agrega un nuevo input de file y otro boton de agregar imagen al ser llamada, con un límite de 4.*/
function agregarImagen() {

    let contenedor;

    if (contador < 5) {
        contador += 1;
        contenedor = document.getElementById('contenedor-foto' + contador);
        contenedor.innerHTML += '<input type="file" id="foto-actividad" name="foto-actividad" accept="image/*"><br>';
    } else {
        alert("¡No se pueden agregar más fotos!");
    }
}

/* #####################################3fin del documento #####################################*/