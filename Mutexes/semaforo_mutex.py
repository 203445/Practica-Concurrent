from threading import Thread
from turtle import st
import requests
import threading
import time

mutex = threading.Lock() # Crea la variable semáforo

def crito(id,url):
    global x;
    x = x + id
    print("Hilo =" +str(id)+ " =>" + str(x))
    print("ulr = " + str(url))
    x=1
    myfile = requests.get(url)
    open(f'/Users/52961/Documents/semaforo/mutex{id}.jpg.png', 'wb').write(myfile.content)
    init_time = time.time()
    end_time = time.time() - init_time
    print(end_time)

class Hilo(threading.Thread): 
    def __init__(self, id, url):
        threading.Thread.__init__(self)
        self.id=id
        self.url=url

    def run(self):
        mutex.acquire() #Inicializa semáforo , lo adquiere
        crito(self.id, self.url)
        mutex.release() #Libera un semáforo e incrementa la varibale semáforo

threads_semaphore = [
    Hilo(1,'https://www.python.org/static/img/python-logo@2x.png'), 
    Hilo(2,'https://acortar.link/i2qCvN'),Hilo(3,'https://acortar.link/FnRHUU'),
    Hilo(5,'https://acortar.link/xdbrLu'),Hilo(6,'https://acortar.link/VBlNF3'),
    Hilo(7,'https://acortar.link/J0XsB3'), Hilo(8,'https://acortar.link/vC4UTq'),
    Hilo(9,'https://acortar.link/pmHnJV'),Hilo(10,'https://acortar.link/EHBfer')   
]
x=1;
for t in threads_semaphore:
    t.start()
