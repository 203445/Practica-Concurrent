
import requests
import threading 
import json
import psycopg2
# import concurrent.futures
import pytube 

with open("credenciales.json") as archivo_credenciales:
    credenciales = json.load(archivo_credenciales)

def get_services():
#    print(f'Data input = {x}')
#    time.sleep(100)
    
    for _ in range(0,50): 
        response = requests.get('https://randomuser.me/api/')
        if response.status_code == 200:
            results = response.json().get('results')
            name = results[0].get('name').get('first')
            print(name)

def get_video():
    url = ["https://www.youtube.com/watch?v=izGwDsrQ1eQ",
    "https://www.youtube.com/watch?v=8UVNT4wvIGY",
    "https://www.youtube.com/watch?v=djV11Xbc914",
    "https://www.youtube.com/watch?v=e-fA-gBCkj0",
    "https://www.youtube.com/watch?v=nPvuNsRccVw"]
    for i in url:
        get_yt = pytube.YouTube(i)
        get_yt.streams.get_highest_resolution().download("/Users/52961/Documents/descarga2")


def get_data():
    data = requests.get("https://jsonplaceholder.typicode.com/photos?_start=0&_limit=2000")
    data = data.json()

    try:
        conexionn = psycopg2.connect(**credenciales)
        print("se conectó exitosamente")
    except psycopg2.Error as e:
        print("Ocurrió un error al conectar a PostgreSQL: ", e)

    con = conexionn.cursor()

    for x in data:
        dato = x['title']
        basedata = f"INSERT INTO datos2 (name) VALUES ('{dato}')"   
        if con.execute(basedata) == None:
            conexionn.commit()

    conexionn.close()

if __name__ == '__main__':
           
    th1 = threading.Thread(target=get_services)
    th2 = threading.Thread(target=get_video)
    th3 = threading.Thread(target=get_data)
    th1.start()
    th2.start()
    th3.start()
    #    get_services()

# 1. Descargar 5 Videos 
# 2. Escribir en base de datos por lo menos 2000 registros
# 3. Generar una solicitud de por lo menos 50 usuarios.  