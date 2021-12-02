def lucky_number(n):
    stack = [0] * n
    count = 0
    middle = n // 2
    left = 0
    right = 0

    while stack:
        if stack[-1] > 9:
            stack.pop()
            if stack:
                stack[-1] += 1
                if len(stack) <= middle: left = sum(stack[:middle])

            continue

        if len(stack) < n:
            if len(stack) > middle and left < sum(stack[middle:]):
                stack.pop()
                if stack:
                    stack[-1] += 1
                    if len(stack) <= middle: left = sum(stack[:middle])

                continue

            stack.extend([0] * (n - len(stack)))
            right = sum(stack[-middle:])

        if left == right: count += 1
        right += 1

        stack[-1] += 1
    return count


class LuckyNumberCalculator:
    def __init__(self, n=6):
        self.n = n
        self.stack = [0] * n

        self.middle = n // 2
        self.left = 0
        self.right = 0

    def _pop_and_recalc_left(self):
        self.stack.pop()
        if self.stack:
            self.stack[-1] += 1
            if len(self.stack) <= self.middle: self.left = sum(self.stack[:self.middle])

    def calculate(self):
        count = 0

        while self.stack:
            if self.stack[-1] > 9:
                self._pop_and_recalc_left()
                continue

            if len(self.stack) < self.n:
                if len(self.stack) > self.middle and self.left < sum(self.stack[self.middle:]):
                    self._pop_and_recalc_left()
                    continue

                self.stack.extend([0] * (self.n - len(self.stack)))
                self.right = sum(self.stack[-self.middle:])

            if self.left == self.right: count += 1
            self.right += 1

            self.stack[-1] += 1
        return count


if __name__ == "__main__":
    from datetime import datetime
    t = datetime.now()
    # print(lucky_number(6))
    calc = LuckyNumberCalculator(6)
    print(calc.calculate())
    print(datetime.now() - t)