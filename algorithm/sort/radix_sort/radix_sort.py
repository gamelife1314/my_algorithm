# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: radix_sort.py
@time: 2019/01/03 11:37 AM
"""

from typing import List
from random import randint


def radix_sort_word(words: List[str]):

    max_len = len(max(words, key=lambda word: len(word)))
    words = list(map(lambda word: word + '0' * (max_len - len(word)), words))
    for i in range(max_len - 1, -1, -1):
        words.sort(key=lambda word: word[i])

    words = list(map(lambda word: word.strip('0'), words))
    return words


def rand_word(min_=1, max_=20):
    length = randint(min_, max_)
    word = ''
    for _ in range(1, length):
        word += chr(randint(ord('a'), ord('z')))
    return word


def test():
    for _ in range(50):
        w = [rand_word() for _ in range(10)]
        assert list(sorted(w)) == radix_sort_word(w)


if __name__ == '__main__':
    test()
