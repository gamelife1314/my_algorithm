# -*- coding:utf-8 -*-

"""
@author: 付登龙
@file: graph.py
@time: 2019/01/28 10:29 PM
"""

from typing import List, Optional, Generator
from collections import deque


class Graph:

    """
    undirected graph
    """

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adjacency = [[] for _ in range(self.num_vertices)]

    def add_edge(self, s: int, t: int):
        self.adjacency[s].append(t)
        self.adjacency[t].append(s)

    def __generate_path(self, s: int, t: int, prev: List[Optional[int]]) -> Generator[str, None, None]:
        if prev[t] or s != t:
            yield from self.__generate_path(s, prev[t], prev)
        yield str(t)

    def bfs(self, s: int, t: int):
        if s == t:
            return
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
                        print(prev)
                        print("->".join(self.__generate_path(s, t, prev)))
                        return
                    visited[neighbour] = True
                    queue.append(neighbour)

    def dfs(self, s: int, t: int):
        visited = [False] * self.num_vertices
        prev = [None] * self.num_vertices

        def _dfs(from_vertex) -> None:
            visited[from_vertex] = True
            if from_vertex == t:
                return
            for neighbour in self.adjacency[from_vertex]:
                if not visited[neighbour]:
                    prev[neighbour] = from_vertex
                    _dfs(neighbour)
        _dfs(s)
        print("->".join(self.__generate_path(s, t, prev)))


if __name__ == '__main__':
    graph = Graph(8)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 7)
    graph.bfs(0, 7)
    graph.dfs(0, 7)
