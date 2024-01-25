import os


# creates a directory for the project
def create_project_directory(directory):
    if not os.path.exists(directory):
        print("Creating project directory ", directory)
        os.makedirs(directory)


# creates the data files for the project i.e. the queue and the crawled files
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, 'blank data')


# creates file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# appends data to file
def append_file(path, data):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(data + '\n')


# deletes file content
def delete_file_content(path):
    with open(path, 'w', encoding='utf-8'):
        pass


# reads file content and adds all the links to a set
def file_to_list(filename):
    links_read = set()
    with open(filename, 'rt') as f:
        for line in f:
            links_read.add(line.replace('\n', ''))
    return links_read


# writes the link in the set to file
def list_to_file(links, filename):
    delete_file_content(filename)
    for link in sorted(links):
        append_file(filename, link)
