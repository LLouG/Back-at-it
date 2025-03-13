'''print(r'That is Carol\'s cat')
print('Hello, world!'.partition('w'))
print('Hello, world!'.partition('XYZ'))
before, sep, after = 'Hello, world!'.partition(' ')
print(before, after, sep='\n')'''

'''print('Hello'.rjust(10))
print('World'.ljust(15, '-'))  # 5 characters from 'World" + 10 spaces
print('Hello'.center(20, '='))'''


'''def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)'''


'''spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))

ord('A')
chr(65)'''


'''import pyperclip
pyperclip.copy('Hello, world!')
pyperclip.paste()'''


# Project: Multi-Clipboard Automatic Messages
# https://automatetheboringstuff.com/2e/chapter6/
