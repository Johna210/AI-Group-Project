# Description: Knapsack problem solver using hill climbing algorithm

import random
import sys

def read_input_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        W = int(lines[0])
        items = {}
        for line in lines[2:]:
            name, weight, value, num_item = line.strip().split(',')
            items[name] = [float(weight), float(value), int(num_item)]

        return W, items

class HillClimbing:
    def __init__(self, items, max_weight, max_iterations):
        self.items = items
        self.max_weight = max_weight
        self.max_iterations = max_iterations
        self.current_solution = {item:0 for item in self.items.keys()} 


    def initState(self):
        neighbor_solution = self.current_solution.copy()
        print(self.items.values())
        sorted_items = sorted(self.items.keys(), key=lambda x: self.items[x][1] / self.items[x][0], reverse=True)
        print(sorted_items)
        for item in sorted_items:
            if neighbor_solution[item] < self.items[item][2] and self.calculate_value(neighbor_solution) + self.items[item][1] > self.calculate_value(self.current_solution):
                neighbor_solution[item] += 1
                break
        return neighbor_solution    

    def calculate_value(self, solution):
        value = 0
        weight = 0
        for i in solution.keys():
            value += solution[i] * self.items[i][1]
            weight += solution[i] * self.items[i][0]
        if weight > self.max_weight:
            return 0
        return value

    def generate_neighbor(self):
        weights = [1/(i if i != 0 else sys.float_info.epsilon)
                   for i, _, _ in self.items.values()]
        item = random.choices(list(self.items.keys()), weights=weights, k=1)[0]
        
        # while items[item][2]==current_solution[item]:
        #     item = random.choice(list(items.keys()))
        new_solution = self.current_solution.copy()

        if (new_solution[item] != 0 and new_solution[item] != self.items[item][2]):
            add = random.choices([-1, 1], weights=[3, 1], k=1)
            # print(add)
            new_solution[item] += add[0]
        elif (new_solution[item] == 0):
            new_solution[item] += 1

        else:
            new_solution[item] -= 1
        return new_solution
       

    def run(self):
        self.current_solution=self.initState()
        
        current_value = self.calculate_value(self.current_solution)
        best_solution = self.current_solution.copy()
        best_value = current_value
        no_improvement_count = 0

        while no_improvement_count < self.max_iterations:
            neighbor_solution = self.generate_neighbor()
            neighbor_value = self.calculate_value(neighbor_solution)

            if neighbor_value > current_value:
                self.current_solution = neighbor_solution.copy()
                current_value = neighbor_value
                no_improvement_count = 0
                if current_value > best_value:
                    best_solution = self.current_solution.copy()
                    best_value = current_value
            else:
                no_improvement_count += 1
           

        return best_solution, best_value

# Example usage
# W, items = read_input_file("my-file.txt")
# print("Max Weight:", W)
# # print("Items:", items)     
# hill_climbing = HillClimbing(items, W, 100)
# optimal_solution, optimal_value = hill_climbing.run()

# selected_items = []
# for i, item in enumerate(items):
#     count = optimal_solution[i]
#     if count > 0:
#         selected_items.append((item["name"], count))

# print("Optimal Solution:",optimal_solution)
# for item in selected_items:
#     print(item[0], "-", item[1])

# print("Optimal Value:", optimal_value)