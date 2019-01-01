# -*- coding:utf-8 -*-

"""

表达式求值，用于计算类似：1 + 2 * 4 - 6 这样的表达式

@author: 付登龙
@file: expression.py
@time: 2019/01/01 6:20 PM
"""
import operator as op


class Stack:

    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data) == 0:
            return None
        return self.data.pop()

    def top(self):
        if len(self.data) == 0:
            return None
        return self.data[-1]


def expression(expr: list):
    operators, operand = Stack(), Stack()
    priorities = {
        '-': 1,
        '+': 1,
        '*': 2,
        '/': 2,
    }
    cal = {
        '-': op.sub,
        '+': op.add,
        '*': op.mul,
        '/': op.truediv,
    }
    expr = list(reversed(expr))

    def do():
        right_operand = operand.pop()
        left_operand = operand.pop()
        operator = operators.pop()
        operand.push(cal[operator](left_operand, right_operand))

    while len(expr) > 0:
        char = expr.pop()
        if char not in priorities:
            operand.push(char)
        else:
            operators_top = operators.top()
            if operators_top is None or priorities[char] > priorities[operators_top]:
                operators.push(char)
            else:
                do()
                expr.append(char)

    while operators.top() is not None:
        do()

    return operand.top()


def test():
    assert expression([1, '+', 2, '-', 3, '*', 4, '+', 5]) == -4
    assert expression([1, '*', 2]) == 2
    assert expression([1, '+', 2]) == 3
    assert expression([1, '-', 2]) == -1
    assert expression([1, '/', 2]) == 0.5
    assert expression([1, '+', 2, '*', 2]) == 5
    assert expression([1, '*', 2, '-', 3]) == -1


if __name__ == '__main__':
    test()
