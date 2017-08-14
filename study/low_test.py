# -*- coding: utf-8 -*-


def pr():
    print('ending!')


def wa():
    global count
    while 1:
        if count == 5:
            return pr()
        count += 1
        print('go on')


if __name__ == '__main__':
    count = 0
    wa()
