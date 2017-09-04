# -*- coding: utf-8 -*-
from utils.request_utils import RequestSession
import json
import time
from utils.db_utils import write_to_sql, check_date
from db.models import Deal_Rec

url = 'https://www.btctrade.com/coin/rmb/btc/order.js?t='
headers = {
    'accept': "application/json, text/javascript, */*; q=0.01",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.8",
    'connection': "keep-alive",
    'host': "www.btctrade.com",
    'referer': "https://www.btctrade.com/btc/",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.59 Safari/537.36",
    'x-requested-with': "XMLHttpRequest",
}

session = RequestSession()
content = session.get_response_content(url, headers=headers)
content_list = json.loads(content)['d']
print(content_list)
rec_list = []
for con in content_list:
    check = check_date()
    if check is not None:
        if str(check) >= con['t']:
            continue
    rec_list.append(
        {
            'DEAL_KIND': con['s'],
            'CURRENT_DATE': con['t'],
            'VOLUME': con['n'],
            'PRICE': con['p'],
            'TOTAL': float(con['p']) * float(con['n']),
            'LAST_TIME': time.time()

        }
    )
write_to_sql(rec_list, Deal_Rec)
