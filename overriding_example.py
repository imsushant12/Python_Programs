class A:
    classVar1 = "Class A"
    def __init__(self):
        self.classVar1 = "Inside Constructor of class A"

#class  inherited from class A
class B(A):
    classVar1 = "Class B"
    def __init__(self):
        self.classVar1 = "Inside Constructor of class B"

a = A()
b = B()

print(b.classVar1)
print(a.classVar1)