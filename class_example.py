class A:
    @staticmethod
    def func():
        print("Hello Static Method")

temp = A()
temp.func()
A.func()