# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/03/07 11:19 PM
"""
from collections import defaultdict
from typing import List


class Solution:

    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        if N == 1: return 1

        p, n = {}, defaultdict(list)

        for a, b in trust:
            p[a] = True
            n[b].append(a)

        for m, items in n.items():
            if len(set([m] + items)) == N and m not in p:
                return m

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))
