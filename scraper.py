from bs4 import BeautifulSoup as bs
import requests
import re

class Scraper:
    def __init__(self, sources):
        self.sources = sources
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        self.proxies = []

    def scrape_multiple_sources(self):
        for source in self.sources:
            self.scrape(source)

    def scrape(self, source):
        soup = bs(self.get_to_source(source).text, 'html.parser')
        proxies = soup.find_all('tr')
        for proxy in proxies:
            try:
                ip = proxy.find_all('td')[0].text
                port = proxy.find_all('td')[1].text
                if self.check_proxy(ip, port):
                    self.proxies.append(f'{ip}:{port}')
            except:
                pass
        
    def get_to_source(self, source):
        return requests.get(source, headers=self.headers)

    def check_proxy(self, ip, port):
        if re.search('[a-zA-Z]', ip) or "." not in ip:
            return False
        return True

