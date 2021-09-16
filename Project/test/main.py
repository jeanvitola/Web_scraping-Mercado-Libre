""""
Proyecto  Web Scraping de paginas de arriendo(Mercado Libre)
13/08/2021
Autor:@jeanvitola
ingeniero,analista y estudiante de Ciencia de datos


Objetivo: Aplicar tecnicas de Scraping a la web, Extraer los datos requeridos, limpiar los datos, subirlos a un servidor y mapearlos

NOTA: Se recomienda leer el README.md
"""
#1)importe de librerias
import requests
from bs4 import BeautifulSoup

#2) Petición HTTP :contrucción de la peticion GET
url=("https://listado.mercadolibre.com.co/inmuebles/arriendo/arriendo-cartagena_PriceRange_1000000-0#applied_filter_id%3Dprice%26applied_filter_name%3DPrecio%26applied_filter_order%3D3%26applied_value_id%3D1000000-*%26applied_value_name%3Dnull1000000-null*%26applied_value_order%3D4%26applied_value_results%3DUNKNOWN_RESULTS%26is_custom%3Dtrue")
request=requests.get(url)
#print(request) # La conexión tiene que dar un objeto response <Response [200]> para indicar que es exitosa
data=request.text
#print(data)  #imprime toda la estructura de la pagina en cadena de texto

#3) creamos un objeto BeaufiulSoup, el cual transforma el contenido de HTML en una estructura de arbol fácil de leer e interpretar
soup = BeautifulSoup(data, 'lxml')  #Este objeto creado nos permite aplicar las funciones de BS4
#print(bsObj)

#4) en el README.md se detalla cuales son las caracteristicas de los datos que se quieren obtener
#por lo cual vamos iterando desde el navegador apra ver donde se encuentra la estructura de cada variable

#5 Identificamos los elementos Li dentro del objeto de Bs4 creado "bsObj"

houses= soup.find_all("li",class_="ui-search-layout__item")

#tratamos de obtener un primer objeto apra identificar los tags relevantes
firts_houses=houses[0]
#print(firts_houses)

#6) indentificamos las imagenes
imgUrl=firts_houses.find("img")["data-src"]
#print(imgUrl)

#7) identificamos el precio
price_house=firts_houses.find(class_="price-tag-fraction").text
#print(price_house)

#8 identificamos el titulo de la publicación
title=firts_houses.find( class_="ui-search-item__title").text
#print(title)

#9 identificamos la dirección de la casa/apartamento/edificio
address=firts_houses.find( class_="ui-search-item__group__element ui-search-item__location").text
#print(title)

#10 calculamos  la cantidad de habitaciones y el tamaño de la casa/apartamento/edificio
#Notamos cuando inspeccionamos los tags que la cantidad de habitaciones y el tamaño se encuentran en el mismo tag
#por ende al momento de llamarlos puede que se excluya algun dato o salga error, etonces:
all_atribute= firts_houses.find_all("li",class_="ui-search-card-attributes__attribute")
size=all_atribute[0].text #indice del primer elemento correponde al tamaño
rooms=""
if (len(all_atribute)>1):
    rooms= all_atribute[1].text

#11 obtenemos la URL dela publicaciónb
url=firts_houses.find("a")["href"]


""" ETAPA #2

Hasta acá hemos obtenido lo elementos para un elemento de toda la apgina, lo que queremos
en realidad es iterar sobre toda la pagina y hacer un scrapeo horizonal, entonces armamos una función
para recorrer todos lo elementos """


def obj_house(house_html):
    imgUrl=house_html.find("img")["data-src"]
    price_house=house_html.find(class_="price-tag-fraction").text
    title=house_html.find( class_="ui-search-item__title").text
    address=house_html.find( class_="ui-search-item__group__element ui-search-item__location").text
    all_atribute= house_html.find_all("li",class_="ui-search-card-attributes__attribute")
    size=all_atribute[0].text
    rooms=""
    if (len(all_atribute)>1):
        rooms= all_atribute[1].text
    url= house_html.find("a")["href"]
    return {"imgUrl":imgUrl,"price_house":price_house,"title":title,"address": address ,"size":size,"rooms":rooms,"url":url }    #codigo ok


#12 La siguiente función impoorta el modelo BBDD donde se creo la BBDD
#itera sobre los elementos de la pagina y los sube
for i in houses:
    houses_ml=obj_house(i)
    BBDD.insert_house(houses_ml)
