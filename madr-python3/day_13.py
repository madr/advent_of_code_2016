import sys


def run(pinput):
    """Day 13: A Maze of Twisty Little Cubicles"""
    w = 10
    y = 0
    z = list()
    for x in range(0, 11):
        for y in range(0, 7):
            z.append('#' if len(
                '{0:b}'.format(x * x + 3 * x + 2 * x * y + y + y * y + pinput).translate(
                    {ord('0'): None})) % 2 == 1 else '.')

    pass


if __name__ == '__main__':
    try:
        with open(sys.argv[1], 'r') as f:
            run(f.read().strip())
    except IOError:
        print('please provide a file path to puzzle file, example: ./puzzle.txt')
    except IndexError:
        print('please provide a file path to puzzle file, example: ./puzzle.txt')
