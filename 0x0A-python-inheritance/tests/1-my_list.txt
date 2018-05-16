>>> MyList = __import__('1-my_list').MyList

>>> type(MyList())
<class '1-my_list.MyList'>

>>> issubclass(MyList, list)
True

>>> s = __import__('1-my_list').__doc__
>>> len(s) > 1
True

>>> empty = MyList()
>>> empty.print_sorted()
[]

>>> 'print_sorted' in dir(MyList)
True

>>> l = MyList()
>>> l.append(10)
>>> l.append(15)
>>> l.append(12)
>>> l.append(13)
>>> l.append(14)
>>> print(l)
[10, 15, 12, 13, 14]
>>> l.print_sorted()
[10, 12, 13, 14, 15]
>>> print(l)
[10, 15, 12, 13, 14]

>>> l = MyList()
>>> l.append(343)
>>> l.append(232)
>>> l.append(21)
>>> l.append(565)
>>> l.print_sorted()
[21, 232, 343, 565]

>>> l = MyList()
>>> l.append(14)
>>> l.append(13)
>>> l.append(12)
>>> l.append(11)
>>> l.append(10)
>>> l.print_sorted()
[10, 11, 12, 13, 14]

>>> l.append(-434)
>>> l.append(-599)
>>> l.append(-4)
>>> l.append(-3)
>>> l.print_sorted()
[-599, -434, -4, -3, 10, 11, 12, 13, 14]

>>> l = MyList()
>>> l.append(-10)
>>> l.append(-49)
>>> l.append(-9)
>>> l.append(-2)
>>> l.print_sorted()
[-49, -10, -9, -2]

>>> l = MyList()
>>> l.append(0)
>>> l.append(0)
>>> l.append(0)
>>> l.print_sorted()
[0, 0, 0]

>>> l.print_sorted(44, 33)
Traceback (most recent call last):
...
TypeError: print_sorted() takes 1 positional argument but 3 were given
