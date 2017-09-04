# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import json
# from settings.proxy_setting import proxies
import requests


def get_cookies(cook):
    cook_list = {}
    for c in cook.cookies:
        cook_list[c.name] = c.value
    return cook_list


def temp_request(url):
    repeat = 0
    content = None
    while repeat < 3:
        try:
            content = requests.get(url, proxies=None).content
            if len(content) > 2:
                if isinstance(content, bytes):
                    content = str(content, encoding='utf-8')
                break
        except:
            if repeat == 3:
                print('the url:{} get failed!'.format(str(url)))
                continue
    return content


def to_json(content):
    try:
        json_content = json.loads(content)
    except:
        json_content = None
    return json_content


class RequestSession(object):
    def __init__(self):
        self.session = self.meke_session()
        self.spider_cookies = {}
        self.temp_cookies = {}

    @staticmethod
    def to_json(content):
        try:
            json_content = json.loads(content)
        except:
            json_content = None
        return json_content

    @staticmethod
    def meke_session():
        session = requests.session()
        return session

    # 获取page页面同时获取当前页面的cookies
    def get_response_content(self, url, headers, cookies=None, validate=False):
        if cookies is None:
            cookies = self.spider_cookies
        page = self.do_get(url, headers, cookies)
        try:
            page_content = page.content
        except:
            page_content = None
            return page_content

        if isinstance(page_content, bytes):
            page_content = str(page_content, encoding='utf-8')
            cookies = get_cookies(page)
        if not validate:
            self.spider_cookies.update(cookies)
        else:
            self.temp_cookies = cookies
        return page_content

    # get请求
    def do_get(self, url, headers, cookies):
        repeat = 0
        content = None
        while repeat < 3:
            repeat += 1
            try:
                content = self.session.get(url, headers=headers, cookies=cookies, proxies=None, timeout=(15, 15))
                if len(content.content) > 2:
                    break
            except:
                if repeat == 3:
                    print('the url:{} get failed!'.format(str(url)))
                continue
        return content

    def get_session(self):
        return self.session
