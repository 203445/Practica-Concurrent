

import threading
import time

l1 = threading.Lock()
l2 = threading.Lock()
l3 = threading.Lock()
l4 = threading.Lock()
l5 = threading.Lock()
l6 = threading.Lock()
l7 = threading.Lock()
l8 = threading.Lock()


class Choosing():
    def __init__(self,izquierda,derecha):
        self.izquierda = izquierda
        self.derecha = derecha


p1 = Choosing(l1,l2)
p2 = Choosing(l2,l3)
p3 = Choosing(l3,l4)
p4 = Choosing(l4,l5)
p5 = Choosing(l5,l6)
p6 = Choosing(l6,l7)
p7 = Choosing(l7,l8)
p8 = Choosing(l8,l1)


def runpa(c,nombre):
    dd = c.derecha.acquire()

    if dd:
        c.izquierda.acquire()

        print (nombre, "Obtiene ambos palillos")
        print (f"La {nombre}  empieza a comer") 

    c.izquierda.release()
    c.derecha.release()
    
    print (f"La {nombre}  terminó de comer")
    time.sleep(2)   
    

t1 = threading.Thread(target=runpa,args=(p1,"P1"))
t2 = threading.Thread(target=runpa,args=(p2,"P2"))
t3 = threading.Thread(target=runpa,args=(p3,"P3"))
t4 = threading.Thread(target=runpa,args=(p4,"P4"))
t5 = threading.Thread(target=runpa,args=(p5,"P5"))
t6 = threading.Thread(target=runpa,args=(p6,"P6"))
t7 = threading.Thread(target=runpa,args=(p7,"P7"))
t8 = threading.Thread(target=runpa,args=(p8,"P8"))


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
