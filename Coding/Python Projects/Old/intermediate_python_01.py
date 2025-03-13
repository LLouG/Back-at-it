lists = "https://youtu.be/HGOBQPFzWKo?t=57"
#Lists: ordered, mutable, allows duplicate elements


tuples = "https://youtu.be/HGOBQPFzWKo?t=990"
#Tuples: ordered, immutable, allows duplicate elements

#import timeit
#print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
#print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))


dictionaries = "https://youtu.be/HGOBQPFzWKo?t=1790"
#Dictionaries: key-value pairs, unordered, mutable

#mydict = {"name":"Max", "age":28, "email":"loug@loug.com"}
#mydict2 = dict(name="Mary", age=27, city="Boston")
#mydict.update(mydict2)
#print(mydict)


sets = "https://youtu.be/HGOBQPFzWKo?t=2561"
#Sets: unordered, mutable, no duplicates

#odds = {1, 3, 5, 7, 9}
#evens = {0, 2, 4, 6, 8}
#primes = {2, 3, 5, 7}
#u = odds.union(evens) #argument is the second set
#print(u)
#i = odds.intersection(primes)
#print(i)

#setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
#setB = {1, 2, 3, 10, 11, 12}
#diff = setA.difference(setB)
#diff2 = setB.symmetric_difference(setA)
#print(diff)
#print(diff2)
#setA.update(setB)
#print(setA)
#setA.intersection_update(setB)
#print(setA)

#setA = {1, 2, 3, 4, 5, 6}
#setB = {1, 2, 3}
#setC = {7, 8}
#print(setB.issubset(setA))
#print(setB.issuperset(setA))
#print(setA.isdisjoint(setC))

#a = frozenset([1, 2, 3, 4]) #frozenset cannot be changed
#print(a)


strings = "https://youtu.be/HGOBQPFzWKo?t=3525"
#Strings: ordered, immutable, text representation

#greeting = "Hello"
#char = mystring[-1]
#print(char)
#if 'ell' in greeting:
#    print("Yes")
#else:
#    print("No")

#mystring = "  Hello World  "
#mystring = mystring.strip()
#print(mystring)
#print(mystring.startswith("H"))
#print(mystring.find("lo"))
#print(mystring.count("o"))
#print(mystring.replace("World", "Universe"))

#thisstring = "how are you doing"
#thislist = thisstring.split(" ") #use , to remove space
#print(thislist)
#newstring = ''.join(thislist)
#print(newstring)

#from timeit import default_timer as timer
#mylist = ['a'] * 1000000
#-----------
#start = timer()
#mystring = '' #BAD
#for i in mylist:
#    mystring += i
#stop = timer()
#print(stop - start)
#-----------
#start = timer() #GOOD
#mystring = ''.join(mylist)
#stop = timer()
#print(stop - start)

format = "%, .format and f-strings"
#var = "Tom"
#var2 = 3.1234
#mystring = "the variable is %s" % var #%d if the variable is a number or %f for float or %.2f for the numbers after dot
#print(mystring)
#mystring = "the variable is {}".format(var) #use {:.2f} for float
#print(mystring)
#mystring = f"the variable is {var} and {var2*2}" #add :.2f to change floating numbers
#print(mystring)


collections = "https://youtu.be/HGOBQPFzWKo?t=4971"
#Collections: counter, namedtuple, orderedDict, defaultdict, deque

#from collections import Counter
#a = "aaaabbbbccc"
#my_counter = Counter(a)
#print(my_counter)
#print(my_counter.keys())
#print(my_counter.items())
#print(my_counter.values())
#print(my_counter.most_common(2)) #Returns the 2 most common items
#print(my_counter.most_common(2)[0][0]) #Or .most_common(2)[0]
#print(list(my_counter.elements()))

#from collections import namedtuple
#Point = namedtuple('Point', 'x,y')
#pt = Point(1, -4)
#print(pt.x, pt.y)

#from collections import OrderedDict
#ordered_dict = {}
#ordered_dict['b'] = 2
#ordered_dict['c'] = 3
#ordered_dict['d'] = 4
#ordered_dict['a'] = 1
#print(ordered_dict)

#from collections import defaultdict
#d = defaultdict(int)
#d['a'] = 1
#d['b'] = 2
#print(d["a"]) #If [] doesn't exist it will return 0

#from collections import deque
#d = deque()
#d.append(1)
#d.append(2)
#d.appendleft(3)
#print(d)
#d.pop() #or d.popleft()
#print(d)
#d.extend([4, 5, 6]) #or d.exendleft()
#print(d)
#d.rotate(1) #negative number to rotate to the left
#print(d)


itertools = "https://youtu.be/HGOBQPFzWKo?t=5805"
#itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

#from itertools import product
#a = [1, 2]
#b = [3]
#prod = product(a, b, repeat=2)
#print(list(prod))

#from itertools import permutations
#a = [1, 2, 3]
#perm = permutations(a, 2) #Second argument is optional
#print(list(perm))

#from itertools import combinations, combinations_with_replacement
#a = [1, 2, 3, 4]
#comb = combinations(a, 2) #Second argument is mandatory
#print(list(comb))
#comb_wr = combinations_with_replacement(a, 2)
#print(list(comb_wr))

#from itertools import accumulate
#import operator
#a = [1, 2, 3, 4]
#acc = accumulate(a) #1+2 then 3+3 then 6+4
#acc2 = accumulate(a, func=operator.mul)
#print(a)
#print(list(acc))
#print(list(acc2))

#from itertools import groupby
#def smaller_than_3(x):
#    return x < 3
#a = [1, 2, 3, 4]
#group_obj = groupby(a, key=smaller_than_3)
#for key, value in group_obj:
#    print(key, value)
#    print(key, list(value))
#=-=-=-=-=-=-=-=-=-=
#persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
#           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
#group_obj = groupby(persons, key=lambda x: x['age'])
#for key, value in group_obj:
#    print(key, list(value))

#from itertools import count, cycle, repeat
#for c in count(10):
#    print(c)
#    if c == 15:
#        break
#a = [1, 2, 3]
#for cy in cycle(a):
#    print(cy)
#    if cy == 3:
#        break
#b = [1, 2, 3]
#for r in repeat(1, 3): #second argument is the number of times it will repeat
#    print(r)