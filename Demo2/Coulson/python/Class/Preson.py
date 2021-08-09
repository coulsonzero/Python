from icecream import ic


class Preson(object):
    def __init__(self, name, age, sex):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)

    def setName(self, name):
        if not isinstance(name, str):
            print("name must be string!")
            return
        self.__name = name

    def setAge(self, age):
        if not isinstance(age, int):
            print("age must be integer!")
            return
        self.__age = age

    def setSex(self, sex):
        if sex not in ("man", "woman"):
            print("sex must be 'man' or 'woman'!")
            return
        self.__sex = sex

    def __test(self):
        print("hello world!")

    def show(self):
        print("Name: ", self.__name)
        print("Age: ", self.__age)
        print("Sex: ", self.__sex)

class Student(Preson):
    def __init__(self, name="shville", age=21, sex="man", room="F4"):
        super(Student, self).__init__(name, age, sex)
        self.room = room


    def show(self):
        print(super(Student, self).show())
        print(self.room)

if __name__ == '__main__':
    # p = Preson("coulson", 24, "man")
    # p.show()
    # p._Preson__test()
    # ic(dir(p))
    s = Student("coulson", 24, "man", "F5")
    # s = Student()
    s.show()
    # s.show()



