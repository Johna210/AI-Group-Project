import matplotlib.pyplot as plt

# Sample data (replace this with your actual data)
algorithms = ['DFS', 'BFS', 'UCS', 'A*', 'IDS', 'Greedy']
average_runtimes = {
    'DFS': [0.4, 0.5, 0.4, 0.7],  # Replace with your actual data
    'BFS': [0.3, 0.3, 0.35, 0.45],
    'UCS': [0.2, 0.3, 0.32, 0.4],  # Replace with your actual data
    'A*': [0.1, 0.2, 0.23, 0.3],  # Replace with your actual data
    'IDS': [0.15, 0.24, 0.3, 0.37],  # Replace with your actual data
    'Greedy': [0.2, 0.3, 0.3, 0.4],  # Replace with your actual data
}
nodes = [10, 20, 30, 40]
edge_probabilities = [0.2, 0.4, 0.6, 0.8]

# Plot each algorithm's average runtime
for algorithm in algorithms:
    plt.plot(nodes, average_runtimes[algorithm], label=algorithm)

# Customize the plot
plt.title('Average Runtime of Searching Algorithms vs. Number of Nodes')
plt.xlabel('Number of Nodes')
plt.ylabel('Average Runtime')
plt.legend()

# Show the plot
plt.show()