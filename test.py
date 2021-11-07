def fib():
    numb, next_numb = 1, 1
    while True:
        yield numb
        numb, next_numb = next_numb, numb + next_numb


for i in (fib()):
    if i % 12 == 0:
        print("Всё приехали")
        break
    print(i)


