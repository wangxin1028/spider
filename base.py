from urllib.parse import urlparse

import requests
import time
import pdfkit
import os
class Spider(object):
    name="No_Name"
    def __init__(self,name,base_url):
        self.name = name
        self.base_url = base_url
        self.domain = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(self.base_url))
    @staticmethod
    def request(url,**kwargs):
        response = requests.get(url,**kwargs)
        return response

    def parse_url_list(self,response):
        raise NotImplementedError

    def parse_content(self,response):
        raise  NotImplementedError

    def run(self):
        start = time.time()
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'outline-depth': 10,
        }
        htmls=[]
        for index,url in enumerate(self.parse_url_list(self.request(self.base_url))):
            html = self.parse_content(self.request(url))
            f_name = ".".join([str(index), "html"])
            with open(f_name, 'wb') as f:
                f.write(html)
            htmls.append(f_name)

        pdfkit.from_file(htmls, self.name + ".pdf", options=options)
        for html in htmls:
            os.remove(html)
        total_time = time.time() - start
        print(u"总共耗时：%f 秒" % total_time)