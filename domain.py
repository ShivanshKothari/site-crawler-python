from urllib.parse import urlparse


# get domain name
def get_domain_name(url):
    try:
        results = get_subdomain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        print('Error encountered:', Exception)
        return ''


# get sub domain name
def get_subdomain_name(url):
    try:
        return urlparse(url).netloc
    except:
        print('Error encountered:', Exception)
        return ''
