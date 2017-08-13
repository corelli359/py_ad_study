# -*- coding: utf-8 -*-
from types import MappingProxyType
from requests import Session


class MappingClassTest(dict):
    def __init__(self, dic):
        if not isinstance(dic, dict):
            raise TypeError(dic)
        self._dic = dic

    def __repr__(self):
        return str(self._dic)


if __name__ == '__main__':
    d = {'name': 'hello'}
    mc = MappingClassTest(d)
    mp = MappingProxyType(d)
    print(mc)
    print(type(mc))
    print(type(mp))
