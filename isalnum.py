# Negative numbers inside strings are not "alphanumeric"

>>> x = '-1'
>>> x.isalnum()
False
>>> y = '1'
>>> y.isalnum()
True
>>> z = '-'
>>> z.isalnum()
False