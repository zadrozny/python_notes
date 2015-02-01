#!/usr/bin/env python3

# Example courtesy of https://github.com/akulakov

# Method resolution order in Python:
# 	https://www.python.org/download/releases/2.3/mro/


# Compare this...
class A:
    def x(self):
        print("in A")
        super().x()

class B:
    def x(self):
        print("in B")

class C(A,B):
    def x(self):
        print("in C")
        super().x()

C().x()


#... with this:

class A:
    def x(self):
        print("in A")
        super().x()

class B:
    def x(self):
        print("in B")

class C(B,A):
    def x(self):
        print("in C")
        super().x()

C().x()