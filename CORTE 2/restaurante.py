# Karla Maricruz Ruiz Diaz  	203440
# Janeth Alejandra Morales Mendoza  203445

from threading import Thread 
import queue, time
import threading 
import random

#clientes llegando 
bufferRest = queue.Queue(maxsize=20)

#caoacidad del rest
rest = queue.Queue(maxsize=20)
restaurante = queue.Queue(maxsize=20)
mutex = threading.Lock()
#ordenes
bufferOrdenes = queue.Queue()   
#cocinar
bufferCook = queue.Queue()

PERSONAS = 20

cant = float(10)
mesero = int(cant * rest.maxsize/100)
meseros = queue.Queue(maxsize=mesero)

class Persona(threading.Thread):
    def __init__(self, id, monitor):
        threading.Thread.__init__(self)
        self.id= id
        self.monitor = monitor

    def reserva(self):
        #cantidad de recepciones validas
        por = float(20)
        reception = int(por * bufferRest.maxsize/100)
        with self.monitor:
            if not bufferRest.full():
                for x in range(reception):
                    self.monitor.notify()
                    bufferRest.put(self.id)
                    print("Hay una reservacion del cliente"+ str(self.id+1))
                    self.monitor.wait()
                    self.atendiendo()
                    
            else:
                self.atendiendo()
                
        time.sleep(5)
    def espera(self):
        with self.monitor:
            if restaurante.full():
                print("Cliente esperando: "+str(self.id+1))
                self.monitor.notify()
                bufferCook.put(self.id)
                self.monitor.wait()
                if not restaurante.empty():
                    self.ingresar()
            else:
                self.ingresar()   
               
        time.sleep(5)

    def entregar(self):
        with self.monitor:
            while not bufferCook.empty():
                bufferCook.get(self.id)
                self.monitor.notify()
                print(" ✅ Mesero entrega la comida al cliente: "+str(self.id+1))
                restaurante.put(self.id)
                self.comiendo()
           

    def comiendo(self):
        with self.monitor:
            if not bufferCook.full():
                print("Cliente: "+str(self.id+1)+" Esta Comiendo 🍴")
                time.sleep(random.randint(5, 9))
                self.monitor.wait()
                print("Cliente: "+str(self.id+1)+" Termino de Comer 😁")
                restaurante.get(self.id)
                self.ingresar()
                self.monitor.notify()
            else:
              self.espera()  

    
    def cocinar (self):
        with self.monitor:
            while not bufferOrdenes.empty():
                # if not bufferOrdenes.empty():
                    if not bufferCook.full():
                        bufferOrdenes.get(self.id)
                        self.monitor.notify()
                        print("🧑‍🍳 Cocinero prepara la comida del cliente: "+str(self.id+1))
                        time.sleep(4)
                        bufferCook.put(self.id)
                        self.monitor.wait()
                        self.entregar()
                    else:
                        self.ordenar()
                        self.espera()   
        time.sleep(4)

    def ordenar(self):
        cant = float(10)
        mesero = int(cant * rest.maxsize/100)
        meseros = queue.Queue(maxsize=mesero)
        with self.monitor:
            while not rest.empty():
                    if not bufferOrdenes.full():
                        rest.get(self.id)
                        self.monitor.notify()
                        for x in range(meseros.maxsize):
                            print("🧑‍💼 Mesero Tomando Orden del Cliente: "+str(self.id+1))
                            time.sleep(5)
                            bufferOrdenes.put(self.id)
                            self.monitor.wait()
                            self.cocinar()
                    else:
                        self.cocinar() 
                        self.monitor.wait()

    def atendiendo(self):
        
        with self.monitor:
            while  not bufferRest.empty():
                if not rest.full():     
                    bufferRest.get(self.id)
                    print("Atendiendo Cliente:" + str(self.id+1))
                    self.monitor.notify()
                    # time.sleep(5)
                    rest.put(self.id)
                    self.monitor.wait()
                    print("Cliente: " +str(self.id+1)+ " ingreso al restaurante")
                    # time.sleep(5)
                    
                    self.ordenar()
                else:
                    self.reserva()
                    self.ordenar()
            
    
    def ingresar(self):
        with self.monitor:
            if not bufferRest.full():
                self.monitor.notify()
                bufferRest.put(self.id)
                print("Hay un nuevo Cliente: " + str(self.id+1))
                self.monitor.wait()
                self.atendiendo()
                self.reserva()
                    
            else:
                self.espera()
                self.reserva()

    def run(self):
        
        self.ingresar()
        self.reserva()
        self.atendiendo()
        self.ordenar()
        self.cocinar()
        self.entregar()

items_monit = threading.Condition()           
def main():
    personas = []

    for i in range(PERSONAS):
        personas.append(Persona(i,items_monit))

    for p in personas:
        p.start()
    
    for p in personas:
        p.join()



if __name__ == "__main__":
    main()
