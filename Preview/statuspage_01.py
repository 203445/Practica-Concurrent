
import time
from threading import Thread
import requests


def url_ok(url):

    r = requests.head(url)
    if  r.status_code != 200:
        print('URL '+ str(url) + ' Página inactiva   ' +str(r.status_code) + '     La solicitud no puede procesarse de manera correcta') 
    else:
        print('URL '+ str(url) + ' Página activa    ' +str(r.status_code))    
    # return r.status_code == 200


class Hilo(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url

    def run(self):
       url_ok(self.url)


t1 = [
    Hilo('https://www.facebook.com/'), Hilo('https://www.canva.com/es_419/'),
    Hilo('https://www.google.com'), Hilo('https://wordpress.org/'), Hilo('https://www.figma.com/'),
    Hilo('https://www.walmart.com.mx/'), Hilo('https://www.amazon.com.mx/'), Hilo('https://trello.com/'), 
    Hilo('https://www.youtube.com/'), Hilo('https://www.netflix.com/mx/'), Hilo('https://www.disneyplus.com/es-mx'), 
    Hilo('https://open.spotify.com/'), Hilo('https://cinepolis.com/'), Hilo('https://www.nike.com/mx/'), 
    Hilo('https://www.suburbia.com.mx/tienda/home'), Hilo('https://web.telegram.org/'), Hilo('https://discord.com/'), 
    Hilo('https://www.jetbrains.com/idea/'), Hilo('https://code.visualstudio.com/'), Hilo('https://web.whatsapp.com/'), 
    Hilo('https://www.raspberrypi.com/software/'), Hilo('https://twitter.com/'), Hilo('https://www.tiktok.com/es'),
    Hilo('https://www.tinkercad.com/'), Hilo('https://classroom.google.com/')
]

while True:
    for i in t1:
        i.start()
    time.sleep(240) 
