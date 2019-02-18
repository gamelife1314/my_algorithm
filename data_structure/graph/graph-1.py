# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: graph-1.py
@time: 2019/02/17 8:53 PM
"""

from typing import List, Optional, Generator
from collections import deque


class Graph(object):

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adjacency = [[] for _ in range(self.num_vertices)]

    def add_edge(self, s: int, t: int):
        if 0 <= s < self.num_vertices - 1 and 0 <= t < self.num_vertices - 1:
            self.adjacency[s].append(t)
            self.adjacency[t].append(s)

    def __generate_path(self, s: int, t: int, prev: List[Optional[int]]) -> Generator[str, None, None]:
        if prev[t] or s != t:
            self.__generate_path(s, prev[t], prev)
        yield str(t)

    def bfs(self, s: int, t: int):
        if s == t: return
        visited = [False] * self.num_vertices
        visited[s] = True
        queue = deque()
        queue.append(s)
        prev = [None] * self.num_vertices
        while queue:
            v = queue.popleft()
            for neighbour in self.adjacency[v]:
                if not visited[neighbour]:
                    prev[neighbour] = v
                    if neighbour == t:
                        print('->'.join(self.__generate_path(s, t, prev)))
                        return
                    visited[neighbour] = True
                    queue.append(neighbour)

    def dfs(self, s: int, t: int):
        visited = [False] * self.num_vertices
        prev = [None] * self.num_vertices

        def _dfs(from_vertex):
            visited[from_vertex] = True
            if from_vertex == t: return
            for neighbour in self.adjacency[from_vertex]:
                if not visited[neighbour]:
                    prev[neighbour] = from_vertex
                    _dfs(neighbour)

        _dfs(s)
        print('->'.join(self.__generate_path(s, t, prev)))
