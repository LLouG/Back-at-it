from time import sleep as sl


def stimer():
    s = 0
    while True:
        s += 1
        sl(1)
        print(f'Timer: {s}')
        if s >= 3:
            break
    print(u'\u16C3\u16A8\u16D2')


stimer()
