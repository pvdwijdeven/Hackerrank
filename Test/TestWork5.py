#!/usr/bin/python
import random
import csv
import time


def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


def read_graph(filename):
    tsv = csv.reader(open(filename), delimiter='\t')
    graph_ = {}
    actors_ = {}
    movies_ = {}
    for (actor_, movie_name, year) in tsv:
        movie = str(movie_name) + ", " + str(year)
        actors_[actor_] = 1
        movies_[movie] = 1
        make_link(graph_, actor_, movie)
    return graph_, actors_, movies_


def centrality(G, v):
    distance_from_start = {}
    distance_from_start[v] = 0
    open_list = [v]
    while len(open_list) > 0:
        current = open_list.pop(0)
        for neighbour in G[current].keys():
            if neighbour not in distance_from_start:
                distance_from_start[neighbour] = distance_from_start[current] + 1
                open_list.append(neighbour)
    return (float(sum(distance_from_start.values()))) / len(distance_from_start)


def bfs_iterative_levels(graph, root):
    visited = {root:0}
    todo = [root]
    while todo:
        cur_node = todo.pop(0)
        for child in graph[cur_node]:
            if child not in visited:
                todo.append(child)
                visited[child] = visited[cur_node]+1
    return (float(sum(visited.values()))) / len(visited)


def rank(my_list, v):
    r = 0
    for l in my_list:
        if l < v:
            r += 1
    return r


def find_rank(my_list, i):
    lt = {}
    eq = {}
    gt = {}
    v = random.choice(my_list.keys())
    for l in my_list.keys():
        if my_list[l] < my_list[v]:
            lt[l] = my_list[l]
        elif my_list[l] == my_list[v]:
            eq[l] = my_list[l]
        elif my_list[l] > my_list[v]:
            gt[l] = my_list[l]
    if len(lt) >= i:
        return find_rank(lt, i)
    elif len(lt) + len(eq) >= i:
        return v
    else:
        return find_rank(gt, i - len(lt) - len(eq))


def read_file():
    actors_ = {}
    movies_ = {}
    f = open("actors.tsv")
    for line in f:
        actor, movie, year = line.strip().split('\t')
        movie = ' '.join([movie, year])
        if actor in actors_:
            actors_[actor].append(movie)
        else:
            actors_[actor] = [movie]
        if movie in movies_:
            movies_[movie].append(actor)
        else:
            movies_[movie] = [actor]
    return actors_, movies_


def create_graph(actors_, movies_):
    graph = {}
    for actor in actors_:
        for movie in actors_[actor]:
            if actor not in graph:
                graph[actor] = set()
            for x in movies_[movie]:
                if x != actor:
                    graph[actor].add(x)
    for actor in graph:
        graph[actor]=list(graph[actor])
    return graph


start = time.time()
(G, actors, movies) = read_graph("actors.tsv")
centralities = {}
y=len(actors)
for i,actor in enumerate(actors.keys()):
    centralities[actor] = bfs_iterative_levels(G, actor)
    print i, y
actor_index = find_rank(centralities, 20)
print actor_index
print centralities[actor_index]
print time.time() - start
start = time.time()
actors, movies = read_file()
graph = create_graph(actors, movies)
print "lap time:", time.time()-start
centralities = {}
y=len(actors)
for i,actor in enumerate(actors.keys()):
    centralities[actor] = centrality(graph, actor)
    print i, y
actor_index = find_rank(centralities, 20)
print actor_index
print centralities[actor_index]
print time.time() - start
