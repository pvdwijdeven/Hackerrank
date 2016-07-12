#
# Write centrality_max to return the maximum distance
# from a node to all the other nodes it can reach
#

def centrality_max(G, v):
    # use DFS
    todo=[v]
    marked={}
    curlevel=0
    while todo:
        curnode=todo[0]
        marked[curnode]=curlevel
        for neighbor in G[curnode]:
            if neighbor not in marked:
                todo.append(neighbor)
        curlevel=+1
        todo.pop(0)
    result=max(marked.values())
    print marked
    print result
    return result

#################
# Testing code
#
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def test():
    chain = ((1,2), (2,3), (3,4), (4,5), (5,6))
    G = {}
    for n1, n2 in chain:
        make_link(G, n1, n2)
    assert centrality_max(G, 1) == 5
    assert centrality_max(G, 3) == 3
    tree = ((1, 2), (1, 3),
            (2, 4), (2, 5),
            (3, 6), (3, 7),
            (4, 8), (4, 9),
            (6, 10), (6, 11))
    G = {}
    for n1, n2 in tree:
        make_link(G, n1, n2)
    assert centrality_max(G, 1) == 3
    assert centrality_max(G, 11) == 6
test()