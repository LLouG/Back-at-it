from gtn import guess_the_number
from rps import rock_paper_scissors
from wordle import Wordle

while True:
    txt = """Mini games!!!
    - Guess The Number      (1)
    - Rock, Paper, Scissor  (2)
    - Wordle                (3)
    - Connect Four          (4)
    - Tic Tac Toe           (5)
Select a game (press a number or 'q' to quit): """

    value = input(txt)
    if value == "1":
        #zx = input("Choose the second input:")
        guess_the_number(100)
        # TODO: ask user for second input
    elif value == "2":
        rock_paper_scissors()
        # TODO: check against all possible cases, "Rock smassers scissors"
    elif value == "3":
        game = Wordle()
        game.play()
        # TODO: load words from text file
    elif value == "4":
        pass
    elif value == "q":
        break
