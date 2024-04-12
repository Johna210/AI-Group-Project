from romania import graph
from collections import deque
import heapq
from math import sqrt

# Depth first search
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

# Breadth first search
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


# Uniform cost search
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


# Heuristic function(manhattan distance) for the greedy search and astar search
def heurisitc(source,destination,graph):
    # A Simple heuristic function that calculates the manhattan distance between two cities
    # By using their latitude and longitude

    s_coordinate = graph.nodes[source]
    d_coordinate = graph.nodes[destination]

    return sqrt((float(s_coordinate[0]) - float(d_coordinate[0]))**2 + abs(float(s_coordinate[1]) - float(d_coordinate[1]))**2)


def coordinate_heuristic(source,destination,g):
    x1,y1 = g.nodes[source]
    x2,y2 = g.nodes[destination]
    return abs(x1-x2) + abs(y1-y2)



# greedy search
def greedy_search(source,destination,graph):
    fringe = []
    visited = set([])
    try:
        heurisitc_function = heurisitc
        h = heurisitc_function(source,destination,graph)
    except:
        heurisitc_function = coordinate_heuristic
        h = coordinate_heuristic(source,destination,graph)

    heapq.heappush(fringe, (h,source))
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
                heapq.heappush(fringe,(heurisitc_function(city,destination,graph),city))
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

# Depth limited search helper function for the iterative deepening search
def depth_limited_search(source,destination,graph,limit):
    stack = []
    visited = set([])
    stack.append((source,0))
    path = {source: None}

    while stack:
        current = stack.pop()
        visited.add(current[0])

        if current[0] == destination:
            break
        if current[1] < limit:
            neighbors = graph.get_neighbours(current[0])
            for neighbor in neighbors:
                city, weight = neighbor
                if city not in visited:
                    stack.append((city,current[1] + 1))
                    path[city] = (current[0],weight)

    if current[0] != destination:
        return None
    else:
        path_list = []
        total_length = 0
        current = current[0]
        while current:
            path_list.append(current)
            if current == None:
                break
            if path[current] == None:
                break
            current,length = path[current][0] , path[current][1]
            total_length += length

        return path_list[::-1],len(visited),total_length

# Iterative deepening search
def ids(source,destination,graph):
    limit = 0
    while True:
        result = depth_limited_search(source,destination,graph,limit)
        if result:
            return result
        limit += 1


# Biderectional search
def bidirectional_search(source,destination,graph):

    # Instantiate two fringes for the source and destination
    source_fringe = deque()
    destination_fringe = deque()

    # The visited set will have both sides of the search but the forward search will have 0 and backward search will have1
    visited = set([])
    source_fringe.append((source,0))
    destination_fringe.append((destination,1))

    # path for both the forward and backward search
    source_path = {source: None}
    destination_path = {destination: None}

    intersection = None

    while source_fringe and destination_fringe:
        # Forward search
        current = source_fringe.popleft()
        visited.add((current[0],0))

        # If the two searches are intersected, break the loop
        if (current[0],1) in visited:
            intersection = current[0]
            break

        neighbors = graph.get_neighbours(current[0])
        for neighbor in neighbors:
            city, weight = neighbor
            if (city,0) not in visited:
                source_fringe.append((city,0))
                source_path[city] = (current[0],weight)

        # Backward search
        current = destination_fringe.popleft()
        visited.add((current[0],1))

        # If the two searches are intersected, break the loop
        if (current[0],0) in visited:
            intersection = current[0]
            break
        
        neighbors = graph.get_neighbours(current[0])

        for neighbor in neighbors:
            city, weight = neighbor
            if (city,1) not in visited:
                destination_fringe.append((city,1))
                destination_path[city] = (current[0],weight)

    # Return path,total_length and nodes visited if the intersection is found
    if intersection:
        path_list = []
        current = intersection
        total_length = 0
        # From the intersection to the source
        while current:
            path_list.append(current)
            if current == None:
                break
            if source_path[current] == None:
                break
            current,length = source_path[current][0] , source_path[current][1]
            total_length += length

        path_list = path_list[::-1]
        current = intersection
        # From the intersection to the destination
        while current:
            if destination_path[current] == None:
                break
            current,length = destination_path[current][0] , destination_path[current][1]
            path_list.append(current)
            total_length += length

        return path_list,len(visited),total_length  

# A* search
def astar(source,destination,graph,heurisitc=heurisitc):
    fringe = []
    visited = set([])
    # Push the heuristic function + cost, current cost, source and current path
    try:
        h = heurisitc(source,destination,graph)
    except:
        h = coordinate_heuristic(source,destination,graph)
    heapq.heappush(fringe,(h,0,source, [source]))

    while fringe:
        current = heapq.heappop(fringe)
        visited.add(current[2])

        if current[2] == destination:
            return current[3],len(visited),current[1]
        
        neighbors = graph.get_neighbours(current[2])
        for neighbor in neighbors:
            city, weight = neighbor
            if city not in visited:
                g = current[1] + weight
                h = heurisitc(city,destination,graph)
                path = current[3] + [city]
                heapq.heappush(fringe,((g + h),g,city,path))



# print("From Arad to Bucharest")
# # print(f"With dfs {dfs("Arad","Bucharest",graph)}")
# print(f"With bfs {bfs("Arad","Bucharest",graph)}")
# print(f"With ufs {ucs("Arad","Bucharest",graph)}")
# print(f"With greedy_search {greedy_search("Arad","Bucharest",graph)}")
# # print(f"With ids {ids("Arad","Bucharest",graph)}")
# # print(f"With biderectional search {bidirectional_search("Arad","Bucharest",graph)}")
# print(f"With A* {astar("Arad","Bucharest",graph)}")

# print()

# print("From Arad to Oradea")
# # print(f"With dfs {dfs("Arad","Oradea",graph)}")
# print(f"With bfs {bfs("Arad","Oradea",graph)}")
# print(f"With ucs {ucs("Arad","Oradea",graph)}")
# print(f"With greedy_search {greedy_search("Arad","Oradea",graph)}")
# # print(f"With ids {ids("Arad","Oradea",graph)}")
# # print(f"With biderectional search {bidirectional_search("Arad","Oradea",graph)}")
# print(f"With A* {astar("Arad","Oradea",graph)}")


   


