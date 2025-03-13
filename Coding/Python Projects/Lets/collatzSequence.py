
# https://automatetheboringstuff.com/2e/chapter3/

'''def collatz():
    while True:
        n1 = input("Say a number: ")
        number = int(n1)
        if number % 2 == 0:
            print(number // 2)
        else:
            for number in range(number):
                print(3 * number + 1)


collatz()'''


'''if n % 2 == 0:
    n / 2
else:
    n * 3 + 1'''


def collatz(n):
    while n != 1:
        if n // 2 == 0:
            print(n / 2)
            break
        else:
            print(n * 3 + 1)
            break


collatz(12)
