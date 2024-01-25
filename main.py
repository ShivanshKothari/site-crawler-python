import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'PlayStation'
HOMEPAGE = 'https://www.playstation.com/en-in/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 6

queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Create threads
def create_spiders():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a job
def create_jobs():
    for link in file_to_list(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are any items in the queue if so, crawl
def crawl():
    queued_links = file_to_list(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in queue')
        create_jobs()


create_spiders()
crawl()
