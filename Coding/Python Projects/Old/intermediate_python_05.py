Function_Arguments_In_Detail = "https://youtu.be/HGOBQPFzWKo?t=17608"

#def foo(a, b, *args, **kwargs):
#    print(a,b)
#    for arg in args:
#        print(arg)
#    for key in kwargs:
#        print(key, kwargs[key])
#foo(1, 2, 3, 4, 5, six=6, seven=7)

#def bar(*args, last):
#    for arg in args:
#        print(arg)
#    print(last)
#bar(1, 2, 3, last=100)

#def foo(a, b, c):
#    print(a, b, c)
#my_dict = {'a': 1, 'b': 2, 'c': 3}
#foo(**my_dict)

#def bar():
#    global number
#    x = number
#    print('Number inside function:', x)
#number = 0
#bar()
#print(number)


Asterisk_Operator = "https://youtu.be/HGOBQPFzWKo?t=19049"

#numbers = [1, 2, 3, 4, 5, 6]
#beginning, *middle, last = numbers # Unpacking
#print(beginning)  # Prints only the first element
#print(middle)
#print(last) # Prints only the last element

#my_tuple = (1, 2, 3)
#my_list = [4, 5, 6]
#new_list = [*my_tuple, *my_list]
#print(new_list)

#dict_a = {'a': 1, 'b': 2}
#dict_b = {'c': 3, 'd': 4}
#my_dict = {**dict_a, **dict_b}
#print(my_dict)


Shallow_vs_Deep_Copying = "https://youtu.be/HGOBQPFzWKo?t=19820"

#from copy import copy
#org = [0, 1, 2, 3, 4]
#cpy = copy(org)
#cpy2 = org[:]
#print(cpy)
#print(cpy2)

#from copy import deepcopy
#org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
#cpy = deepcopy(org)
#cpy[0][1] = -10
#print(org)
#print(cpy)

#import copy
#class Person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#class Company:
#    def __init__(self, boss, employee):
#        self.boss = boss
#        self.employee = employee
#p1 = Person('Alex', 55)
#p2 = Person('Joe', 27)
#company = Company(p1, p2)
#company_clone = copy.deepcopy(company)
#company_clone.boss.age = 56
#print(company_clone.boss.age)
#print(company.boss.age)


Context_Manager = "https://youtu.be/HGOBQPFzWKo?t=20408"

#with open('notes.txt', 'w') as file: # Recommended way to open files
#    file.write('some todoo...')

#class ManagedFile:
#    def __init__(self, filename):
#        print('init')
#        self.filename = filename
#    def __enter__(self):
#        print('enter')
#        self.file = open(self.filename, 'w')
#        return self.file
#    def __exit__(self, exc_type, exc_value, exc_traceback):
#        if self.file:
#            self.file.close()
#        if exc_type is not None:
#            print('exception has been handled')
#        #print('exc:', exc_type, exc_value) # use this with file.somemethod()
#        print('exit')
#        return True
#with ManagedFile('notes.txt') as file:
#    print('do some stuff...')
#    file.write('some todoo...')
#    file.somemethod()   # This wil generate an error
#print('continuing')

#from contextlib import contextmanager
#@contextmanager
#def open_managed_file(filename):
#    f = open(filename, 'w')
#    try:
#        yield f     # yield is a generator
#    finally:
#        f.close()
#with open_managed_file('notes.txt') as f:
#    f.write('some todoo...')
