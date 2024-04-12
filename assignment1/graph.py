from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        self.nodes = {}
        self.neighbours = defaultdict(list)

    def add_node(self,node):
        city, latitude, longitude = node
        self.nodes[city] = (latitude,longitude)

    def remove_node(self,node):
        if node in self.nodes:
            del self.nodes[node]
        if node in self.neighbours:
            del self.neighbours[node]

    def add_edge(self,city1,city2,weight):
        self.neighbours[city1].append((city2 , weight))
        self.neighbours[city2].append((city1 , weight))

    def remove_edge(self, city1, city2):
        if city1 in self.neighbours and city2 in self.neighbours[city1]:
            del self.neighbours[city1][city2]
        if city2 in self.neighbours and city1 in self.neighbours[city2]:
            del self.neighbours[city2][city1]

    def get_neighbours(self,city):
        return self.neighbours[city]
    
    def __str__(self) -> str:
        return str(self.neighbours)
    
class RandomGraph():
    def __init__(self):
        self.nodes = {}
        self.neighbours = defaultdict(list)

    def add_node(self,node,coor):
        self.nodes[node] = coor

    def remove_node(self,node):
        if node in self.nodes:
            del self.nodes[node]
        if node in self.neighbours:
            del self.neighbours[node]
        
    def add_edge(self,source,destination,wieght):
        self.neighbours[source].append((destination,wieght))
        self.neighbours[destination].append((source,wieght))

    def remove_edge(self,source,destination):
        if source in self.neighbours and destination in self.neighbours[source]:
            del self.neighbours[source][destination]
        if destination in  self.neighbours and source in self.neighbours[destination]:
            del self.neighbours[destination][source]
    
    def get_neighbours(self,node):
        return self.neighbours[node]
    
    def __str__(self) -> str:
        return str(self.neighbours)

    