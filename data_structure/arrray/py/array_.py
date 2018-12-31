# -*- coding:utf-8 -*-

import sys
from array import array
from random import random

if __name__ == '__main__':
    arr = array('d', (random() for i in range(10 ** 6)))
    lst = [random() for i in range(10 ** 6)]
    print("arr: ", sys.getsizeof(arr), "list: ", sys.getsizeof(lst))
    arr1 = array('h', [1, 2])
    arr1_bytes = arr1.tobytes()
    print(arr1_bytes)
    arr2 = array('h')
    arr2.frombytes(arr1_bytes)
    print(arr2[0])
