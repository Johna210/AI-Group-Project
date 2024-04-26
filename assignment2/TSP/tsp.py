import argparse
from hill_climbing import hill_climbing
from graph import UndirectedGraph
from simulated_annealing import simulated_annealing
from genetic_algorithm import genetic_algorithm
import time

parser = argparse.ArgumentParser(description='Solve the TSP using a specified algorithm')
parser.add_argument('--algorithm', type=str, choices=['hc', 'sa', 'ga'], default='hc',
                    help='the algorithm to use (default: hc)')
parser.add_argument('--file', type=str, required=True,
                    help='the path to the file containing the TSP data')


args = parser.parse_args()
graph = UndirectedGraph()


with open(args.file) as file:
    cities = set()
    for line in file.readlines()[1:]:
        city_1, city_2, distance = line.split("    ")

        distance = int(distance)


        graph.add_edge(city_1, city_2, distance)
        cities.add(city_1)
        cities.add(city_2)

    cities = list(cities)


if args.algorithm == 'hc':
    start_time = time.perf_counter()
    path, dist = hill_climbing(cities=cities, graph=graph, generation=100)
    end_time = time.perf_counter()

elif args.algorithm == 'sa':
    start_time = time.perf_counter()
    path, dist = simulated_annealing(cities=cities, graph=graph, generation=1000)
    end_time = time.perf_counter()


elif args.algorithm == 'ga':
    start_time = time.perf_counter()
    path, dist = genetic_algorithm(cities=cities, 
                                   graph=graph, 
                                   population_size=150, 
                                   percent=0.7, 
                                   generation=200)    
    end_time = time.perf_counter()
    


print("Algorithm Selected: ", args.algorithm)
print("Time Taken: ", end_time - start_time)
print("Tour Taken: ", path)
print("Distance: ", dist)