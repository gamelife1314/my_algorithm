# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: heap_sort.py
@time: 2019/01/20 8:57 PM
"""
from random import randint
from typing import List


def sort(nums: List[int]):
    length = len(nums)
    build_heap(nums, length)
    for i in range(length - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)


def build_heap(nums: List[int], length: int):
    for i in range((length - 2) >> 1, -1, -1):
        heapify(nums, length, i)


def heapify(nums: List[int], length: int, i: int):
    while True:
        max_pos, left, right = i, 2 * i + 1, 2 * i + 2
        if left < length and nums[left] > nums[max_pos]:
            max_pos = left
        if right < length and nums[right] > nums[max_pos]:
            max_pos = right
        if i == max_pos:
            break
        nums[i], nums[max_pos] = nums[max_pos], nums[i]
        i = max_pos


def test():
    for _ in range(1000):
        nums = [randint(0, 10 ** 4) for _ in range(randint(1, 40))]
        result1 = list(sorted(nums))
        sort(nums)
        assert result1 == nums


if __name__ == '__main__':
    test()
