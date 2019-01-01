# -*- coding:utf-8 -*-


class Stack:

    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data) == 0:
            return None
        return self.data.pop()

    def empty(self):
        self.data = []


class Browser:

    def __init__(self):
        self.x = Stack()
        self.y = Stack()

    def open(self, page):
        self.y.empty()
        self.x.append(page)

    def back(self):
        top = self.x.pop()
        if top is not None:
            self.y.append(top)
        return top

    def move(self):
        top = self.y.pop()
        if top is not None:
            self.x.append(top)
        return top
