class CustonException(Exception):
    def __init__(self, msg):
        x = open('logs.txt', 'a+')
        x.write(msg + '\n')
        x.close()

try:
    raise CustonException("My exception")
except CustonException as e:
    print(e)