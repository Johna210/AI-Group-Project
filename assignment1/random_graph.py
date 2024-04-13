from graph import RandomGraph
import random
from search import dfs, bfs, ucs, astar, ids, greedy_search,bidirectional_search
import time

def generate_random_graph(nodes,probability):
    graph = RandomGraph()
    generated_coordinates = set([])
    for i in range(1,nodes+1):
        coor = generate_random_coordinates()
        while coor in generated_coordinates:
            coor = generate_random_coordinates()
        graph.add_node(i,coor)

    for i in range(1,nodes+1):
        for j in range(1,nodes+1):
            if i == j: 
                continue
            elif random.random() < probability:
                if j not in graph.get_neighbours(i):
                    graph.add_edge(i,j,generate_random_weight())
    return graph

def generate_random_weight():
    return random.randint(1,10)

def generate_random_coordinates():
    return (random.randint(0,100),random.randint(0,100))


# g10_02 = generate_random_graph(10,0.2)
# g10_04 = generate_random_graph(10,0.4)
# g10_06 = generate_random_graph(10,0.6)
# g10_08 = generate_random_graph(10,0.8)


# for _ in range(1,10):
#     source = random.randint(1,10)
#     destination = random.randint(1,10)

#     print(f"From Source {source} to Destination {destination}")
#     print("------------------------------------")
#     start = time.perf_counter()
#     is_found = dfs(source,destination,g10_02)
#     end = time.perf_counter()
#     if not is_found:
#         continue
#     print(f"dfs{is_found} time taken = {(end-start)* 10 ** 6}")
#     start = time.perf_counter()
#     print(f"bfs{bfs(source,destination,g10_02)} time taken = {(time.perf_counter() -start) * 10 ** 6}")
#     start = time.perf_counter()
#     print(f"ucs{ucs(source,destination,g10_02)} time taken = {(time.perf_counter() -start) * 10 ** 6}")
#     start = time.perf_counter()
#     print(f"A*{astar(source,destination,g10_02)} time taken = {(time.perf_counter() -start) * 10 ** 6}")
#     start = time.perf_counter()
#     print(f"ids{ids(source,destination,g10_02)} time taken = {(time.perf_counter() -start) * 10 ** 6}")
#     start = time.perf_counter()
#     print(f"Greedy{greedy_search(source,destination,g10_02)} time taken = {(time.perf_counter() -start) * 10 ** 6}")
#     start = time.perf_counter()
#     print(f"bidirectional{bidirectional_search(source,destination,g10_02)} time taken = {(time.perf_counter() -start) * 10 ** 6}")
#     print("\n\n")

# print("\n")
# print("With 0.4 probability")

# for _ in range(1,10):
#     source = random.randint(1,10)
#     destination = random.randint(1,10)

#     print(f"From Source {source} to Destination {destination}")
#     print("------------------------------------")
#     start = time.perf_counter()
#     is_found = dfs(source,destination,g10_04)
#     end = time.perf_counter()
#     if not is_found:
#         continue    
#     print(f"dfs{is_found} time taken = {(end-start)* 10 ** 6}")
#     start = time.perf_counter()
#     print(f"bfs{bfs(source,destination,g10_04)} time taken = {(time.perf_counter() -start) * 10 ** 6}")
#     start = time.perf_counter()
#     print(f"ucs{ucs(source,destination,g10_04)} time taken = {(time.perf_counter() -start) * 10 ** 6}")
#     start = time.perf_counter()
#     print(f"A*{astar(source,destination,g10_04)} time taken = {(time.perf_counter() -start) * 10 ** 6}")
#     start = time.perf_counter()
#     print(f"ids{ids(source,destination,g10_04)} time taken = {(time.perf_counter() -start) * 10 ** 6}")
#     start = time.perf_counter()
#     print(f"Greedy{greedy_search(source,destination,g10_04)} time taken = {(time.perf_counter() -start) * 10 ** 6}")
#     start = time.perf_counter()
#     print(f"bidirectional{bidirectional_search(source,destination,g10_04)} time taken = {(time.perf_counter() -start) * 10 ** 6}")
#     print("\n\n")


# print("\n")
# print("With 0.6 probability")

# for _ in range(1,10):
#     source = random.randint(1,10)
#     destination = random.randint(1,10)

#     print(f"From Source {source} to Destination {destination}")
#     print("------------------------------------")
#     start = time.perf_counter()
#     is_found = dfs(source,destination,g10_06)
#     end = time.perf_counter()
#     if not is_found:
#         continue
#     print(f"dfs{is_found} time taken = {(end-start)* 10 ** 6}")
#     start = time.perf_counter()
#     print(f"bfs{bfs(source,destination,g10_06)} time taken = {(time.perf_counter() -start) * 10 ** 6}")
#     start = time.perf_counter()
#     print(f"ucs{ucs(source,destination,g10_06)} time taken = {(time.perf_counter() -start) * 10 ** 6}")
#     start = time.perf_counter()
#     print(f"A*{astar(source,destination,g10_06)} time taken = {(time.perf_counter() -start) * 10 ** 6}")
#     start = time.perf_counter()
#     print(f"ids{ids(source,destination,g10_06)} time taken = {(time.perf_counter() -start) * 10 ** 6}")
#     start = time.perf_counter()
#     print(f"Greedy{greedy_search(source,destination,g10_06)} time taken = {(time.perf_counter() -start) * 10 ** 6}")
#     start = time.perf_counter()
#     print(f"bidirectional{bidirectional_search(source,destination,g10_06)} time taken = {(time.perf_counter() -start) * 10 ** 6}")
#     print("\n\n")

# print("\n")
# print("With 0.8 probability")

# for _ in range(1,10):
#     source = random.randint(1,10)
#     destination = random.randint(1,10)

#     print(f"From Source {source} to Destination {destination}")
#     print("------------------------------------")
#     start = time.perf_counter()
#     is_found = dfs(source,destination,g10_08)
#     end = time.perf_counter()
#     if not is_found:
#         continue
#     print(f"dfs{is_found} time taken = {(end-start)*10 ** 5}")
#     start = time.perf_counter()
#     print(f"bfs{bfs(source,destination,g10_08)} time taken = {(time.perf_counter() -start)*10 ** 5}")
#     start = time.perf_counter()
#     print(f"ucs{ucs(source,destination,g10_08)} time taken = {(time.perf_counter() -start)*10 ** 5}")
#     start = time.perf_counter()
#     print(f"A*{astar(source,destination,g10_08)} time taken = {(time.perf_counter() -start)*10 ** 5}")
#     start = time.perf_counter()
#     print(f"ids{ids(source,destination,g10_08)} time taken = {(time.perf_counter() -start)*10 ** 5}")
#     start = time.perf_counter()
#     print(f"Greedy{greedy_search(source,destination,g10_08)} time taken = {(time.perf_counter() -start)*10 ** 5}")
#     start = time.perf_counter()