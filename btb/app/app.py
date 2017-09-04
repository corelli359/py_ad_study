# -*- coding: utf-8 -*-
from utils.request_utils import RequestSession
from setting.headers import k_1m_headers
import time
from setting.data_set import *
from utils.db_utils import *
import json


def crawler_k_line():
    session = RequestSession()
    for k in url_k_list:
        content = session.get_response_content(k['url'], headers=k_1m_headers)
        content_list = eval(content)
        k_list = []
        check = check_last(k['kind'])
        for con in content_list:
            if check is not None:
                if check >= int(con[0] / 1000):
                    continue
            cur_time = time.strftime(
                '%Y-%m-%d %H:%M:%S %A',
                time.localtime(int(con[0] / 1000) - 28800)
            )
            if len(con) == 6:
                last_time = None
                if content_list.index(con) == len(content_list) - 1:
                    last_time = int(con[0] / 1000)
                k_list.append(
                    {
                        'KAI_PAN': con[2],
                        'ZUI_GAO': con[3],
                        'ZUI_DI': con[4],
                        'SHOU_PAN': con[5],
                        'CUR_DATE': cur_time,
                        'VOLUME': con[1],
                        'LAST_TIME': last_time
                    }
                )
            else:
                continue
        write_to_sql(k_list, k['kind'])


def crawler_volume():
    session = RequestSession()
    content = session.get_response_content(deal_url, headers=k_1m_headers)
    content_list = json.loads(content)['d']
    rec_list = []
    CUR_DATE, LAST_TIME = check_date()
    for con in content_list:
        if LAST_TIME is not None:
            t = int(time.time())
            if LAST_TIME >= t:
                continue
            if str(CUR_DATE) >= con['t']:
                continue
        rec_list.append(
            {
                'DEAL_KIND': con['s'],
                'CUR_DATE': con['t'],
                'VOLUME': con['n'],
                'PRICE': con['p'],
                'TOTAL': float(con['p']) * float(con['n']),
                'LAST_TIME': time.time()
            }
        )
    write_to_sql(rec_list, Deal_Rec)
