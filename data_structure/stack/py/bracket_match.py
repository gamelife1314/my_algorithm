# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: bracket_match.py
@time: 2019/01/01 7:12 PM
"""


class Stack:

    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data) == 0:
            return None
        return self.data.pop()


def check(expr):
    matches = {
        '[': ']',
        '(': ')',
        '{': '}',
    }
    stack = Stack()
    for char in expr:
        if char in matches:
            stack.push(char)
        else:
            top = stack.pop()
            if top is None or matches[top] != char:
                return False

    return stack.pop() is None


def test():
    assert check('{[{}]}') is True
    assert check('{[}]}') is False
    assert check('{[{)]}') is False
    assert check(']') is False
    assert check('{') is False
    assert check('{}[]()') is True


if __name__ == '__main__':
    test()
