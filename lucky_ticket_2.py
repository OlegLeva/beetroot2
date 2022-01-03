def lucky_number(n):
    stack = [0] * n
    count = 0
    middle = n // 2
    left = 0
    right = 0

    while stack:


        if stack[-1] > 9:
            # print(f'Когда когда поледний 10 {stack}')
            stack.pop()
            if stack:
                stack[-1] += 1
                # import pdb; pdb.set_trace()
                if len(stack) <= middle:
                    left = sum(stack[:middle])
                    print(stack)

            continue

        if len(stack) < n:
            # print(f'Когда LEN меньше 6 {stack}')
            stack.extend([0] * (n - len(stack)))
            right = sum(stack[-middle:])

        if left == right:
            count += 1
        right += 1

        stack[-1] += 1

    return count


if __name__ == "__main__":
    from datetime import datetime
    t = datetime.now()
    print(lucky_number(6))
    print(datetime.now() - t)


