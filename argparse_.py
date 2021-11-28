import argparse
parser = argparse.ArgumentParser()

parser.add_argument('a', type=str)
parser.add_argument('b', type=str)

args = parser.parse_args()



def count_lines(name):
    with open(name, 'r') as n:
        print(len(n.readlines()))

def count_chars(name):
    with open(name, 'r') as n:
        print(n.read())


def test(name):
    count_lines(name)
    count_chars(name)

count_lines(args.a)
count_chars(args.b)