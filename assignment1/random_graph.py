from graph import RandomGraph
import random
from search import dfs, bfs, ucs, astar, ids, greedy_search,bidirectional_search

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





g = generate_random_graph(10,0.2)
g2 = generate_random_graph(10,0.4)
g3 = generate_random_graph(10,0.6)
g4 = generate_random_graph(10,0.8)

x = g.nodes

for _ in range(1,10):
    source = random.randint(1,10)
    destination = random.randint(1,10)

    print(f"From Source {source} to Destination {destination}")

    print(f"dfs{dfs(source,destination,g)}")
    print(f"bfs{bfs(source,destination,g)}")
    print(f"ucs{ucs(source,destination,g)}")
    print(f"A*{astar(source,destination,g)}")
    print(f"ids{ids(source,destination,g)}")
    print(f"Greedy{greedy_search(source,destination,g)}")
    print(f"bidirectional{bidirectional_search(source,destination,g)}")

    print("\n\n")