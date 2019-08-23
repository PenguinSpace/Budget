# class CSStudent():
#     stream = "cse"
#
#     def __init__(self, name = "Helen"):
#         self.name = name
#
#
# if __name__ == '__main__':
#     a = CSStudent("Nelson")
#     b = CSStudent()
#
#     print(a.name)
#     print(b.name)
#     print(a.stream)
#     print(CSStudent.stream)


class Base(object):
    def __init__(self, x):
        self.x = x


class derived(Base):
    def __init__(self, x, y):
        Base.x = x
        self.y = y

    def printxy(self):
        print(self.y, Base.x)


if __name__ == '__main__':
    me = derived(10, 20)
    me.printxy()