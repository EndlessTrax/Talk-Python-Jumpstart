


def main():
    print_header()
    game_loop()


def print_header():
    print('---------------------------------')
    print('        WIZARD GAME APP')
    print('---------------------------------')
    print()


def game_loop():
    while True:
        cmd = input("Do you want to [a]ttack, [r]unaway, or [l]ook around? ")

        if cmd == 'a':
            print('attack')
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('Look Away')
        else:
            print('Ok, exiting the game... bye!')
            break


if __name__ == '__main__':
    main()
