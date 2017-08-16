# -*- coding: utf-8 -*-
from requests import Session
from lxml import etree
import re


def get_cookies(cook):
    cook_list = {}
    for c in cook.cookies:
        cook_list[c.name] = c.value
    return cook_list


proxies = {
    'http': 'http://%s' % '219.234.81.111:9999',
    # 'http': 'http://%s' % '192.168.100.111:9999',
}


class TianYanCha(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        session = Session()
        headers = {
            'content-type': "text/html; charset=utf-8",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "zh-CN,zh;q=0.8",
            'cache-control': "no-cache",
            'connection': "keep-alive",
            'host': "www.tianyancha.com",
            'referer': "https://www.tianyancha.com/",
            'upgrade-insecure-requests': "1",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        }
        # name = '广东美信科技股份有限公司'
        name = self.name
        url = 'https://www.tianyancha.com/search?key={}&checkFrom=searchBox'
        target_url = url.format(name)
        cookies = {}
        response = session.get(target_url, headers=headers, timeout=(15, 15))
        cookies.update(get_cookies(response))
        print(cookies)
        content = response.content.decode('utf-8')
        source = etree.HTML(content)
        href = source.xpath('//div[@class="row pb10"]/div/a/@href')[0]
        print(href)

        detail_url = href
        detail_headers = {
            'content-type': "text/html; charset=utf-8",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "zh-CN,zh;q=0.8",
            'cache-control': "no-cache",
            'connection': "keep-alive",
            'host': "www.tianyancha.com",
            # 'referer': "https://www.tianyancha.com/search?key=%E5%B9%BF%E4%B8%9C%E7%BE%8E%E4%BF%A1%E7%A7%91%E6%8A%80%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&checkFrom=searchBox",
            'referer': '',
            'upgrade-insecure-requests': "1",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        }
        try:
            detail_response = session.get(detail_url, headers=detail_headers, cookies=cookies, timeout=(15, 15))
        except:
            return None
        detail_content = detail_response.content.decode('utf-8')
        v = '纳税人识别号' in detail_content
        print(v)

        nashui = re.findall('<div class="c8">纳税人识别号：\n +<span>(.+?)</span>', detail_content)[0]
        # print(nashui)
        return nashui
