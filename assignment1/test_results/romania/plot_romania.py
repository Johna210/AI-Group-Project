import matplotlib.pyplot as plt

# Data
algorithms = ['DFS', 'BFS', 'UCS',"A*","Greedy","Bidirectional","IDS"]
average_results = {
    "DFS": (10.9,767,8.93),
    "BFS": (9.5,404.3,3.57),
    "UCS": (8.4,369.6,2.35),
    "A*": (6.5,305,1.5),
    "Greedy": (6,346,1.77),
    "Bidirectional":(9.9,426.1,1.08),
    "IDS": (6.1,415.8,1.96)
}
runtimes = [average_results[algo][2] for algo in algorithms]

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(algorithms, runtimes, color=['blue', 'green', 'orange','red','purple','brown','yellow'])

# Add labels and title
plt.xlabel('Searching Algorithms')
plt.ylabel('Runtime (microseconds)')
plt.title('Comparison of Searching Algorithms Runtimes')

# Show plot
plt.show()

# Add another graph for average nodes expanded
average_nodes_expanded = [average_results[algo][0] for algo in algorithms]

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(algorithms, average_nodes_expanded, color=['blue', 'green', 'orange','red','purple','brown','yellow'])

# Add labels and title
plt.xlabel('Searching Algorithms')
plt.ylabel('Average Nodes Expanded')
plt.title('Comparison of Searching Algorithms Average Nodes Expanded')

# Show plot
plt.show()

# Add another graph for average path length
average_path_length = [average_results[algo][1] for algo in algorithms]

# Create bar chart
plt.figure(figsize=(10, 4))
plt.bar(algorithms, average_path_length, color=['blue', 'green', 'orange','red','purple','brown','yellow'])

# Add labels and title
plt.xlabel('Searching Algorithms')
plt.ylabel('Average Path Length')
plt.title('Comparison of Searching Algorithms Average Path Length')

# Show plot
plt.show()
