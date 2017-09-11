# -*- coding: utf-8 -*-
from functools import wraps
import asyncio


def simple_coroutine(a):
    print('-> coroutine started')
    x = yield a
    print('-> coroutine received:', x)
    c = yield a + x
    print('-> Received: c =', c)


# @asyncio.coroutine
def coroutine_wraps(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine_wraps
def averager():
    total = 0.0
    count = 0
    average = None
    while 1:
        term = yield average
        total += term
        count += 1
        average = total / count


# def coroutine_wraps(func):
#     """装饰器：向前执行到第一个`yield`表达式，预激`func`"""
#
#     @wraps(func)
#     def primer(*args, **kwargs):
#         gen = func(*args, **kwargs)
#         next(gen)
#         return gen
#
#     return primer


if __name__ == '__main__':
    my_coro = simple_coroutine()
