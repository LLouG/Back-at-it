'''catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
          ' (Or enter nothing to stop.)')
    name = input()
    if name == '':
        break
    catNames += [name]
print('The cat names are:')
for name in catNames:
    print(' ' + name)'''


'''spam = ['a', 'l', 'k', 'A', 'L', 'K']
spam.sort(key=str.lower)
print(spam)'''


# Mutable and Immutable Data Types
'''name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(newName)'''

'''print(type(('hello',)))
print(type(('hello')))'''

n1 = [1, 2, 3, 4, 5]
n2 = n1
n2[1] = 'Heyo'
print(n1, n2, sep='\n')
print(f'The id for n1 is {id(n1)} and the id for n2 is {id(n2)}.')
