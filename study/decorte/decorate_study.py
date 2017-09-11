# -*- coding: utf-8 -*-
import time

'''
原理:
@decorate
def target():
    print('running target()')
等价于 =>>>   target = decorate(target
'''


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


def deco(func):
    print(func)

    def inner():
        print('running inner()')

    return inner


@deco
def target():
    print('running target()')


if __name__ == '__main__':
    target()
    # print('*' * 40, 'Calling snooze(.123)')
    # print(snooze(.123))
    # print(factorial(6))
