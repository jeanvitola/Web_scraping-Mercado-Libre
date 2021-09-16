
#1 Estudiar el comportamiento de los elmentos de las URLS

"""
page 1

composicion:
1--->48 : 48*1

page 2
https://listado.mercadolibre.com.co/inmuebles/arriendo/arriendo-cartagena_Desde_49_PriceRange_1000000-0

49-->96: 48*2

desde 49

page 3
https://listado.mercadolibre.com.co/inmuebles/arriendo/arriendo-cartagena_Desde_97_PriceRange_1000000-0

97-->144: 48*3

page 4
https://listado.mercadolibre.com.co/inmuebles/arriendo/arriendo-cartagena_Desde_145_PriceRange_1000000-0

145-->192 48*4

page 5
https://listado.mercadolibre.com.co/inmuebles/arriendo/arriendo-cartagena_Desde_193_PriceRange_1000000-0

193 -->240: 48*5

Cada 48 elementos
"""

composicion

1) 1
2)1+48*(PageNumber-1)
3)1+48*(PageNumber-1)
4)1+48*(PageNumber-1)
5)1+48*(PageNumber-1)


si quiero ir a la pagina 100
1+48*(PageNumber-1)
PageNumber=)numero de pagina que se quiere acceder
48= Numero de elementos por apginas


def page(page_number):
    initial_range=1+48*(pageNumber-1)
    page_url="https://listado.mercadolibre.com.co/inmuebles/arriendo/"
    page_url=page_url +"arriendo-cartagena_Desde_{}_PriceRange_1000000-0".format(page_number)


def parser(url_parser):
    url=(url_parser)
    r=requests.get(url)
    data=r.text
    soup = BeautifulSoup(data, 'lxml')
    houses= soup.find_all("li",class_="ui-search-layout__item")
