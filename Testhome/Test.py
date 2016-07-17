import sys


def bfs(graph_, start_node, end_node):
    if start_node not in graph_ or end_node not in graph:
        return []
    visited = {start_node: None}
    queue = [start_node]
    while queue:
        node = queue.pop(0)
        if node == end_node:
            path = []
            while node is not None:
                path.append(node)
                node = visited[node]
            return path[::-1]
        for neighbour in graph_[node]:
            if neighbour not in visited:
                visited[neighbour] = node
                queue.append(neighbour)
    return []


def edge_to_graph(graph_, edge_):
    node1 = edge_[0]
    node2 = edge_[1]
    if node1 not in graph_:
        graph_[node1] = []
    if node2 not in graph_:
        graph_[node2] = []
    if node2 not in graph_[node1]:
        graph_[node1].append(node2)
    if node1 not in graph_[node2]:
        graph_[node2].append(node1)

import sys
f = sys.stdin
T = int(f.readline())
for t in xrange(T):
    N,M = map(int,f.readline().split())
    edges=[]
    for m in xrange(M):
        edges.append(map(int,f.readline().split()))
    start_node=int(f.readline())
    graph={}
    for x in edges:
        edge_to_graph(graph,x)

    for i in xrange(1,N+1):
        if i!=start_node:
            dist = bfs(graph, start_node, i)
            if dist:
                print (len(dist) - 1)*6,
            else:
                print -1,
    print
