# Trabajo para CC5002 Otoño 2022
## Por Valeria Franciscangeli
- vvfranciscangeli@gmail.com
- https://github.com/valfranciscangeli/Tarea_3_DesarrolloWeb.git

En esta carpeta se encuentra la version 'tarea 3' que corresponde a los archivos necesarios para correr la aplicación web de forma local y la version para el servidor anakena que corresponde a todos los archivos que se subieron a anakena para el deploy de la tarea.

A considerar: 
- Las credenciales para la base de datos difieren entre las 2 versiones, al igual que los archivos .sql para crear las bases de datos.
- Para anakena se utilizó la base de datos n.º 79 (cc500279_db).
- Los nombres de las sub carpetas de cada versión son autoexplicativos.
- Para ver el listado de actividades en ambas versiones es necesario que exista al menos 1 actividad guardada previamente en la base de datos. (En el caso local, se sugiere ingresar actividad, fotos y contactos directamente en myphpadmin o ingresar directamente a formulario.py la primera vez).

Novedades:
##### Mapas:
- Esta versión contiene un mapa de Leaflets que muestra marcadores en las comunas donde hay actividades.
- Al pasar el mouse por encima se puede leer la información de cuantas fotos hay subidas de actividades en esa comuna.
- Al hacer clic sobre el marcador se muestra un listado con la información de las actividades guardadas para esa comuna. Solo se muestra tema, dia y hora de inicio, sector e imágenes. 
- Algunas actividades no tienen información de sector pues no es obligatorio, por lo que esa información se verá en blanco.
- Además, se agrega un link "+ info" que lleva a una nueva pestaña donde se puede leer toda la información relacionada con una actividad. 
- Se agrega una característica de geolocalización del usuario para que el centro del mapa se encuentre en su ubicación para que asi pueda revisar más fácilmente las actividades cercanas a él. 
- Normalmente, el navegador pedirá confirmar si se desea compartir la ubicación. De no permitirse, el mapa se centrará en la ubicación de la Facultad de Ciencias Físicas y Matemáticas.
- Los marcadores azules corresponden a actividades, el rojo a la ubicación del usuario y el color oro a la FCFM.
- Al clickear sobre cualquier lugar del mapa se despliega un pop-up con las coordenadas del lugar.

##### Gráficos:
- Para esta versión se agrega a las gráficas (antes con datos fijos) la información obtenida desde la base de datos utilizando AJAX. 
- Se utiliza Chat.js para los 3 tipos de gráficos.
- Si uno de los gráficos no aparece, es probable que se deba a la demora de la petición XHR, por lo que simplemente se debe esperar a que esta se termine de realizar. 
- Los colores del gráfico de torta varían por cada recarga de la página, es decir, los colores de cada tema van cambiando.
- Los gráficos con etiquetas permiten cliquear sobre una o varias de ellas para ocultar la información relacionada sobre el gráfico. Para volver a ver dicha información simplemente volver a cliquear.
- Gracias a las funciones de Chart.js, las gráficas son interactivas, por lo que al pasar el cursor sobre el mapa se puede ver más detalles de los datos.


 Home page en anakena de la tarea 3: https://anakena.dcc.uchile.cl/~vfrancis/cgi-bin/tarea3/
