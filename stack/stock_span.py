# https://leetcode.com/problems/online-stock-span


class StockSpanner:
    def __init__(self):
        # Initialize an empty stack to store prices and their corresponding indices.
        self.stack = []
        self.index = -1

    def next(self, price: int) -> int:
        self.index += 1

        # Pop prices from the stack that are less than or equal to the current price.
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        # If the stack is not empty, calculate the span by subtracting the current index
        # from the index of the last price greater than the current price.
        if self.stack:
            res = self.index - self.stack[-1][1]
        else:
            # If the stack is empty, it means there are no previous prices greater
            # than the current price, so the span is the current index + 1.
            res = self.index + 1

        # Push the current price and its index onto the stack.
        self.stack.append((price, self.index))
        return res
