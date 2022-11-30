
import time 
import requests



def url_ok(url_site,timeout):

    r = requests.head(url_site,timeout=timeout)
    if  r.status_code != 200:
        print("URL "+ str(i) + " Página inactiva   " +str(r.status_code) + "     La solicitud no puede procesarse de manera correcta") 
    else:
        print("URL "+ str(i) + " Página activa    " +str(r.status_code))    
    return r.status_code == 200

 

if __name__ == "__main__":
    url_site = ["https://www.facebook.com/","https://www.canva.com/es_419/",
    "https://www.google.com","https://wordpress.org/",
    "https://www.figma.com/","https://www.walmart.com.mx/",
    "https://www.amazon.com.mx/","https://trello.com/", "https://www.youtube.com/","https://www.netflix.com/mx/",
    "https://www.disneyplus.com/es-mx","https://open.spotify.com/",
    "https://cinepolis.com/","https://www.nike.com/mx/",
    "https://www.suburbia.com.mx/tienda/home","https://web.telegram.org/",
    "https://discord.com/","https://www.jetbrains.com/idea/",
    "https://code.visualstudio.com/","https://web.whatsapp.com/",
    "https://www.raspberrypi.com/software/","https://twitter.com/",
    "https://www.tiktok.com/es","https://www.tinkercad.com/", "https://classroom.google.com/"]

    while True:
        for i in url_site:
            url_ok(i,timeout=5)
        time.sleep(240)        