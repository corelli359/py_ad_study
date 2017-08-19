# -*- coding: utf-8 -*-
import random
import time


# 为函数添加注解
def clip(text: str, max_len: 'int > 0' = 80) -> str:
    """在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # 没找到空格
        end = len(text)
    return text[:end].rstrip()


def tag(name, *content, cls=None, **attrs):
    """生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


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
