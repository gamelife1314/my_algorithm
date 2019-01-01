# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: stack.py
@time: 2019/01/01 7:01 PM
"""


class Stack:

    __slots__ = ('__data', )

    def __init__(self):
        self.__data = []

    def push(self, value):
        self.__data.append(value)

    def pop(self):
        if len(self.__data) == 0:
            return None
        return self.__data.pop()

    def top(self):
        if len(self.__data) == 0:
            return None
        return self.__data[-1]

