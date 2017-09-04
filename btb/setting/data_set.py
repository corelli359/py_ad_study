# -*- coding: utf-8 -*-
from db.models import *

url_1m_k = 'https://plugin.sosobtc.com/widgetembed/data/period?symbol=btctradebtccny&step=60'
url_3m_k = 'https://plugin.sosobtc.com/widgetembed/data/period?symbol=btctradebtccny&step=180'
url_5m_k = 'https://plugin.sosobtc.com/widgetembed/data/period?symbol=btctradebtccny&step=300'
url_10m_k = 'https://plugin.sosobtc.com/widgetembed/data/period?symbol=btctradebtccny&step=600'
url_15m_k = 'https://plugin.sosobtc.com/widgetembed/data/period?symbol=btctradebtccny&step=900'
url_30m_k = 'https://plugin.sosobtc.com/widgetembed/data/period?symbol=btctradebtccny&step=1800'
url_1h_k = 'https://plugin.sosobtc.com/widgetembed/data/period?symbol=btctradebtccny&step=3600'
url_2h_k = 'https://plugin.sosobtc.com/widgetembed/data/period?symbol=btctradebtccny&step=7200'
url_4h_k = 'https://plugin.sosobtc.com/widgetembed/data/period?symbol=btctradebtccny&step=14400'
url_6h_k = 'https://plugin.sosobtc.com/widgetembed/data/period?symbol=btctradebtccny&step=21600'
url_12h_k = 'https://plugin.sosobtc.com/widgetembed/data/period?symbol=btctradebtccny&step=43200'
url_1d_k = 'https://plugin.sosobtc.com/widgetembed/data/period?symbol=btctradebtccny&step=86400'
url_3d_k = 'https://plugin.sosobtc.com/widgetembed/data/period?symbol=btctradebtccny&step=259200'
url_week_k = 'https://plugin.sosobtc.com/widgetembed/data/period?symbol=btctradebtccny&step=604800'
url_month_k = 'https://plugin.sosobtc.com/widgetembed/data/period?symbol=btctradebtccny&step=2592000'

url_k_list = [
    {'kind': K_1M, 'url': url_1m_k}, {'kind': K_3M, 'url': url_3m_k}, {'kind': K_5M, 'url': url_5m_k},
    {'kind': K_10M, 'url': url_10m_k}, {'kind': K_15M, 'url': url_15m_k}, {'kind': K_30M, 'url': url_30m_k},
    {'kind': K_1H, 'url': url_1h_k}, {'kind': K_2H, 'url': url_2h_k}, {'kind': K_4H, 'url': url_4h_k},
    {'kind': K_6H, 'url': url_6h_k}, {'kind': K_12H, 'url': url_12h_k}, {'kind': K_1D, 'url': url_1d_k},
    {'kind': K_3D, 'url': url_3d_k}, {'kind': K_WEEK, 'url': url_week_k}, {'kind': K_MONTH, 'url': url_month_k},
]

deal_url = 'https://www.btctrade.com/coin/rmb/btc/order.js?t='
