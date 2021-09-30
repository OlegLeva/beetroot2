s = 'helloworld'

if len(s) > 2:
    print(s[0:2]+s[-2]+s[-1])
elif len(s) == 2:
    print(s*2)
else:
    print('Empty string')

tel = '380509991111'
if 10 < len(tel) < 13 and tel.isdigit():
    print(True)
else:
    print(False)

name = 'oleg'
name_2 = input('Введите имя: ')
if name == name_2.lower():
    print(True)
else:
    print(False)