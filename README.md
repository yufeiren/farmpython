farmpython
==========

python tutorial

http://docs.python.org/2/tutorial/


python -c command [arg] ...

python -m module [arg] ...

>>> # Fibonacci series:
... # the sum of two elements defines the next
... a, b = 0, 1
>>> while b < 10:
...     print b
...     a, b = b, a+b
...

>>> a, b = 0, 1
>>> while b < 1000:
...     print b,
...     a, b = b, a+b
...

Coding style:
Use 4-space indentation, and no tabs.
Use docstrings


filter()
map()
reduce()


list --> []
tuple --> ()

Lists are mutable, while tuple is not mutable.



>>> s = 'hello'
>>> len(s)
5
>>> s = 'hello',
>>> len(s)
1



A set is an unordered collection with no duplicate elements.

Note that in general the practice of importing * from a module or
package is frowned upon, since it often causes poorly readable
code. However, it is okay to use it to save typing in interactive
sessions.

if make changes to a module, use reload(), e.g. reload(modulename)

.pyc and .pyo only affect loading time


str.ljust()
str.zfill()
str.format()



exception arguments

Most exceptions are defined with names that end in “Error,” similar to
the naming of the standard exceptions.

try
except
else
finally


Class initialization:

def __init__(self):
    self.data = []

Class variables vs. instances variables




next:
https://docs.python.org/2/tutorial/classes.html



