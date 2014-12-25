# How to delete the elements of a list
>>> import sys
>>> li = [1, 2, 3]
>>> sys.getsizeof(li)
96
>>> del li[:]
>>> sys.getsizeof(li)
72
