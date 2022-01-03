def lucky_ticket(n):
    stack = [0] * 6
    middle = n // 2
    count = 0
    index = 1
    # left = 0
    # right = 0

    while stack:
        if sum(stack[:middle]) == sum(stack[-middle:]):
            count += 1

        if stack[-index] > 9:
            stack.pop()
            stack[-index] += 1
            stack.extend([0] * (n - len(stack)))

        stack[-index] += 1
        print(stack)

    return count

print(lucky_ticket(6))
