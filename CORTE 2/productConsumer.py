# Janeth Alejandra Morales Mendoza
# Actividad 01-02
from queue import Queue
import threading
import time

PRODUCTORES = 10
# CONSUMIDORES = 5

bodeguita = Queue(maxsize=10)

def productor():
    while True:
        if not bodeguita.full():
           for i in range(PRODUCTORES):
                bodeguita.put(f"Producto {i}")
                print(f'El productor inserta producto: {i}')
                print(f'Bodega:  {list(bodeguita.queue)}')
                time.sleep(4)
        else:
            time.sleep(4)


def consumidor():
    while True:
        if bodeguita.full():
            while bodeguita.qsize() !=0:
                for i in range(1,5):
                    valorcito = bodeguita.get()
                    print(f'Consumidor consume el producto: {valorcito}')
                    print(f'Bodega Actual: {list(bodeguita.queue)}')
            time.sleep(4)
        else:
            time.sleep(4)


productor = threading.Thread(target=productor)
consumidor = threading.Thread(target=consumidor)

productor.start()
consumidor.start()

