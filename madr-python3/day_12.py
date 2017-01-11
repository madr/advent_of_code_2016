import sys


def solve(pinput, registers):
    lines = pinput.splitlines()
    n = 0

    while n < len(lines):
        l = lines[n]
        if l.startswith('cpy'):
            c, v, r = l.split()
            registers[r] = registers[v] if v in registers.keys() else int(v)

        if l.startswith('inc') or l.startswith('dec'):
            c, r = l.split()
            registers[r] += 1 if c == 'inc' else -1

        if l.startswith('jnz'):
            c, nz, v = l.split()
            nz = int(registers[nz]) if nz in registers.keys() else int(nz)
            n = n + int(v) if nz != 0 else n + 1
        else:
            n += 1

    return registers


def run(pinput):
    """Day 12: Leonardo's Monorail"""
    initial = {'a': 0, 'b': 0, 'c': 0, 'd': 0, }
    registers = solve(pinput, initial)
    print('Register A, c=0:                        %s' % registers['a'])

    initial['c'] = 1
    registers = solve(pinput, initial)
    print('Register A, c=1:                        %s' % registers['a'])


if __name__ == '__main__':
    try:
        with open(sys.argv[1], 'r') as f:
            run(f.read().strip())
    except IOError:
        print('please provide a file path to puzzle file, example: ./puzzle.txt')
    except IndexError:
        print('please provide a file path to puzzle file, example: ./puzzle.txt')
