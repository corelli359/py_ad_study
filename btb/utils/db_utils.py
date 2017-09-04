# -*- coding: utf-8 -*-
from db.models import *
from db.db_init import db_session, lock
import os


def check_last(model_table):
    table = model_table.__table__
    lock.acquire()
    try:
        sql = 'select max(LAST_TIME) from {} order by ID DESC '.format(table)
        check = db_session.execute(sql).first()[0]
        print(check)
    except:
        check = None
    lock.release()

    return check


def check_date():
    lock.acquire()
    try:
        result = db_session.execute(
            'SELECT CUR_DATE,LAST_TIME FROM DEAL_RECORD ORDER BY LAST_TIME DESC'
        ).first()
        CUR_DATE, LAST_TIME = result[0], result[1]

    except TypeError:
        CUR_DATE = LAST_TIME = None
    lock.release()
    return CUR_DATE, LAST_TIME


def check_date_txt():
    abs_f_name = 'data.txt'
    if not os.path.exists(abs_f_name):
        return None, None
    with open(abs_f_name, 'r') as f:
        data = f.readlines()
    try:
        end = eval(str(data[len(data) - 1]))
    except IndexError:
        return None, None
    if len(end) == 0:
        return None, None
    last = end[0]
    CUR_DATE = last[1]
    FIRST_TIME = last[len(last) - 1]
    return CUR_DATE, FIRST_TIME


def write_to_txt(data):
    if len(data) == 0:
        return
    abs_f_name = 'data.txt'
    with open(abs_f_name, 'a+') as f:
        f.writelines(str(data) + '\n')


def write_to_sql(data, model_table):
    if len(data) == 0:
        return
    try:

        db_session.execute(
            model_table.__table__.insert(), data
        )
        try:
            db_session.commit()

        except Exception as e:
            print('write failed and e is', e)

    except:
        print('sql commit failed!')
        print('data is', data)


if __name__ == '__main__':
    print(check_last(K_1M))
