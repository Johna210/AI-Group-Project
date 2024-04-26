import sys
import time
import knap
import knapsack
import knapsack_simulated


def read_knapsackData(file_name):
    knapsackData = {}
    with open(file_name, 'r') as file:
        lines = file.readlines()
        maxWeight = int(lines[0])
        for line in lines[2:]:
            item, weight, value, quantity = line.strip().split(',')
            knapsackData[item] = [float(weight.strip()), int(
                value.strip()), int(quantity.strip())]
    return knapsackData, maxWeight


populationSize = 300
mutationRate = 0.045
numGenerations = 1500
initial_temperature = 1000
cooling_rate = 0.99
stopping_temperature = 0.001
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("The argument should be in this form: python main.py --algorithm ga --file my-file.txt")
        exit()

    algorithm = sys.argv[2]
    file = sys.argv[4]
    print(algorithm, file)

    itemsData, maxWeight = read_knapsackData(file)

    if algorithm == 'ga':
        knapsack_ga = knapsack.GeneticAlgorithm(
            itemsData, populationSize, mutationRate, numGenerations, maxWeight)

        start_time = time.time()
        best_combination, best_fitness = knapsack_ga.run_ga()
        end_time = time.time()

        itemList, totalWeight = knapsack_ga.carried_items(best_combination)

        print("Genetic Algorithm Results:")
        print("Best combination:", best_combination)
        print("Best Value:", best_fitness)
        print("Total weight carried:", totalWeight)
        print("Execution time:", end_time - start_time, "seconds")

    elif algorithm == 'sa':
        knapsack_sa = knapsack_simulated.KnapsackSimulated(
            itemsData, maxWeight)

        start_time = time.time()
        best_combination, best_fitness = knapsack_sa.simulated_annealing(
            initial_temperature, cooling_rate, stopping_temperature)
        end_time = time.time()

        print("Simulated Annealing Results:")
        print("Best combination:", best_combination)
        print("Best Value:", best_fitness)
        print("Execution time:", end_time - start_time, "seconds")

    elif algorithm == 'hc':
        knapsack_hc = knap.HillClimbing(itemsData, maxWeight,100)
        start_time = time.time()
        best_combination, best_fitness = knapsack_hc.run()
        end_time = time.time()

        print("Hill Climbing Results:")
        print("Best combination:", best_combination)
        print("Best Value:", best_fitness)
        print("Execution time:", end_time - start_time, "seconds")
