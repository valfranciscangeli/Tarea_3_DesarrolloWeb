import hashlib
import sys

import mysql.connector

class DB:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def get_temaID(self, tema):
        sql = f'''
           SELECT id FROM tema WHERE nombre='{tema}';
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def guardar_tema(self, tema):
        sql = f'''
           INSERT INTO tema (nombre) VALUES ('{tema}');
            '''
        self.cursor.execute(sql)
        self.db.commit()

    def guardar_contacto(self, contacto_info):
        # nombre, identificador, id_actividad
        sql = '''
                INSERT INTO contactar_por (nombre, identificador, actividad_id) VALUES (%s, %s, %s);
             '''
        self.cursor.execute(sql, contacto_info)
        #self.db.commit()

    def guardar_actividad(self, actividad):
        # recibe un diccionario
        """
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
        """

        sql = '''
                INSERT INTO actividad (comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion, tema_id) VALUES 
                (%s, %s, %s,%s, %s, %s, %s, %s, %s);
                '''

        valores = (actividad['comuna'],
                   actividad['sector'],
                   actividad['nombre'],
                   actividad['email'],
                   actividad['celular'],
                   actividad['inicio'],
                   actividad['termino'],
                   actividad['descripcion'],
                   actividad['tema'])
        self.cursor.execute(sql, valores)  # ejecuta la consulta
        #self.db.commit()
        id_actividad = self.cursor.getlastrowid()
        return id_actividad

        # =============================================================

    def save_data(self, data):
        """
            vamos a ignorar problemas de que se guarde la actividad por partes 
        """

        # data = (actividad, redes_sociales, tabla_fotos)

        actividad = data[0]

        redes_sociales = data[1]
        """
        #                 nombre      identificador
        redes_sociales = {'whatsapp': wspUser,
                        'telegram': tlgUser,
                        'twitter': twUser,
                        'instagram': igUser,
                        'facebook': fbUser,
                        'tiktok': tkUser,
                        'otraRed': otraRed, 
                        'otroUser': otroUser
                        }
        """

        fotos = data[2]
        """
        fotos = [foto1, ... , fotoN]
        """

        try:
            # ====================
            # guardar actividad
            # ====================
            id_actividad = self.guardar_actividad(actividad)  # guarda la actividad y recupera el id

            # #====================
            # # guardar contactos
            # #====================

            # whatsapp
            if redes_sociales['whatsapp'] != '':
                whatsapp = ('whatsapp', redes_sociales['whatsapp'], id_actividad)
                self.guardar_contacto(whatsapp)

            # #telegram
            if redes_sociales['telegram'] != '':
                telegram = ('telegram', redes_sociales['telegram'], id_actividad)
                self.guardar_contacto(telegram)

            # #twitter
            if redes_sociales['twitter'] != '':
                twitter = ('twitter', redes_sociales['twitter'], id_actividad)
                self.guardar_contacto(twitter)

            # #instagram
            if redes_sociales['instagram'] != '':
                instagram = ('instagram', redes_sociales['instagram'], id_actividad)
                self.guardar_contacto(instagram)

            # #facebook
            if redes_sociales['facebook'] != '':
                facebook = ('facebook', redes_sociales['facebook'], id_actividad)
                self.guardar_contacto(facebook)

            # #tiktok
            if redes_sociales['tiktok'] != '':
                tiktok = ('tiktok', redes_sociales['tiktok'], id_actividad)
                self.guardar_contacto(tiktok)

            # otra
            if redes_sociales['otroUser'] != '':
                otro = ('otra', redes_sociales['otroUser'], id_actividad)
                self.guardar_contacto(otro)

            # #====================
            # # guardar las fotos
            # #====================            
            for foto in fotos:
                # Procesar archivo
                fileobj = foto
                filename = fileobj.filename

                # Cuenta los archivos que hay en la base de datos
                sql = "SELECT COUNT(id) FROM foto;"
                self.cursor.execute(sql)
                total = self.cursor.fetchall()[0][0] + 1
                filename_hash = hashlib.sha256(filename.encode()).hexdigest()[
                                0:30]  # aplica función de hash
                # concatena la función de hash con el número total de archivos, nombre único
                filename_hash += f"_{total}"
                # OJO: lo anterior puede ser peligroso en el caso en que se tenga un servidor que ejecute peticiones en
                # paralelo. Lo que se conoce como un datarace. Nuestro servidor ejecuta sus procesos de forma secuencial,
                # no worries.

                # guarda el archivo localmente
                open(f"media/{filename_hash}", "wb").write(fileobj.file.read())
                sql_file = '''
                            INSERT INTO foto (ruta_archivo, nombre_archivo, actividad_id) 
                            VALUES (%s, %s, %s)
                            '''
                self.cursor.execute(sql_file, (
                    filename_hash, filename, id_actividad))  # ejecuta la query que guarda el archivo en base de datos

            # ==================================================
            self.db.commit()  # modifico la base de datos

        except:
            print("ERROR AL GUARDAR EN LA BASE DE DATOS")
            sys.exit()

        # =============================================================

    def get_data_portada(self):
        sql = '''
           SELECT AC.id, CO.nombre, AC.sector, AC.nombre, AC.email, AC.celular, AC.dia_hora_inicio, AC.dia_hora_termino, AC.descripcion, TE.nombre FROM actividad AC, comuna CO, tema TE WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id ORDER BY id DESC LIMIT 5;
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_data_listado(self, inicio):
        sql = f'''
            SELECT AC.id, CO.nombre, AC.sector, AC.nombre, AC.email, AC.celular, AC.dia_hora_inicio, AC.dia_hora_termino, AC.descripcion, TE.nombre FROM actividad AC, comuna CO, tema TE WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id ORDER BY id DESC LIMIT {inicio}, 5;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def get_todas_actividades(self):
        sql = f'''
            SELECT AC.id, CO.nombre, AC.sector, AC.nombre, AC.email, AC.celular, AC.dia_hora_inicio, AC.dia_hora_termino, AC.descripcion, TE.nombre FROM actividad AC, comuna CO, tema TE WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id ORDER BY id DESC;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_temas(self):
        sql = '''
            SELECT id, nombre FROM `tema` ORDER BY nombre ASC;
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_fotos(self, id_actividad):
        sql = f'''
            SELECT id, ruta_archivo, nombre_archivo, actividad_id FROM foto WHERE actividad_id={id_actividad};
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def contar_fotos(self, id_actividad):
        sql = f'''
            SELECT COUNT(id) FROM foto WHERE actividad_id={id_actividad};
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def contar_actividades(self):
        sql = f'''
            SELECT COUNT(id) FROM `actividad`;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_contacto(self, id_actividad):
        sql = f'''
            SELECT id, nombre, identificador, actividad_id FROM contactar_por WHERE actividad_id={id_actividad} ORDER BY nombre ASC;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_region(self, comuna):
        sql = f'''
            SELECT nombre FROM region WHERE id=(SELECT region_id FROM comuna WHERE nombre="{comuna}");
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def get_regiones(self):
        sql = '''
            SELECT id, nombre FROM `region` ORDER BY id ASC;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_comunas(self, region_id):
        sql = f'''
            SELECT id, nombre FROM `comuna` WHERE region_id={region_id} ORDER BY id ASC;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_comunas2(self, region_id):
        sql = f'''
            SELECT * FROM `comuna` WHERE region_id={region_id} ORDER BY region_id, nombre ASC;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_comuna3(self):
        sql = '''
            SELECT id FROM `comuna`ORDER BY id ASC;
        '''
        self.cursor.execute(sql)
        comunas = self.cursor.fetchall()
        arreglo = []
        
        for comuna in comunas:
            arreglo.append(comuna[0])
        return arreglo
    
    def get_cantidad_imagenes_por_comuna_id(self, comuna_id):
        sql = f'''
            SELECT COUNT(foto.id) from foto, actividad WHERE actividad.id=foto.actividad_id AND actividad.comuna_id={comuna_id};
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def get_comuna_por_nombre(self, nombre):
        sql = f'''
                    SELECT id from comuna WHERE nombre='{nombre}';
                '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]
    
    def get_id_actividades_comuna(self, comuna):
        sql = f'''
                    SELECT id from actividad WHERE comuna_id={comuna} ORDER BY dia_hora_inicio DESC;
                '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_info_actividad_mapa(self, actividad):
        sql = f'''
            SELECT TE.nombre, AC.dia_hora_inicio, AC.sector FROM actividad AC, tema TE WHERE AC.id={actividad} AND AC.tema_id=TE.id;
             '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_actividades_por_dia(self):
        sql = '''
            SELECT COUNT(actividad.id) cantidad, DATE(dia_hora_inicio) dia FROM `actividad` GROUP BY DATE(dia_hora_inicio) ORDER BY dia_hora_inicio ASC;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_actividades_por_tema(self):
        sql = '''
            SELECT COUNT(actividad.id) cantidad, tema_id tm FROM `actividad` GROUP BY tema_id ORDER BY tema_id ASC;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_actividades_por_hora(self):
        sql = '''
SELECT COUNT(actividad.id) cantidad, MONTH(dia_hora_inicio) mes, HOUR(dia_hora_inicio) hora FROM `actividad` GROUP BY MONTH(dia_hora_inicio), HOUR(dia_hora_inicio) ORDER BY mes, hora ASC;                '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

