from urllib.request import urlopen
from link_finder import LinkFinder
from general import *


class Spider:
    # declaring class variables for communication between objects as the have same values for all objects
    project_name = ''
    base_url = ''
    domain_name = ''
    page_url = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = project_name + '/queue.txt'
        Spider.crawled_file = project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('first spider', Spider.base_url)

    @staticmethod
    def boot():
        create_project_directory(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_list(Spider.queue_file)
        Spider.crawled = file_to_list(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name, 'crawling', page_url)
            print('Pages in queue:', len(Spider.queue), end='')
            print(' | Crawled pages:', len(Spider.crawled))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        try:
            response = urlopen(page_url)
            html_string = response.read()

            # if response.getheader('Content-Type') == 'text/html':
            #     html_bytes = response.read()
            #     html_string = html_bytes.decode('utf-8')
            html_string = html_string.decode('utf-8')
            finder = LinkFinder(Spider.base_url, page_url)

            finder.feed(html_string)
        except Exception as e:
            print('Error! cannot crawl page>>> Error:', e)
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        list_to_file(Spider.queue, Spider.queue_file)
        list_to_file(Spider.crawled, Spider.crawled_file)
