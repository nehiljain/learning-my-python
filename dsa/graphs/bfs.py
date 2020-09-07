from typing import List, Dict
from collections import deque

class Graph:

  def __init__(self, graph: Dict[int, tuple]):
    self.graph = graph

  def get_vertices(self):
    return self.graph.keys()

  def add_edge(self, u, v):
    self.graph[u].append(v)
    self.graph[v].append(u)

  def get_adj_vertices(self, u):
    return self.graph.get(u, [])


def bfs(g, v, visited:set()):

  q = deque()
  q.append(v)
  visited.add(u)
  parent = {v: None for v in g.get_vertices}

  while q:

    u = q.pop()
    for v in g.get_adj_vertices(u):

      if v not in visited:
        visited.add(v)
        q.append(v)
        parent[v] = u
      elif parent[u] != v
        raise Excepption('Cycle found')

