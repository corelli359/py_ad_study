# -*- coding: utf-8 -*-

import time
import sched
import threading
from app.app_pro import crawler_volume_txt


def get_deal(cmd, inc):
    crawler_volume_txt()
    schedule.enter(inc, 0, get_deal, (cmd, inc))


def crwaler_deal_func():
    # 10为间隔时间，单位为秒，此处可自行设置
    schedule.enter(5, 0, get_deal, ('deal_connect', 10))
    schedule.run()


if __name__ == '__main__':
    schedule = sched.scheduler(time.time, time.sleep)
    thread_list = []
    deal_thread = threading.Thread(target=crwaler_deal_func)
    thread_list.append(deal_thread)

    for t in thread_list:
        t.setDaemon(True)
        t.start()
    t.join()
