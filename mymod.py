import sys

f = sys.argv[1]

def count_lines(name):
    with open(name, 'r') as n:
        print(len(n.readlines()))

def count_chars(name):
    with open(name, 'r') as n:
        print(len(n.read()))


def test(name):
    count_lines(name)
    count_chars(name)

test(f)