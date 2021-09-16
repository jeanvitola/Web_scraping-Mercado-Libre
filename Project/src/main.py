""""
Proyecto  Web Scraping de páginas de arriendo(Mercado Libre)
13/08/2021
Autor:@jeanvitola
ingeniero, analista y estudiante de Ciencia de datos

Objetivo: Aplicar técnicas de Scraping a la web, Extraer los datos requeridos, limpiar los datos, subirlos a un servidor y mapearlos

NOTA: Se recomienda leer el README.md
"""

#1)Importar módulos y librerías
import requests
from bs4 import BeautifulSoup
import math
import DAO2

#---------------------------------------------------------------
#2 Identificación de la URL y petición GET

url =("https://listado.mercadolibre.com.co/inmuebles/arriendo/arriendo-cartagena_PriceRange_1000000-0#applied_filter_id%3Dprice%26applied_filter_name%3DPrecio%26applied_filter_order%3D3%26applied_value_id%3D1000000-*%26applied_value_name%3Dnull1000000-null*%26applied_value_order%3D4%26applied_value_results%3DUNKNOWN_RESULTS%26is_custom%3Dtrue")
r  = requests.get(url)
data = r.text

#---------------------------------------------------------------
#3)Convertir en  un objeto Soup
soup = BeautifulSoup(data, 'lxml')

#---------------------------------------------------------------
#4) identificamos los elementos li en este caso
houses= soup.find_all("li",class_="ui-search-layout__item")


#---------------------------------------------------------------
#5) Esta función permite iterar sobre todos los elementos de la pagina

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

#---------------------------------------------------------------
#6) Esta función permite iterar sobre las páginas que componen la búsqueda

def page(pageNumber):
    initial_range= 1 + 48 * (pageNumber-1)
    page_url="https://listado.mercadolibre.com.co/inmuebles/arriendo/"
    page_url= page_url +"arriendo-cartagena_Desde_{}_PriceRange_1000000-0".format(initial_range)
    return page_url            #codigo ok

def scrap_url(urls):
    url=(urls)
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')
    houses= soup.find_all("li",class_="ui-search-layout__item")
    for house_html in houses:
        object=obj_house(house_html)
        DAO2.insert_house(object)

#---------------------------------------------------------------
#7) Obtenemos  la cantidad de elementos  y la cantidad redondeada de páginas a escrapear
houses_amount=float(soup.find(class_="ui-search-search-result__quantity-results").text.split(" ")[0].replace(".","")) #obtener la cantidad de Articulos
page_amount=math.ceil(houses_amount/48)


"""Declaramos la iteración para la función"""
for i in range(1,page_amount+1):
    url_page=page(i)
    jean=scrap_url(url_page)
    print(jean)
