import pytube 
import time
import threading
import concurrent.futures

threading_local = threading.local()

def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor: 
        executor.map(get_service,url)

def get_service(url):
    get_yt = pytube.YouTube(url)
    get_yt.streams.get_highest_resolution().download("/Users/52961/Documents/Descarga")


if __name__ == "__main__":
    url_site = ["https://www.youtube.com/watch?v=izGwDsrQ1eQ","https://www.youtube.com/watch?v=8UVNT4wvIGY",
    "https://www.youtube.com/watch?v=djV11Xbc914","https://www.youtube.com/watch?v=e-fA-gBCkj0","https://www.youtube.com/watch?v=nPvuNsRccVw"]
    init_time = time.time()
    service(url_site)
    end_time = time.time() - init_time
    print(end_time)