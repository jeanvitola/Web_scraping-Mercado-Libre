#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Abrimos el archivo,asignamos las columnas estipuladas
import pandas as pd
from geopy.geocoders import Nominatim

df = pd.read_csv("MercadoLibre.csv")
df
#renombramos el nombre de las columnas
df=df.rename(columns={'https://http2.mlstatic.com/D_NQ_NP_813896-MCO46840303360_072021-C.jpg':'Imagenes','3.500.000':'Precio',"Cartagena Arriendo De Apartamento Castillogrande":"Titulo","Castillogrande, Cartagena De Indias, Bolívar":"Dirección","63 m² cubiertos":"Tamaño","1 hab.":"Habitaciones","https://apartamento.mercadolibre.com.co/MCO-649333001-cartagena-arriendo-de-apartamento-castillogrande-_JM#position=1&search_layout=stack&type=item&tracking_id=0e48f889-011e-4b02-a3a7-569289a48a48":"Url"})
address=df["Dirección"]

address.replace(to_replace= r'Estrato 2 - ',value='', regex=True,inplace=True)
address.replace(to_replace= r'Estrato 3 -',value='', regex=True,inplace=True)
address.replace(to_replace= r'Estrato 3-',value='', regex=True,inplace=True)
address.replace(to_replace= r'Estrato 5 - ',value='', regex=True,inplace=True)
address.replace(to_replace= r'Estrato 4 -',value='', regex=True,inplace=True)
address.replace(to_replace= r'Estrato 4 -',value='', regex=True,inplace=True)
address.replace(to_replace= r'Historica Y Turistica - ',value='', regex=True,inplace=True)
address.replace(to_replace= r'Historica Y Turistica  -',value='', regex=True,inplace=True)
address.replace(to_replace= r'Las Delicias,',value='', regex=True,inplace=True)
address.replace(to_replace= r'3 Avenida 28,',value='', regex=True,inplace=True)
address.replace(to_replace= r'Norte,',value='', regex=True,inplace=True)
address.replace(to_replace= r'Manzanillo 23,',value='', regex=True,inplace=True)
address.replace(to_replace= r'Centro, Popayán, Cauca,',value='Cartagena De Indias, Bolívar', regex=True,inplace=True)
address.replace(to_replace= r'Boca Grande',value='Bocagrande', regex=True,inplace=True)
address.replace(to_replace= r'Manzanillo Del Mar,',value='Morros,', regex=True,inplace=True)
address.replace(to_replace= r'Punta Canoa, ',value='Bocagrande,', regex=True,inplace=True)
address.replace(to_replace= r'Urbana - Estrato 3,  ',value='', regex=True,inplace=True)
address.replace(to_replace= r'Boston, Boston, Cartagena De Indias, Bolívar  ',value='Boston, Cartagena De Indias, Bolívar ', regex=True,inplace=True)
address.replace(to_replace= r'Cielo Mar, ',value='Crespo,', regex=True,inplace=True)
address.replace(to_replace= r'El Cabrero,',value='Cabrero,', regex=True,inplace=True)
address.replace(to_replace= r'Urbana - Estrato 3, ',value='', regex=True,inplace=True)
address.replace(to_replace= r'Zona Industrial - Mamonal,',value='Mamonal,', regex=True,inplace=True)
address.replace(to_replace= r'Olaya Sector Tesca Nuevo, ',value='Olaya,', regex=True,inplace=True)
address.replace(to_replace= r'Zona  Cartagena De Indias, Bolívar, ',value='Cartagena De Indias, Bolívar,', regex=True,inplace=True)
address.replace(to_replace= r'San Diego - Centro Histórico',value='centro historico,', regex=True,inplace=True)
address.replace(to_replace= r'El Toril,',value='', regex=True,inplace=True)
address.replace(to_replace= r'El Rubí,',value='', regex=True,inplace=True)
address.replace(to_replace= r'Chino,',value='', regex=True,inplace=True)


def location_py(address):
    geolocator = Nominatim(user_agent="jeanvitola")
    location = geolocator.geocode(address)
    print((location.latitude, location.longitude))

    
    
LonLati=[]

for i in address:
    select=i
    
    try:
        location_py(select)
             
    except:
        pass





# In[ ]:




