# Bridge Edges v4
#
# Find the bridge edges in a graph given the
# algorithm in lecture.
# Complete the intermediate steps
#  - create_rooted_spanning_tree
#  - post_order
#  - number_of_descendants
#  - lowest_post_order
#  - highest_post_order
#
# And then combine them together in
# `bridge_edges`

# So far, we've represented graphs
# as a dictionary where graph[n1][n2] == 1
# meant there was an edge between n1 and n2
#
# In order to represent a spanning tree
# we need to create two classes of edges
# we'll refer to them as "green" and "red"
# for the green and red edges as specified in lecture
#
# So, for example, the graph given in lecture
# graph = {'a': {'c': 1, 'b': 1},
#      'b': {'a': 1, 'd': 1},
#      'c': {'a': 1, 'd': 1},
#      'd': {'c': 1, 'b': 1, 'e': 1},
#      'e': {'d': 1, 'g': 1, 'f': 1},
#      'f': {'e': 1, 'g': 1},
#      'g': {'e': 1, 'f': 1}
#      }
# would be written as a spanning tree
# spanning_tree = {'a': {'c': 'green', 'b': 'green'},
#      'b': {'a': 'green', 'd': 'red'},
#      'c': {'a': 'green', 'd': 'green'},
#      'd': {'c': 'green', 'b': 'red', 'e': 'green'},
#      'e': {'d': 'green', 'g': 'green', 'f': 'green'},
#      'f': {'e': 'green', 'g': 'red'},
#      'g': {'e': 'green', 'f': 'red'}
#      }
#


def create_rooted_spanning_tree(graph, root):
    spanning_tree = {}
    marked = {}
    todo = [root]
    while todo:
        cur_node = todo.pop(0)
        marked[cur_node] = True
        spanning_tree[cur_node] = {}
        found = False
        for x in graph[cur_node]:
            if x in marked:
                if not found:
                    found = True
                    spanning_tree[cur_node][x] = "green"
                else:
                    spanning_tree[cur_node][x] = "red"
                    spanning_tree[x][cur_node] = "red"
            else:
                spanning_tree[cur_node][x] = "green"
                todo.append(x)
    return spanning_tree


# This is just one possible solution
# There are other ways to create a
# spanning tree, and the grader will
# accept any valid result
# feel free to edit the test to
# match the solution your program produces
def test_create_rooted_spanning_tree():
    graph = {'a': {'c': 1, 'b': 1},
             'b': {'a': 1, 'd': 1},
             'c': {'a': 1, 'd': 1},
             'd': {'c': 1, 'b': 1, 'e': 1},
             'e': {'d': 1, 'g': 1, 'f': 1},
             'f': {'e': 1, 'g': 1},
             'g': {'e': 1, 'f': 1}
             }
    spanning_tree = create_rooted_spanning_tree(graph, "a")
    assert spanning_tree == {'a': {'c': 'green', 'b': 'green'},
                             'b': {'a': 'green', 'd': 'red'},
                             'c': {'a': 'green', 'd': 'green'},
                             'd': {'c': 'green', 'b': 'red', 'e': 'green'},
                             'e': {'d': 'green', 'g': 'green', 'f': 'green'},
                             'f': {'e': 'green', 'g': 'red'},
                             'g': {'e': 'green', 'f': 'red'}
                             }


###########


def mark_node(graph, v, marked, level, po, po_num):
    marked[v] = level
    for x in sorted(graph[v]):
        if graph[v][x] != "red":
            if x not in marked:
                marked[x] = level
                mark_node(graph, x, marked, level + 1, po, po_num)
    po[v] = len(po.keys()) + 1
    return marked


def post_order(spanning_tree, root):
    # return mapping between nodes of spanning_tree and the post-order value
    # of that node
    po = {}
    marked = mark_node(spanning_tree, root, {}, 1, po, 1)
    return po


