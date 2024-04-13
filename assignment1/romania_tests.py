from romania import graph
from search import dfs,bfs,ucs,greedy_search,astar,bidirectional_search,ids
import random
import time
from tabulate import tabulate

cities = ['Oradea', 'Zerind', 'Arad', 'Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 'Sibiu', 'Fagaras', 'Pitesti', 'Giurgiu', 'Bucharest', 'Urziceni', 'Eforie', 'Hirsova', 'Vaslui', 'Iasi', 'Neamt']

test1_results = {}

searching_algos = {
    'DFS': dfs,
    'BFS': bfs,
    'UCS': ucs,
    'Greedy Search': greedy_search,
    'A*': astar,
    'Bidirectional Search': bidirectional_search,
    'IDS': ids
}

for i in range(10):
    source = random.choice(cities)
    destination = random.choice(cities)
    while destination == source:
        destination = random.choice(cities)
    
    for algo_name, algo in searching_algos.items():
        start_time = time.perf_counter()
        result = algo(source, destination,graph)
        end_time = time.perf_counter()

        test1_results.setdefault(algo_name, []).append((result,end_time-start_time))
print(test1_results)

# for result in test1_results:
#     with open("test_results.txt", "a") as file:
#         file.write(f"Algorithm: {result}\n")
#         file.write(f"{'Destination':<20}{'Time':<20}\n")
#         for res in test1_results[result]:
#             file.write(f"{res[0][0]}-{res[0][1]:<20}{res[1]:<20}\n")
#         file.write(f"{'Average':<20}{sum([res[1] for res in test1_results[result]])/10:<20}\n\n")

headers = ["Algorithm","Path","Nodes Expanded","Time"]
rows = []
for algo, results in test1_results.items():
    for result, time_taken in results:
        path, nodes_expanded, total_distance = result
        rows.append([algo, path, nodes_expanded, total_distance, time_taken])

print(tabulate(rows, headers=headers))