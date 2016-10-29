import vk_api
from time import strftime, localtime, sleep
from threading import Thread
from datetime import timedelta
from queue import Queue
import threading
from celery.decorators import periodic_task

@periodic_task(run_every=timedelta(seconds=2))
def start_workers():
    num_fetch_threads = 2
    fetch_queue = Queue()

    for i in range(num_fetch_threads):
        worker = threading.Thread(
            target=scan_wall,
            args=(fetch_queue,),
            name='worker-{}'.format(i),
        )
        worker.setDaemon(True)
        worker.start()

    fetch_queue.put('hackrussia2016')
    fetch_queue.put('spb_vape')
    fetch_queue.put('vape_baraholka_piter')
    fetch_queue.put('zapvaper')
    fetch_queue.join()

def scan_wall(queue):
    while True:
        url = queue.get()
        session = vk_api.VkApi()
        session.authorization()
        api = session.get_api()
        response = api.wall.get(domain=url, extended=1)

        name = response['groups'][0]['name']
        for i in range(1, len(response)):
            try:
                text = response['items'][i]['text']
                post_id = response['items'][i]['id']
                print (post_id)
            except IndexError:
                pass
            except TypeError:
                print ('TypeError')
                return
        print ('ready')