# This is just one possible solution
# There are other ways to create a
# spanning tree, and the grader will
# accept any valid result.
# feel free to edit the test to
# match the solution your program produces
def test_post_order():
    spanning_tree = {'a': {'c': 'green', 'b': 'green'},
                     'b': {'a': 'green', 'd': 'red'},
                     'c': {'a': 'green', 'd': 'green'},
                     'd': {'c': 'green', 'b': 'red', 'e': 'green'},
                     'e': {'d': 'green', 'g': 'green', 'f': 'green'},
                     'f': {'e': 'green', 'g': 'red'},
                     'g': {'e': 'green', 'f': 'red'}
                     }
    po = post_order(spanning_tree, 'a')
    assert po == {'a': 7, 'b': 1, 'c': 6, 'd': 5, 'e': 4, 'f': 2, 'g': 3}


##############

def number_of_descendants(spanning_tree, root):
    # return mapping between nodes of spanning_tree and the number of descendants
    # of that node
    nd = 0
    return nd


def test_number_of_descendants():
    spanning_tree = {'a': {'c': 'green', 'b': 'green'},
                     'b': {'a': 'green', 'd': 'red'},
                     'c': {'a': 'green', 'd': 'green'},
                     'd': {'c': 'green', 'b': 'red', 'e': 'green'},
                     'e': {'d': 'green', 'g': 'green', 'f': 'green'},
                     'f': {'e': 'green', 'g': 'red'},
                     'g': {'e': 'green', 'f': 'red'}
                     }
    nd = number_of_descendants(spanning_tree, 'a')
    assert nd == {'a': 7, 'b': 1, 'c': 5, 'd': 4, 'e': 3, 'f': 1, 'g': 1}


###############

def lowest_post_order(spanning_tree, root, po):
    # return a mapping of the nodes in spanning_tree
    # to the lowest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    lp = 0
    return lp


def test_lowest_post_order():
    spanning_tree = {'a': {'c': 'green', 'b': 'green'},
                     'b': {'a': 'green', 'd': 'red'},
                     'c': {'a': 'green', 'd': 'green'},
                     'd': {'c': 'green', 'b': 'red', 'e': 'green'},
                     'e': {'d': 'green', 'g': 'green', 'f': 'green'},
                     'f': {'e': 'green', 'g': 'red'},
                     'g': {'e': 'green', 'f': 'red'}
                     }
    po = post_order(spanning_tree, 'a')
    l = lowest_post_order(spanning_tree, 'a', po)
    assert l == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2}


################

def highest_post_order(spanning_tree, root, po):
    # return a mapping of the nodes in spanning_tree
    # to the highest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    hp = 0
    return hp


def test_highest_post_order():
    spanning_tree = {'a': {'c': 'green', 'b': 'green'},
                     'b': {'a': 'green', 'd': 'red'},
                     'c': {'a': 'green', 'd': 'green'},
                     'd': {'c': 'green', 'b': 'red', 'e': 'green'},
                     'e': {'d': 'green', 'g': 'green', 'f': 'green'},
                     'f': {'e': 'green', 'g': 'red'},
                     'g': {'e': 'green', 'f': 'red'}
                     }
    po = post_order(spanning_tree, 'a')
    h = highest_post_order(spanning_tree, 'a', po)
    assert h == {'a': 7, 'b': 5, 'c': 6, 'd': 5, 'e': 4, 'f': 3, 'g': 3}


#################

def bridge_edges(graph, root):
    # use the four functions above
    # and then determine which edges in graph are bridge edges
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]
    bridges = []
    return bridges


def test_bridge_edges():
    graph = {'a': {'c': 1, 'b': 1},
             'b': {'a': 1, 'd': 1},
             'c': {'a': 1, 'd': 1},
             'd': {'c': 1, 'b': 1, 'e': 1},
             'e': {'d': 1, 'g': 1, 'f': 1},
             'f': {'e': 1, 'g': 1},
             'g': {'e': 1, 'f': 1}
             }
    bridges = bridge_edges(graph, 'a')
    assert bridges == [('d', 'e')]


test_create_rooted_spanning_tree()
test_post_order()
