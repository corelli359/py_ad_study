# -*- coding: utf-8 -*-
from requests import Session
from lxml import etree
import re
from tyc.headers import headers, detail_headers
from urllib.parse import quote


def get_cookies(cook):
    cook_list = {}
    for c in cook.cookies:
        cook_list[c.name] = c.value
    return cook_list


proxies = {
    'http': 'http://%s' % '219.234.81.111:9999',
    # 'http': 'http://%s' % '192.168.100.111:9999',
}


def return_none():
    pass


class TianYanCha(object):
    def __init__(self, name):
        self.name = name

    def run(self, count=0):
        # agent = random.choice(agents)
        # print('now the UA is {}'.format(agent))
        session = Session()

        # name = '广东美信科技股份有限公司'
        name = quote(self.name)
        pattern = '(<a href="https://www.tianyancha.com/company(.+?)")[\s\S]+?(%s{1})' % self.name
        url = 'https://www.tianyancha.com/search?key={}&checkFrom=searchBox'
        target_url = url.format(name)
        cookies = {}
        response = session.get(target_url, headers=headers, timeout=(15, 15))
        cookies.update(get_cookies(response))
        print(cookies)
        content = response.content.decode('utf-8')
        source = etree.HTML(content)
        try:
            href_list = re.findall(pattern, content)
            if len(href_list) == 0:
                return None
            # href = source.xpath('//div[@class="row pb10"]/div/a/@href')[0]
            href = re.findall('href="(.*?)"', str(href_list[0]))[0]
            print(href)
            detail_url = href
            detail_response = session.get(detail_url, headers=detail_headers, cookies=cookies, timeout=(15, 15))
            detail_content = detail_response.content.decode('utf-8')
            if '纳税人识别号' in detail_content:
                nashui = re.findall('纳税人识别号[\s\S]+?<span>(.+?)</span>', detail_content)[0]
                # nashui = re.findall('<div class="c8">纳税人识别号：\n +<span>(.+?)</span>', detail_content)
            else:
                nashui = None
        except:
            if count < 10:
                print('getting with wrong wait and retry! ')
                count += 1
                return self.run(count)
            else:
                nashui = None

        return nashui
