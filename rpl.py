import sys


def main():
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], 'r') as f:
                print(*f.readlines(), sep='')
        except FileNotFoundError:
            print('File is not existed!')
    else:
        print('There is not any parameter for a file to be interpreted!')


if __name__ == '__main__':
    main()
