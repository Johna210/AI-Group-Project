import matplotlib.pyplot as plt
import numpy as np
import csv


algorithms = ['DFS', 'BFS', 'UCS', 'A*', 'IDS', 'Greedy']
average_runtimes = {
    'DFS': [],
    'BFS': [],
    'UCS': [],
    'A*': [],
    'IDS': [],
    'Greedy': [],
    'Bidirectional': []
}

average_nodes_expanded = {
    'DFS': [],
    'BFS': [],
    'UCS': [],
    'A*': [],
    'IDS': [],
    'Greedy': [],
    'Bidirectional': []
}

average_distance = {
    'DFS': [],
    'BFS': [],
    'UCS': [],
    'A*': [],
    'IDS': [],
    'Greedy': [],
    'Bidirectional': []
}   

nodes = [10, 20, 30, 40]
edge_probabilities = [0.2, 0.4, 0.6, 0.8]

# Open the CSV file
with open('graph_data.csv', newline='') as file:
    reader = csv.reader(file)
    
    # Read the header row
    headers = next(reader)
    
    # Print the header row
    print("Headers:", headers)
    
    # Iterate over the remaining rows
    for row in reader:
        average_runtimes[row[1]].append(float(row[4]))
        average_nodes_expanded[row[1]].append(float(row[3]))
        average_distance[row[1]].append(float(row[2]))


for algorithm in algorithms:
    plt.plot(nodes, average_runtimes[algorithm], label=algorithm)

# Customize the plot
plt.title('Average Runtime of Searching Algorithms vs. Number of Nodes')
plt.xlabel('Number of Nodes')
plt.ylabel('Average Runtime')
plt.legend()

# Show the plot
plt.show()

# Plot a bar chart of average nodes expanded and the number of nodes
x = np.arange(len(nodes))
width = 0.1  # Width of each bar

fig, ax = plt.subplots()
for i, algorithm in enumerate(algorithms):
    ax.bar(x + (i * width), average_nodes_expanded[algorithm], width, label=algorithm)

# Customize the plot
ax.set_xlabel('Number of Nodes')
ax.set_ylabel('Nodes Expanded')
ax.set_title('Number of Nodes Expanded by Searching Algorithms')
ax.set_xticks(x + (len(algorithms) * width) / 2)
ax.set_xticklabels(nodes)
ax.legend()

# Show the plot
plt.show()

# Plot a bar chart of average distance and the number of nodes

x = np.arange(len(nodes))
width = 0.1  # Width of each bar

fig, ax = plt.subplots()
for i, algorithm in enumerate(algorithms):
    ax.bar(x + (i * width), average_distance[algorithm], width, label=algorithm)

# Customize the plot
ax.set_xlabel('Number of Nodes')
ax.set_ylabel('Average Distance')
ax.set_title('Average Distance of Searching Algorithms')
ax.set_xticks(x + (len(algorithms) * width) / 2)
ax.set_xticklabels(nodes)
ax.legend()

# Show the plot
plt.show()