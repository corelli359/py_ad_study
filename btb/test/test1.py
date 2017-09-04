# -*- coding: utf-8 -*-
from utils.request_utils import RequestSession
from setting.headers import k_1m_headers
import time
from setting.data_set import *
from utils.db_utils import *

session = RequestSession()
for k in url_k_list:
    content = session.get_response_content(k['url'], headers=k_1m_headers)
    content_list = eval(content)[:2]
    print(len(content_list))
    k_list = []
    for con in content_list:
        check = check_last(k['kind'])
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
                    'CURRENT_DATE': cur_time[0],
                    'VOLUME': con[1],
                    'LAST_TIME': last_time
                }
            )
        else:
            continue
    write_to_sql(k_list, k['kind'])
