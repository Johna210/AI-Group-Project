import sys
import random
import time

def read_knapsackData(file_name):
    knapsackData = {}
    with open(file_name, 'r') as file:
        lines = file.readlines()
        maxWeight = int(lines[0])
        for line in lines[2:]:
            item, weight, value, quantity = line.strip().split(',')
            knapsackData[item] = [float(weight.strip()), int(value.strip()), int(quantity.strip())]
    return knapsackData, maxWeight

class GeneticAlgorithm:
    def __init__(self, knapsack_data, population_size, mutation_rate, num_generations, max_weight):
        self.knapsack_data = knapsack_data
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.num_generations = num_generations
        self.max_weight = max_weight 

    def generate_population(self):
        population = []
        while len(population) < self.population_size:
            combination = {}
            total_weight = 0
            for item, data in self.knapsack_data.items():
                quantity = random.randint(0, data[2])
                weight = data[0] * quantity
                if total_weight + weight <= self.max_weight:
                    combination[item] = quantity
                    total_weight += weight
                else:
                    break
            if combination:
                population.append(combination)
        return population

    def calculate_fitness(self, combination):
        total_weight = 0
        total_value = 0
        for item, quantity in combination.items():
            weight, value, _ = self.knapsack_data[item]
            total_weight += quantity * weight
            total_value += quantity * value
        if total_weight > self.max_weight:
            total_value = 0
        return total_value

    def select(self, population, k=5):
        selected_parents = []
        for _ in range(2):
            participants = random.sample(population, k)
            best_parent = max(participants, key=self.calculate_fitness)
            selected_parents.append(best_parent)
        return selected_parents

    def crossover(self, parent1, parent2):
        crossover_point = random.choice(list(parent1.keys()))

        child1 = {**parent1, **{key: parent2[key] for key in parent2 if key >= crossover_point}}
        child2 = {**parent2, **{key: parent1[key] for key in parent1 if key >= crossover_point}}

        return child1, child2




    def mutate(self, combination):
        mutated_combination = {}
        for item, quantity in combination.items():
            if random.random() < self.mutation_rate:
                _, _, n_items = self.knapsack_data[item]
                mutated_quantity = random.randint(0, n_items)
            else:
                mutated_quantity = quantity
            mutated_combination[item] = mutated_quantity
        return mutated_combination

    def carried_items(self, combination):
        items = []
        total_weight = 0
        for item, quantity in combination.items():
            if quantity > 0:
                items.append(item)
                weight, _, _ = self.knapsack_data[item]
                total_weight += weight * quantity
        return items, total_weight

    def run_ga(self):
        population = self.generate_population()

        for _ in range(self.num_generations):
            new_population = []

            while len(new_population) < self.population_size:
                parent1, parent2 = self.select(population)
                child1, child2 = self.crossover(parent1, parent2)
                mutated_child1 = self.mutate(child1)
                mutated_child2 = self.mutate(child2)
                new_population.extend([mutated_child1, mutated_child2])

            population = new_population

        best_combination = max(population, key=self.calculate_fitness)
        best_value = self.calculate_fitness(best_combination)
        return best_combination, best_value

    
populationSize = 300
mutationRate = 0.045
numGenerations = 1500


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("The argument should be in this form: python knapsack.py --algorithm ga --file my-file.txt")
        exit()
    
    algorithm = sys.argv[2]
    file = sys.argv[4]
    
    itemsData, maxWeight = read_knapsackData(file)
    
    if algorithm == 'ga':
        knapsack_ga = GeneticAlgorithm(itemsData, populationSize, mutationRate, numGenerations, maxWeight)
        
        start_time = time.time()
        best_combination, best_fitness = knapsack_ga.run_ga()
        end_time = time.time()
        
        itemList, totalWeight = knapsack_ga.carried_items(best_combination)
        
        print("Best combination:", best_combination)
        print("Best Value:", best_fitness)
        print("Total weight carried:", totalWeight)
        print("Execution time:", end_time - start_time, "seconds")
