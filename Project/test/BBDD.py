
import pymysql.cursors


def get_bd_connection():
    connection_db=pymysql.connect(host='b5c9b456f5h3lvyq8qcr-mysql.services.clever-cloud.com',
                             user='uvko6tpdub18qp8v',
                             password='tWMZ9k5skV8UvfaGAgPs',
                             database='b5c9b456f5h3lvyq8qcr',
                             cursorclass=pymysql.cursors.DictCursor)
    return connection_db

def query_execute(query,param=""):
    bd_con=get_bd_connection()
    db_cursor= bd_con.cursor()
    if(param == ""):
        db_cursor.execute(query)
    else:
        db_cursor.execute(query,param)
        db_cursor.close()
        bd_con.commit()
        bd_con.close()
        return 1

def insert_house(house):
    query_for_insert_house=("INSERT INTO MercadoLibre (imgUrl, price_house, title, address, size, rooms, url) VALUES (%s, %s,%s,%s,%s,%s,%s)")
    param=(house['imgUrl'],house['price_house'],house['title'],house['address'],house['size'],house['rooms'],house['url'])
    query_execute(query_for_insert_house,param)
    return 1
