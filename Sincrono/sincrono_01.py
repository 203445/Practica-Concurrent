import json
import requests
import time
import psycopg2


# conexion a base de datos
with open("credenciales.json") as archivo_credenciales:
    credenciales = json.load(archivo_credenciales)

try:
    conexionn = psycopg2.connect(**credenciales)
    print("se conectó exitosamente")
except psycopg2.Error as e:
    print("Ocurrió un error al conectar a PostgreSQL: ", e)


# Investigar libreria threading

def get_service():
  
    # obtener datos de api  
    data = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
    
    data = data.json()

    for x in data["results"]:
        write_db(x['name'])
        
        # print("conexion cerrada")
    conexionn.close()
    #Implementar requests
    # Consumir un servicio que descargue por lo menos 5000 registros


def write_db(dato):
   
    con = conexionn.cursor()
    print(dato)
    basedata = f"INSERT INTO dato (name) VALUES ('{dato}')"        

    if con.execute(basedata) == None:
        conexionn.commit()
        

    # Escribir en response en una base de datos 

if __name__ == "__main__":
    init_time = time.time()
    get_service()
    end_time = time.time() - init_time
    print(end_time)