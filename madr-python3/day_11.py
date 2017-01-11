import sys


def move_generators(pinput, pos):

    for r in range(4, 0, -1):
        v = ' '.join(map(lambda x: x[0].ljust(2) if x[1] == r else '. ', sorted(pos.items())))
        print('F%d %s' % (r, v))
    print('\n\n')


def run(pinput):
    """Day 11: Radioisotope Thermoelectric Generators"""
    steps = 0
    starting = {
        'E': 1, 'SG': 1, 'SM': 1, 'PG': 1, 'PM': 1, 'TG': 2,
        'RG': 2, 'RM': 2, 'CG': 2, 'CM': 2, 'TM': 3, }
    m = move_generators(pinput, starting)
    steps += 1

    starting = {
        'E': 2, 'SG': 2, 'SM': 1, 'PG': 2, 'PM': 1, 'TG': 2,
        'RG': 2, 'RM': 2, 'CG': 2, 'CM': 2, 'TM': 3, }
    m = move_generators(pinput, starting)
    steps += 1

    starting = {
        'E': 3, 'SG': 3, 'SM': 1, 'PG': 2, 'PM': 1, 'TG': 3,
        'RG': 2, 'RM': 2, 'CG': 2, 'CM': 2, 'TM': 3, }
    m = move_generators(pinput, starting)
    steps += 1

    starting = {
        'E': 4, 'SG': 4, 'SM': 1, 'PG': 2, 'PM': 1, 'TG': 4,
        'RG': 2, 'RM': 2, 'CG': 2, 'CM': 2, 'TM': 3, }
    m = move_generators(pinput, starting)
    steps += 1

    starting = {
        'E': 3, 'SG': 4, 'SM': 1, 'PG': 2, 'PM': 1, 'TG': 3,
        'RG': 2, 'RM': 2, 'CG': 2, 'CM': 2, 'TM': 3, }
    m = move_generators(pinput, starting)
    steps += 1

    starting = {
        'E': 4, 'SG': 4, 'SM': 1, 'PG': 2, 'PM': 1, 'TG': 4,
        'RG': 2, 'RM': 2, 'CG': 2, 'CM': 2, 'TM': 4, }
    m = move_generators(pinput, starting)
    steps += 1

    starting = {
        'E': 3, 'SG': 3, 'SM': 1, 'PG': 2, 'PM': 1, 'TG': 4,
        'RG': 2, 'RM': 2, 'CG': 2, 'CM': 2, 'TM': 4, }
    m = move_generators(pinput, starting)
    steps += 1

    starting = {
        'E': 2, 'SG': 2, 'SM': 1, 'PG': 2, 'PM': 1, 'TG': 4,
        'RG': 2, 'RM': 2, 'CG': 2, 'CM': 2, 'TM': 4, }
    m = move_generators(pinput, starting)
    steps += 1

    starting = {
        'E': 1, 'SG': 1, 'SM': 1, 'PG': 1, 'PM': 1, 'TG': 4,
        'RG': 2, 'RM': 2, 'CG': 2, 'CM': 2, 'TM': 4, }
    m = move_generators(pinput, starting)
    steps += 1

    starting = {
        'E': 2, 'SG': 2, 'SM': 2, 'PG': 1, 'PM': 1, 'TG': 4,
        'RG': 2, 'RM': 2, 'CG': 2, 'CM': 2, 'TM': 4, }
    m = move_generators(pinput, starting)
    steps += 1

    starting = {
        'E': 3, 'SG': 3, 'SM': 3, 'PG': 1, 'PM': 1, 'TG': 4,
        'RG': 2, 'RM': 2, 'CG': 2, 'CM': 2, 'TM': 4, }
    m = move_generators(pinput, starting)
    steps += 1

    starting = {
        'E': 2, 'SG': 2, 'SM': 3, 'PG': 1, 'PM': 1, 'TG': 4,
        'RG': 2, 'RM': 2, 'CG': 2, 'CM': 2, 'TM': 4, }
    m = move_generators(pinput, starting)
    steps += 1

    starting = {
        'E': 3, 'SG': 2, 'SM': 3, 'PG': 1, 'PM': 1, 'TG': 4,
        'RG': 3, 'RM': 2, 'CG': 3, 'CM': 2, 'TM': 4, }
    m = move_generators(pinput, starting)
    steps += 1


    #starting = {'E': 1, 'HG': 2, 'HM': 1, 'LG': 3, 'LM': 1}
    #m = move_generators(pinput, starting)

    #print('Bot that deals with %s and %s:          %s' % )
    print('Steps:                                  %s' % steps)


if __name__ == '__main__':
    try:
        with open(sys.argv[1], 'r') as f:
            run(f.read().strip())
    except IOError:
        print('please provide a file path to puzzle file, example: ./puzzle.txt')
    except IndexError:
        print('please provide a file path to puzzle file, example: ./puzzle.txt')
