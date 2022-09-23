from urllib import response
import requests
import threading


def get_service_1(response_json_data):
    print(response_json_data)

def get_error_1():
    print("Error en la solicitud")

def get_service_2(response_json_data):
    print(response_json_data)

def get_error_2():
    print("Error en la solicitud")

def request_data(url, success_callback, error_callback): #Target principal para poder recuperar los datos
    response = requests.get(url)
    if response.status_code == 200:
        success_callback(response.json())
    else:
        error_callback()

class Hilo(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        h1 = threading.Thread(target=request_data, 
        kwargs={'url':'http://3.22.27.8:3000/api/comprador/getAll',
        'success_callback':get_service_1 ,
        'error_callback':get_error_1
        })
        h1.start()

        h2 = threading.Thread(target=request_data,  #Hace un servicio diferente al anterior
        kwargs={'url':'http://3.22.27.8:3000/api/controlEntregas/getAll',
        'success_callback':get_service_2 ,
        'error_callback':get_error_2
        })
        h2.start()

        #Puedo generar servicios diferentes de ser necesario.

hilo = Hilo ()
hilo.start()