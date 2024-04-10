from romania import graph
from collections import deque
import heapq

def dfs(source, destination,graph):
    stack = []
    visited = set([])
    stack.append(source)
    # path is a dictionary that stores the path from the source to the current node
    path = {source: None}

    while stack:
        # Pop and expand the current node
        current = stack.pop()
        visited.add(current)

        if current == destination:
            break
        # Get the neighbors of the current node 
        neighbors = graph.get_neighbours(current)
        for neighbor in neighbors:
            city, weight = neighbor
            if city not in visited:
                stack.append(city)
                path[city] = (current,weight)

    # If the destination is not found, return None
    if current != destination:  
        return None
    else:
        path_list = []
        total_length = 0
        while current:
            path_list.append(current)
            if path[current] == None:
                break
            current , length = path[current][0],path[current][1]
            total_length += length

        # return the path, the number of nodes visited and the total length
        return path_list[::-1],len(visited),total_length


def bfs(source,destination,graph):
    fringe = deque()
    visited = set([])
    fringe.append(source)
    path = {source: None}

    while fringe:
        current = fringe.popleft()
        visited.add(current)

        if current == destination:
            break
        neighbors = graph.get_neighbours(current)
        for neighbor in neighbors:
            city, weight = neighbor
            if city not in visited:
                fringe.append(city)
                path[city] = (current,weight)

    if current != destination:
        return None
    else:
        path_list = []
        total_length = 0
        while current:
            path_list.append(current)
            if path[current] == None:
                break
            current , length = path[current][0],path[current][1]
            total_length += length

        return path_list[::-1],len(visited),total_length



def ucs(source,destination,graph):
    # use priority queue data structure to implement ucs by using heapq module
    fringe = []
    visited = set([])
    heapq.heappush(fringe,(0,source))
    path = {source: None}

    while fringe:
        current = heapq.heappop(fringe)
        visited.add(current[1])

        if current[1] == destination:
            break
        neighbors = graph.get_neighbours(current[1])
        for neighbor in neighbors:
            city, weight = neighbor
            if city not in visited:
                heapq.heappush(fringe,(current[0] + weight,city))
                path[city] = (current[1],weight)

    if current[1] != destination:
        return None
    else:
        path_list = []
        total_length = 0
        current = current[1]
        while current:
            path_list.append(current)
            if current == None:
                break
            if path[current] == None:
                break
            current,length = path[current][0] , path[current][1]
            total_length += length

        return path_list[::-1],len(visited),total_length

def heurisitc(source,destination):
    s = graph.nodes[source]
    d = graph.nodes[destination]

    return (float(s[0]) - float(d[0]) + float(s[1]) - float(d[1]))


def greedy_search(source,destination,graph):
    fringe = []
    visited = set([])
    heapq.heappush(fringe, (-1 *heurisitc(source,destination),source))
    path = {source: None}

    while fringe:
        current = heapq.heappop(fringe)
        visited.add(current[1])

        if current[1] == destination:
            break
        neighbors = graph.get_neighbours(current[1])
        for neighbor in neighbors:
            city, weight = neighbor
            if city not in visited:
                # because we want to get the minimum value, we need to multiply the heuristic value by -1
                heapq.heappush(fringe,(-1 * heurisitc(city,destination),city))
                path[city] = (current[1],weight)

    if current[1] != destination:
        return None
    else:
        path_list = []
        total_length = 0
        current = current[1]
        while current:
            path_list.append(current)
            if current == None:
                break
            if path[current] == None:
                break
            current,length = path[current][0] , path[current][1]
            total_length += length

        return path_list[::-1],len(visited),total_length

print("From Arad to Bucharest")
print(f"With dfs {dfs("Arad","Bucharest",graph)}")
print(f"With bfs {bfs("Arad","Bucharest",graph)}")
print(f"With ufs {ucs("Arad","Bucharest",graph)}")
print(f"With greedy_search {greedy_search("Arad","Bucharest",graph)}")

print()

print("From Arad to Oradea")
print(f"With dfs {dfs("Arad","Fagaras",graph)}")
print(f"With bfs {bfs("Arad","Fagaras",graph)}")
print(f"With ucs {ucs("Arad","Fagaras",graph)}")
print(f"With greedy_search {greedy_search("Arad","Fagaras",graph)}")

def astar():
    pass

def ids():
    pass

def bs():
    pass

