# -*- coding: utf-8 -*-
import random
import time


# 私有属性_dic 不被外部控制，但是可以随着初始化时的引入变量的值的改变而改变
class MappingClassTest:
    def __init__(self, dic):
        if not isinstance(dic, dict):
            raise TypeError(dic)
        self._dic = dic

    def __repr__(self):
        return str(self._dic)


def effect_set_list():
    def choice_num():
        return random.sample(range(10000000), 1000)

    def func_1():
        start = time.time()
        count = 0
        for n in choice_list:
            if n in total:
                count += 1
        if count == 1000:
            print('func_1 takes {} secs'.format(str(time.time() - start)))

    def func_2():
        start = time.time()
        count = len(set(choice_list) & set(total))
        if count == 1000:
            print('func_2 takes {} secs'.format(str(time.time() - start)))

    choice_list = choice_num()
    total = [x for x in range(10000000)]
    func_2()
    func_1()


# 利用此类进行__call__的理解,利用__call__将对象函数化，可被调用
class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


if __name__ == '__main__':
    bg = BingoCage(range(5))
    print(callable(bg))
    print('hello')
