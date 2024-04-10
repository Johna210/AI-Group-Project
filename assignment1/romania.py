from graph import Graph

file = open("romania.txt","r")
graph = Graph()

# Read from file and make the graph
with open("romania.txt") as file:
    # Jump the first line
    next(file)
    for line in file:
        l = line.strip().split()
        if len(l) > 3:
            city = l[0] + " " + l[1]
            latitued = l[2]
            longitude = l[3]
        else:
            city = l[0]
            latitued = l[1]
            longitude = l[2]

        graph.add_node((city, latitued, longitude))

# Add the edges to the graph based on the book
graph.add_edge("Oradea", "Zerind", 71)
graph.add_edge("Oradea", "Sibiu", 151)
graph.add_edge("Zerind", "Arad", 75)
graph.add_edge("Arad", "Sibiu", 140)
graph.add_edge("Arad", "Timisoara", 118)
graph.add_edge("Timisoara", "Lugoj", 111)
graph.add_edge("Lugoj", "Mehadia", 70)
graph.add_edge("Mehadia", "Drobeta", 75)
graph.add_edge("Drobeta", "Craiova", 120)
graph.add_edge("Craiova", "Rimnicu Vilcea", 146)
graph.add_edge("Craiova", "Pitesti", 138)
graph.add_edge("Rimnicu Vilcea", "Sibiu", 80)
graph.add_edge("Rimnicu Vilcea", "Pitesti", 97)
graph.add_edge("Sibiu", "Fagaras", 99)
graph.add_edge("Fagaras", "Bucharest", 211)
graph.add_edge("Pitesti", "Bucharest", 101)
graph.add_edge("Bucharest", "Urziceni", 85)
graph.add_edge("Urziceni", "Hirsova", 98)
graph.add_edge("Urziceni", "Vaslui", 142)
graph.add_edge("Hirsova", "Eforie", 86)
graph.add_edge("Iasi", "Neamt", 87)
graph.add_edge("Iasi", "Vaslui", 92)

def give_graph():
    return graph