class A:
    def __init__(self, v1=0, v2=1):
        self.v1 = v1
        self.__v2 = v2
    # def __dir__(self):
    #     pass
    def func1(self):
        print("func1")
    def func2(self):
        print(self.__v2)
    def __func3(self):
        # self.__v2 = 5
        # print(self.__v2)
        print("hello")

if __name__ == '__main__':
    a = A()
    # print(a.__dir__())
    # a.func2()
    # print(a._A__v2)
    print(a._A__func3())

