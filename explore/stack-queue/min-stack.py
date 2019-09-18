# -*- coding: utf-8 -*-


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        if self.min is None or self.min > x:
            self.min = x
        self.stack.append((self.min, x))

    def pop(self) -> None:
        self.stack.pop()
        if not self.stack:
            self.min = None
        elif self.stack[-1][0] > self.min:
            self.min = self.stack[-1][0]

    def top(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        return self.min
