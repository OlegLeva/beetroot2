def lucky_number(n):
    is_odd = n % 2 != 0
    if is_odd: n -= 1
    count = 0
    middle = n // 2
    stack = [0] * (middle - 1) + [1] + [0] * middle
    left = 1
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

    count += 1  # count zeros as a luck number
    if is_odd: count *= 10

    return count


class LuckyNumberCalculator:
    def __init__(self, n):
        self.is_odd = n % 2 != 0
        if self.is_odd: n -= 1
        self.n = n
        self.middle = n // 2
        self.stack = [0] * (self.middle - 1) + [1] + [0] * self.middle
        self.left = 1
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

        count += 1 # count zeros as a luck number
        if self.is_odd: count *= 10
        return count


if __name__ == "__main__":
    from datetime import datetime
    t = datetime.now()
    print(lucky_number(9))
    #calc = LuckyNumberCalculator(8)
    #print(calc.calculate())
    print(datetime.now() - t)