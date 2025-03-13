import random
import sys
import time

''' # Guess the number
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

for guesses in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break  # This condition is the correct guess!

if guess == secretNumber:
    print(f'Good job! You guessed my number in {guesses} guesses!')
else:
    print(f'Nope. The number I was thinking of was {secretNumber}.')'''


'''# RPS
wins = 0
losses = 0
ties = 0

while True:  # The main game loop.
    # print('%s Wins, %s Losses, %s Ties' (wins, losses, ties))
    print(f'{wins} Wins, {losses} Losses, {ties} Ties.')
    while True:  # The player input loop.
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            print('Exiting program.')
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type one of r, p, s, or q.')

    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    if playerMove == computerMove:
        print('It is a tie')
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins += 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses += 1
        wins += 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses += 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses += 1'''


# print(i for i in range(1, 11))


'''indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('*******')
        time.sleep(0.1)

        if indentIncreasing:
            indent += 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()'''


# Comma Code
spam = ['apples', 'bananas', 'tofu', 'cats']
print(', '.join(spam[0:3]) + f' and {spam[-1]}')


# Coin Flip Streaks
# https://automatetheboringstuff.com/2e/chapter4/
'''numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.

    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))'''
