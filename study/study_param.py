# -*- coding: utf-8 -*-
# wrong func!
class HauntedBus:
    """
        备受幽灵乘客折磨的校车
        
        没有指定初始乘客的 HauntedBus 实例会共享同一个乘客列表(passengers)。
        因为 self.passengers 变成了 passengers 参数默认值的别名
    """

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    bus = HauntedBus(['a', 'b'])
    print(bus.passengers)
    bus.pick('c')
    print(bus.passengers)
    bus_1 = HauntedBus()
    print(id(bus_1))
    bus_1.pick('e')
    print(bus_1.passengers)
    bus_2 = HauntedBus()
    print(id(bus_2))
    print(bus_2.passengers)
    print(bus.passengers)

    print(dir(HauntedBus.__init__.__defaults__))
    print(HauntedBus.__init__.__defaults__)
