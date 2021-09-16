""""
Proyecto  Web Scraping de paginas de arriendo(Mercado Libre)
Pagina oficial: wwww.Mercadolibre.com
Tipo de pagina: Estática
13/08/2021 ----> Inicio del proyecto
20/08/2021----> construcción de metodo apra iterar sobre los articulos de paginas
21/08/2021----< Conectar a una base de datos
Autor:@jeanvitola
ingeniero,analista y estudiante de Ciencia de datos

Objetivo: Aplicar tecnicas de Scraping a la web, Extraer los datos requeridos, limpiar los datos, subirlos a un servidor y mapearlos

NOTA: Se recomienda leer el README.md Aca se establece el codigo  para que los datos escrapeados se almacenen
 en una base de datos ya diseñada

"""
#1 importe de librerias
import pymysql # Esta libreria es necesaria para la conexión de la BBDD con el codigo

"""Módulos"""
#2 Objeto .connnect crea la conexión de los datos del servidor de la BDDD
cnn=pymysql.connect(host='bekzlcrpotaer34put0l-mysql.services.clever-cloud.com',
                             user='ulzxosuwkz3dbda7',
                             password='h0Ur2QByPl6VpPhzpSdP',
                             database='bekzlcrpotaer34put0l',
                             cursorclass=pymysql.cursors.DictCursor)

#3 Función para importar los elementos iterados a la BBDD

def insertar_datos(house) :
    cur=cnn.cursor() # Permite ejecutar la consulta
    sql=("INSERT INTO MercadoLibre (imgUrl, price_house, tittle, address, size, rooms, url) VALUES (%s, %s,%s,%s,%s,%s,%s)") #Query
    param=(house['imgUrl'],house['price_house'],house['tittle'],house['address'],house['size'],house['rooms'],house['url'])  #Query
    cur.execute(sql,param) # ejecuta las consulta de Sql,param
    n=cur.rowcount #Cuantas filas se han afectadas
    cnn.commit()# Guarda las querys ejecutadas
    cur.close()  # Cierra la conexión del cursor
    cnn.close()
    return n
