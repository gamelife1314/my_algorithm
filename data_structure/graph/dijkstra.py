# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: dijkstra.py
@time: 2019/02/17 9:41 PM
"""

from typing import List, Generator, Optional
import heapq


class Edge(object):

    def __init__(self, source: int, target: int, weight: int) -> None:
        self.source = source
        self.target = target
        self.weight = weight


class Graph(object):

    def __init__(self, vertex_count: int) -> None:
        self.adjacency = [[] for _ in range(vertex_count)]

    def add_edge(self, s: int, t: int, w: int)-> None:
        edge = Edge(s, t, w)
        self.adjacency[s].append(edge)

    def __len__(self):
        return len(self.adjacency)


class Vertex:

    def __init__(self, v: int, dist: float) -> None:
        self.id = v
        self.dist = dist

    def __gt__(self, other):
        return self.dist > other.dist

    def __repr__(self):
        return str((self.id, self.dist))


class PriorityQueue:

    def __init__(self):
        self.vertices = []

    def get(self) -> Vertex:
        return heapq.heappop(self.vertices)

    def put(self, v: Vertex):
        self.vertices.append(v)
        self.update_priority()

    def update_priority(self):
        heapq.heapify(self.vertices)

    def empty(self):
        return len(self.vertices) == 0

    def __repr__(self):
        return str(self.vertices)


def dijkstra(graph: Graph, s: int, t: int):
    length = len(graph)
    pq = PriorityQueue()
    in_queue = [False] * length
    vertices = [Vertex(v, float('inf')) for v in range(length)]
    predecessor = [None] * length
    vertices[s].dist = 0
    pq.put(vertices[s])
    in_queue[s] = True

    while not pq.empty():
        v = pq.get()
        if v.id == t:
            break
        for edge in graph.adjacency[v.id]:
            if v.dist + edge.weight < vertices[edge.target].dist:
                vertices[edge.target].dist = v.dist + edge.weight
                predecessor[edge.target] = v.id
                pq.update_priority()
            if not in_queue[edge.target]:
                in_queue[edge.target] = True
                pq.put(vertices[edge.target])

    print('->'.join(generate_path(s, t, predecessor)))

    return vertices[t].dist


def generate_path(s: int, t: int, prev: List[Optional[int]]) -> Generator[str, None, None]:
    if prev[t] or s != t:
        yield from generate_path(s, prev[t], prev)
    yield str(t)


if __name__ == '__main__':
    graph = Graph(6)
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 4, 15)
    graph.add_edge(1, 2, 15)
    graph.add_edge(1, 3, 2)
    graph.add_edge(2, 5, 5)
    graph.add_edge(3, 2, 1)
    graph.add_edge(3, 5, 12)
    graph.add_edge(4, 5, 10)
    print(dijkstra(graph, 0, 5))

