from random import randint as ri

def guess_the_number(x):
    print("Let's play Guess The Number")

    random_number = ri(0, x)
    num_guesses = 0

    while True:
        guess = int(input(f"Guess a number between 0 and {x}: "))
        num_guesses += 1

        if guess == random_number:
            print(f"Congrats! The number is {random_number} and you guessed it in {num_guesses} attempts")
            break
        elif guess < random_number:
            print("Too low!")
        else:
            print("Too high!")
            