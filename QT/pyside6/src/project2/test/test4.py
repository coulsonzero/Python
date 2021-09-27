"""
@author: coulson
@version: 2021/7/29  9:56
"""
class A:
    def __init__(self, v1=0,v2=1):
        self.v1 = v1
        self.__v2 = v2

    def __dir__(self):
        print("changed")

    def func1(self):

        print("test")
    def __func2(self):
        self.__v2 = 5
        print(self.__v2)


if __name__ == '__main__':
    a = A()
    print(a.__dir__())

    print(a._A__v2)
    print(a._A__func2())

