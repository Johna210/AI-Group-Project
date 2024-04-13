from random_graph import generate_random_graph
from search import dfs,bfs,ucs,greedy_search,astar,bidirectional_search,ids
import random
import time
import statistics as stats
import csv

g10_graphs = [generate_random_graph(10,0.2),generate_random_graph(10,0.4),generate_random_graph(10,0.6),generate_random_graph(10,0.8)]
g20_graphs = [generate_random_graph(20,0.2),generate_random_graph(20,0.4),generate_random_graph(20,0.6),generate_random_graph(20,0.8)]
g30_graphs = [generate_random_graph(30,0.2),generate_random_graph(30,0.4),generate_random_graph(30,0.6),generate_random_graph(30,0.8)]
g40_graphs = [generate_random_graph(40,0.2),generate_random_graph(40,0.4),generate_random_graph(40,0.6),generate_random_graph(40,0.8)]


graphs = {
    'g10' : g10_graphs,
    'g20' : g20_graphs,
    'g30' : g30_graphs,
    'g40' :g40_graphs
}

searching_algos = {
    'DFS': dfs,
    'BFS': bfs,
    'UCS': ucs,
    'Greedy': greedy_search,
    'A*': astar,
    'Bidirectional': bidirectional_search,
    'IDS': ids
}
average_results = {
        'g10':[],
        'g20':[],
        'g30':[],
        'g40':[]
}

for i in range(10):
    source = random.randint(1,10)
    destination = random.randint(1,10)

    for g in graphs:
        for algo,algo_func in searching_algos.items():
            local_average = {
                algo : {
                    'average_distance':0,
                    'average_nodes_expanded':0,
                    'average_time':0
                } 
            }
            count = 1
            for graph in graphs[g]:
                start = time.perf_counter()
                result = algo_func(source,destination,graph)
                end = time.perf_counter()
                local_average[algo]['average_time'] += ((end-start)/count)
                local_average[algo]['average_nodes_expanded'] += result[1]/count
                local_average[algo]['average_distance'] += result[2]/count
                count += 1
            
            average_results[g].append(local_average)

final_results = {
    'g10':None,
    'g20':None,
    'g30':None,
    'g40':None
}

for result in average_results:
    local_average = {
        'BFS':{
            'average_distance':0,   
            'average_nodes_expanded':0,
            'average_time':0
        }
        ,
        'DFS':{
            'average_distance':0,   
            'average_nodes_expanded':0,
            'average_time':0
        },
        'UCS':{
            'average_distance':0,   
            'average_nodes_expanded':0,
            'average_time':0
        },
        'Greedy':{
            'average_distance':0,   
            'average_nodes_expanded':0,
            'average_time':0
        },
        'A*':{
            'average_distance':0,   
            'average_nodes_expanded':0,
            'average_time':0
        },
        'Bidirectional':{   
            'average_distance':0,   
            'average_nodes_expanded':0,
            'average_time':0
        },
        'IDS':{
            'average_distance':0,   
            'average_nodes_expanded':0,
            'average_time':0
        }
    }
    for algo in average_results[result]:
        for key in algo:
            local_average[key]['average_distance'] = stats.mean([algo[key]['average_distance'],local_average[key]['average_distance']])
            local_average[key]['average_nodes_expanded']= stats.mean([algo[key]['average_nodes_expanded'],local_average[key]['average_nodes_expanded']])
            local_average[key]['average_time'] = stats.mean([algo[key]['average_time'],local_average[key]['average_time']])

    final_results[result] = local_average

headers = ['graph', 'algorithm', 'average_distance', 'average_nodes_expanded', 'average_time']

# Write data to a CSV file
with open('graph_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for graph, algorithms in final_results.items():
        for algorithm, metrics in algorithms.items():
            writer.writerow([graph, algorithm, metrics['average_distance'], metrics['average_nodes_expanded'], metrics['average_time']])


