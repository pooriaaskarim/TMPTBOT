import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class HttpHandler:
    def __new__(cls):
        """ creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(HttpHandler, cls).__new__(cls)
        return cls.instance
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)