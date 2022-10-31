# Karla Maricruz Ruiz Diaz
# Janeth Alejandra Morales Mendoza

from threading import Thread 
import queue, time
import threading 
import random

#clientes llegando 
bufferRest = queue.Queue(maxsize=20)
#print(cantrecep.maxsize)

#cantidad de meseros

#print(pormeseros)
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
        #with self.monitor:
        if not bufferRest.full():
            for x in range(reception):
                bufferRest.put(self.id)
                print("Hay una reservacion del cliente"+ str(self.id+1))
                self.atendiendo()
                self.monitor.wait()
        else:
            self.atendiendo()
                # ciclo = False

    def espera(self):
        ciclo = True
        with self.monitor:
            #while not bufferOrdenes.empty():
                # if not bufferOrdenes.empty():
                    if restaurante.full():
                        #bufferOrdenes.get(self.id)
                        print("Cliente esperando: "+str(self.id+1))
                        time.sleep(3)
                       # bufferCook.put(self.id)
                        self.monitor.wait()
                        #self.entregar()
                        if not restaurante.empty():
                            self.ingresar()
                    else:
                        self.ingresar()   
                # else:
                #     self.atendiendo()


    def entregar(self):
        with self.monitor:
            while not bufferCook.empty():
                # if not bufferOrdenes.empty():
                    #if not bufferCook.empty():
                        bufferCook.get(self.id)
                        print("Mesero entrega la comida al cliente: "+str(self.id+1))
                        restaurante.put(self.id)
                        self.comiendo()
                        self.monitor.wait()

    def comiendo(self):
        with self.monitor:
            if not bufferCook.full():
                print("cliente: "+str(self.id+1)+" Esta Comiendo")
                time.sleep(random.randint(2, 6))
                print("cliente: "+str(self.id+1)+" Termino de Comer")
                restaurante.get(self.id)
                self.monitor.wait()
            else:
              self.espera()  

    
    def cocinar (self):
        ciclo = True
        with self.monitor:
            while not bufferOrdenes.empty():
                # if not bufferOrdenes.empty():
                    if not bufferCook.full():
                        bufferOrdenes.get(self.id)
                        print("Cocinero prepara la comida del cliente: "+str(self.id+1))
                        time.sleep(4)
                        bufferCook.put(self.id)
                        self.monitor.wait()
                        self.entregar()
                    else:
                        self.ordenar()
                        self.espera()   
                # else:
                #     self.atendiendo()


    def ordenar(self):
        cant = float(10)
        mesero = int(cant * rest.maxsize/100)
        meseros = queue.Queue(maxsize=mesero)
        ciclo = True
        with self.monitor:
            while not rest.empty():
                # if not rest.empty():
                    if not bufferOrdenes.full():
                        rest.get(self.id)
                        for x in range(meseros.maxsize):
                            print("Mesero Tomando Orden del Cliente: "+str(self.id+1))
                            time.sleep(5)
                            bufferOrdenes.put(self.id)
                            self.monitor.notify()
                            self.cocinar()
                    else:
                        self.cocinar() 
                        # self.monitor.wait()
                # else:
                #     self.atendiendo()
                    # self.monitor.wait()
                    
    def atendiendo(self):
        
        #with self.monitor:
        while  not bufferRest.empty():
            # if not bufferRest.empty():
            if not rest.full():     
                bufferRest.get(self.id)
                print("Atendiendo Cliente:" + str(self.id+1))
                time.sleep(5)
                rest.put(self.id)
                print("Cliente: " +str(self.id+1)+ " ingreso al restaurante")
                time.sleep(5)
                self.ordenar()
                self.monitor.notify()
                    
            else:
                self.reserva()
                self.ordenar()
                        # self.monitor.wait()    
                # else:
                #     self.ingresar()
                #     # self.monitor.wait()
            
    
    def ingresar(self):
        ciclo = True
        #with self.monitor:
            #while not bufferRest.full():
        if not bufferRest.full():
            bufferRest.put(self.id)
            print("Hay un nuevo Cliente: " + str(self.id+1))
            self.atendiendo()
            self.reserva()
                # self.monitor.wait()
                # if      
        else:
            #     self.atendiendo()
            self.espera()
            self.reserva()
            # self.monitor.notify()

    def run(self):
        self.ingresar()
        self.reserva()
        self.atendiendo()
        self.ordenar()
        self.cocinar()
        self.entregar()

items_monit = threading.Condition()           
#person = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
recepcionista = [1]   
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
