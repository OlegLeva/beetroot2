import random

point = 0
while True:
    x = random.randint(1, 50)
    y = random.randint(1, 50)
    print("Твои очки:" + str(point))

    answer = input(f"Сколько будет {x} + {y} = ")
    if answer == 'q':
        break
    if int(answer) != x+y:
        print("Ваня ЛОХ")
    else:
        print("Ваня КРАСАВЧИК")
        point += 1
















