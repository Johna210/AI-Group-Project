import networkx as nx
import matplotlib.pyplot as plt
from romania import graph

class CentralityCalculator:
    def __init__(self, graph):
        self.graph = graph

    def convert_to_networkx(self):
        G = nx.Graph()
        for city, coor in self.graph.nodes.items():
            G.add_node(city, latitude=coor[0], longitude=coor[1])

        for city, neighbors in self.graph.neighbours.items():
            for neighbor, weight in neighbors:
                G.add_edge(city, neighbor, weight=weight)
        return G

    def compute_centralities(self):
        G = self.convert_to_networkx()

        # Degree Centrality
        degree_centrality = nx.degree_centrality(G)

        # Closeness Centrality
        closeness_centrality = nx.closeness_centrality(G)

        # Eigenvector Centrality
        eigenvector_centrality = nx.eigenvector_centrality(G)

        # Katz Centrality
        katz_centrality = nx.katz_centrality(G)

        # PageRank Centrality
        pagerank_centrality = nx.pagerank(G)

        # Betweenness Centrality
        betweenness_centrality = nx.betweenness_centrality(G)

        return degree_centrality, closeness_centrality, eigenvector_centrality, katz_centrality, pagerank_centrality, betweenness_centrality

    def save_centralities_to_file(self, filename):
        degree_centrality, closeness_centrality, eigenvector_centrality, katz_centrality, pagerank_centrality, betweenness_centrality = self.compute_centralities()

        with open(filename, "w") as file:
            for city in self.graph.nodes.keys():
                file.write(f"City: {city}\n")
                file.write(f"Degree Centrality: {degree_centrality[city]}\n")
                file.write(f"Closeness Centrality: {closeness_centrality[city]}\n")
                file.write(f"Eigenvector Centrality: {eigenvector_centrality[city]}\n")
                file.write(f"Katz Centrality: {katz_centrality[city]}\n")
                file.write(f"PageRank Centrality: {pagerank_centrality[city]}\n")
                file.write(f"Betweenness Centrality: {betweenness_centrality[city]}\n")
                file.write("=" * 30 + "\n")
    def plot_centrality_table(self):
        degree_centrality, closeness_centrality, eigenvector_centrality, katz_centrality, pagerank_centrality, betweenness_centrality = self.compute_centralities()

        # Sort cities based on each centrality measure
        top_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
        top_closeness = sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
        top_eigenvector = sorted(eigenvector_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
        top_katz = sorted(katz_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
        top_pagerank = sorted(pagerank_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
        top_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:5]

        # Create table data
        table_data = [
            ["Degree Centrality"] + [f"{city}: {centrality:.4f}" for city, centrality in top_degree],
            ["Closeness Centrality"] + [f"{city}: {centrality:.4f}" for city, centrality in top_closeness],
            ["Eigenvector Centrality"] + [f"{city}: {centrality:.4f}" for city, centrality in top_eigenvector],
            ["Katz Centrality"] + [f"{city}: {centrality:.4f}" for city, centrality in top_katz],
            ["PageRank Centrality"] + [f"{city}: {centrality:.4f}" for city, centrality in top_pagerank],
            ["Betweenness Centrality"] + [f"{city}: {centrality:.4f}" for city, centrality in top_betweenness]
        ]

        # Plot the table
        plt.figure(figsize=(10, 6))
        table = plt.table(cellText=table_data, loc='center', cellLoc='center', colLabels=['Top 5 Cities'] + [f"Rank {i+1}" for i in range(5)], colWidths=[0.25]*6)
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.5, 1.5)
        plt.axis('off')
        plt.title('Top-ranked cities in each centrality category')
        plt.show()

# Usage example:
centrality_calculator = CentralityCalculator(graph)
centrality_calculator.save_centralities_to_file("centrality_output.txt")
centrality_calculator.plot_centrality_table()
