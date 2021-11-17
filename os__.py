import os
import sys


# for a, b, c in os.walk('.'):
#     print(a, b, c)

# for a, b, c in os.walk(os.getcwd()):
#     print(a, b, c)

print(os.getcwd())

print(os.listdir('.'))

print(sys.argv)
print((sys.argv[1]*5))

x = os.listdir('/Users/mymac/Downloads')
print(x)
d = {k: v for k, v in enumerate(x)}
print((sys.argv[1]*5))
with open('test_os.txt', 'a') as f:
    for k, v in enumerate(x, 5):
        f.write(f'{k}: {v} \n')


with open('test_os.txt', 'r') as f:
    t = f.read()
print(t)
