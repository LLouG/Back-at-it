import random

'''print(not not not not not not True)  # Even returns True, Odd returns False'''

'''while True:
    print("Please type your name")
    name = input()
    if name == 'your name':
        break
print("Thank you!")'''


'''while True:
    print('Who are you?')
    name = input()
    if name != 'Loug':
        continue
    print('Hello, Loug. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print("Access granted.")'''

'''print('My name is')
for i in range(5):
    print('Loug Five Times (' + str(i + 1) + ')')'''

'''total = 0
for num in range(101):
    total = total + num
print(total)'''

'''for i in range(5):
    print(random.randint(1, 10))'''


# print('Spam', 'eggs', 'spam', sep=', ')

'''# Call Stack
def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()'''


'''# Local scopes
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()'''


'''def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)'''


'''def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))'''
