import scrapy
from ..items import IpItem
import requests


class IpspiderSpider(scrapy.Spider):
    name = 'ipSpider'
    allowed_domains = ['www.ip3366.net']
    page_urls = 'http://www.ip3366.net/free/?stype=1&page={}'

    def parse(self, response):
        lists = response.xpath('//tr')
        for i in lists:
            ip = i.xpath('./td[1]/text()').get()
            port = i.xpath('./td[2]/text()').get()
            proxy = f'{ip}:{port}'
            if ip and self.check_proxy(ip, port):
                item = IpItem()
                item['ip'] = ip
                item['port'] = port
                item['proxy'] = proxy
                print(proxy, '可以使用的ip')
                yield item
            else:
                print(proxy, '不能使用')

    def start_requests(self):
        for i in range(1, 2):
            url = self.page_urls.format(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def check_proxy(self, ip, port):
        proxy = {
            'http': '{}:{}'.format(ip, port)
        }
        try:
            e = requests.get('https://www.baidu.com/', proxies=proxy, timeout=5)
            return True
        except ZeroDivisionError as e:
            return False
