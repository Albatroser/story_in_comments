import vk_api
from time import strftime, localtime, sleep
from datetime import timedelta
from queue import Queue
from glue.models import Community
import threading
from celery.decorators import periodic_task

@periodic_task(run_every=timedelta(seconds=7))
def start_workers():
    num_fetch_threads = 1
    fetch_queue = Queue()

    for i in range(num_fetch_threads):
        worker = threading.Thread(
            target=scan_wall,
            args=(fetch_queue,),
            name='worker-{}'.format(i),
        )
        worker.setDaemon(True)
        worker.start()

    for community in Community.objects.all():
        fetch_queue.put(community)

    fetch_queue.join()

def scan_wall(queue):
    while True:
        community = queue.get()
        url = community.vk_domen
        session = vk_api.VkApi()
        session.authorization()
        api = session.get_api()
        response = api.wall.get(owner_id=-url, extended=1)

        name = response['groups'][0]['name']
        for i in range(0, len(response)):
            try:
                text = response['items'][i]['text']
                if text == community.post.text:
                    post_id = response['items'][i]['id']
                    community.is_posted = True
                    community.vk_id_real = post_id
                    community.save()
                    print (post_id)
            except IndexError:
                pass
            except TypeError:
                print ('TypeError')
                return
        print ('-------------------------------ready---------------------------')
        queue.task_done()
