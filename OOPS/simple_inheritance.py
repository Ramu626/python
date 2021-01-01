
# @Author: Ramu Devarashetti

# Method Resolution Order is C => A (Left most) if init then done won't go to B (Right)\
    # C(A, B).
# To Avoid this we need to call super() method in each class

class A:
    def __init__(self):
        print("Inside {} ".format(__class__))
        super().__init__()
        self.a = 1

class B:
    def __init__(self):
        print("Inside {} ".format(__class__))
        super().__init__()
        self.b = 2

class C(A, B):
    def __init__(self):
        print("Inside {} ".format(__class__))
        super().__init__()
        self.c = 3


if __name__ == "__main__":
    c_obj = C()
    print(C.mro())
    print(c_obj.a, c_obj.b, c_obj.c)
    # Try commenting super().__init__() in A and B once for better understanding

