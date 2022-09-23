import json
import requests
import time
import psycopg2
import threading
import concurrent.futures

threading_local = threading.local()

# conexion a base de datos
with open("credenciales.json") as archivo_credenciales:
    credenciales = json.load(archivo_credenciales)


def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor: 
        executor.map(get_service,url)


def get_service(url):
    print(url)
    # obtener datos de api  
    data = requests.get(url)
    data = data.json()

    connection_db(data)
   
    #Implementar requests
    # Consumir un servicio que descargue por lo menos 5000 registros

def connection_db(dato):
    try:
        conexionn = psycopg2.connect(**credenciales)
        print("se conectó exitosamente")
    except psycopg2.Error as e:
        print("Ocurrió un error al conectar a PostgreSQL: ", e)

    for x in dato:
        write_db(x['title'],conexionn= conexionn)

    conexionn.close()
    
def write_db(dato, conexionn):
    con = conexionn.cursor()
    basedata = f"INSERT INTO dato (name) VALUES ('{dato}')"        

    if con.execute(basedata) == None:
        conexionn.commit()
    
    # Escribir en response en una base de datos 

if __name__ == "__main__":
    url_site = ["https://jsonplaceholder.typicode.com/photos"]
    init_time = time.time()
    service(url_site)
    end_time = time.time() - init_time
    print(end_time)