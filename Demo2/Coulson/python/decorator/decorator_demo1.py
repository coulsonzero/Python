# python多层装饰器执行顺序




from icecream import ic
def deco1(func):
    ic(1)
    def wrapper1():
        ic(2)
        func()
        ic(3)
    ic(4)
    return wrapper1

def deco2(func):
    ic(5)
    def wrapper2():
        ic(6)
        func()
        ic(7)
    ic(8)
    return wrapper2

'''
装饰器执行顺序：从内到外
装饰器内函数调用顺序：从外到内，先进后出
'''
@deco1  # 后装饰deco1
@deco2  # 先装饰deco2
def foo():
    ic('foo')

if __name__ == '__main__':

    foo()

'''
5
8
1
4
2
6
foo
7
3
'''