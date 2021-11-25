# <center>Analizar arriendos de apartamentos/casas y edificios en Mercado libre</center>

****
<img src="https://logodownload.org/wp-content/uploads/2018/10/mercado-libre-logo-2.png" alt="JuveR" width="300px">

******

> Creo que los animales ven en el hombre un ser igual a ellos que ha perdido de forma extraordinariamente peligrosa el sano intelecto animal.

> Es decir, que ven en él al animal irracional, al animal que ríe, al animal que llora, al animal infeliz. — Friedrich Nietzsche




<p style="text-align: justify;">El internet ha abierto las puertas y a dado acceso a que todo el mundo pueda vender, comprar y arrendar un inmueble con un simple click. Si bien eso es una gran oportunidad tanto para compradores como vendedores al hacer mejores negocios gracias a la enorme difusión que pueden llegar a tener sus productos en el internet.

Sin embargo muchas veces entre tanta oferta disponible en el mercado, se hace un poco tedioso encontrar la mejor opción de lo que estamos buscando. En mi caso, estaba buscando departamentos en cartagena de indias para arrendar, pero me di cuenta que hay muchas ofertas y eso me hace no poder decidir cual de todas escoger!!. Asi que se me ocurrió una forma de poder acceder a todas estas ofertas de arriendos, compararlas y visualizarlas de una manera más sencilla, para que me pudiera ayudar a encontrar la que más se adapta a mis necesidades, así que sin más rodeos vamos a la acción.

La idea es realizar un web scraping, el cual es un proceso de extraer información de sitios web dinamicos o estaticos de manera automatica. El sitio web de preferencia fue mercado libre Finalmente con la información obtenida creé una base de datos para visualizar la información con otras herramientas de mapeo.

</p>


****
****
****
****

# Requerimientos

Librerias a utilizar :
* BeautifulSoup
* Pandas
* Numpy
* Requests
* PyMySQL
* Math

*********
*******
*****




## 1) Obteniendos los datos de los Arriendos

El proceso de Web Scraping consiste en obtener información de una pagina web de manera automatizada, esta información se puede guardar en la manera que se desee, en mi caso quiero obtener la información de los arriendos de departamentos ofertados, pero siendo más especifico me interesan las siguientes caracteristica


* Imagen
* Precio
* Titulo
* Direccion
* Tamaño
* Habitaciones
* Url

Estas caracteristicas corresponderán a las columnas de mi Data Frame. Así sin más utilizando la libreria Requests, y Beautiful Soup de Python realicé el Web Scraping a la Pagina Web

De manera general el trabajo que hace el Script es extraer el codigo html de la pagina web y la almacena en una variable, con esta variable podemos ir navegando dentro del codigo html y encontrar los tags donde se almacenan los items que contienen la información objetivo. Esta información se guarda como texto en las listas de Python declaradas como nuevas variables y realizando una serie de bucles, se extrae la información de cada item, por cada pagina.

Para automatizar todo el proceso anterior definí una función llamada `def obj_house` a la cual se le debe pasar como argumento la URL(objeto Soup) a parsear que se desea consultar . Esta función devuelve listas con la información de las caracteristicas explicadas arriba (precio,metros cuadrados, baños, habitaciones, dirección y URL)

****
***
***
**

##  2) Subir los Archivos a una BBDD (PyMysql)

La idea del web scraping es que se puedan obtener todos los elementos que se requieren y a su vez se tenga disponibilidad en alguna base de datos, por ende se utiliza la librería PyMysql para crear los objetos y las conexiones, con el fin de que el DataFrame creado se suba correctamente.

`import pymysql.cursors`

Servidor de BBDD: `https://www.clever-cloud.com/en/`

<img src="https://i.ibb.co/H4Pnytw/Scrap.png" alt="JuveR" width="px">


********
*******
******
****


##  3) Limpiar el DataFrame(PyMysql)

Muchas veces suele suceder que las personas no escriben la información completa sobre lo que están ofreciendo en la web, o tal vez debido a errores de tipeos, la información no se llena adecuadamente en cada categoria. Debido a esto es necesario realizar una limpieza a los datos, eliminando las variables que no aporten información, y modificando algunos tipos de datos para que puedan ser procesados posteriormente por Tableau/myMaps de Google.

A modo general, para la limpieza de estos datos, elimine el texto adicional de las variables numericas como Cantidad de Baños, Dormitorios, Precios y Metros Cuadrados. Tambien cambie el tipo de dato a numerico (Interger) ya que toda la información extraida de internet se almacena en texto (String).

Finalmente debido a los errores de tipeo de algunos usuarios al escribir el precio de arriendo de los departamentos, consideré los valores que estuvieran en un rango de $1.000.000 COP en adelante.

*********
********
******
##  4) Direcciones y Coordenadas Geograficas de Arriendos

Uno de los motivos que más me interesaba al realizar este proyecto, fue el poder ver de manera global en un mapa de Santiago donde se encuentra cada uno de departamentos en arriendo que se ofrecen en la pagina web.

Para poder realizar esto, tuve que obtener las coordenadas geograficas de las direcciones de mi Data Frame,con una libreria que se llama geopy, a la cual se le pasa una dirección y devuelve las coordenadas.

las información dada por Geopy Latidud/Longitud se utiliza mas cuadno trabajamos con visualizaciones mas avanzado como klepper.gl, Tableau...etc

Para el uso práctico se utilizo Google myMaps


<img src="https://i.ibb.co/SNskWpN/maps.png" alt="JuveR" width="800px">



<iframe src="https://www.google.com/maps/d/u/0/embed?mid=1bvytQ79gIIoZfDjx7J_2v0RIRzGbyogB" width="640" height="480"></iframe>
