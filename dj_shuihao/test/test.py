# -*- coding: utf-8 -*-
from requests import Session

name = ['北京中数智汇', '中国专利技术开发公司']
session = Session()
url = 'http://219.234.81.168:3359/search_page'
data = {
    'target': None
}
for i in range(len(name)):
    data['target'] = name[i]
    content = session.post(url, data=data, timeout=(15, 15))

    print(content.text)

