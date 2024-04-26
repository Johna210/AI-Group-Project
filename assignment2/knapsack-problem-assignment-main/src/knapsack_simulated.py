import argparse
import math
import random
import time


def read_input_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        W = int(lines[0])
        items = {}
        total_item = 0
        for line in lines[2:]:
            name, weight, value, num_item = line.strip().split(',')
            total_item += int(num_item)
            items[name] = (float(weight), float(value), int(num_item))
        return W, items, total_item


class KnapsackSimulated:
    def __init__(self, items, W):
        self.current_solution = {}
        self.current_value = 0
        self.items = items
        self.W = W
        self.total_item = sum(num for _, _, num in self.items.values())

    def __initState(self):
        choosen = {}
        for name in self.items:
            choosen[name] = 0
        for i in range(self.total_item):
            value = random.choices([True, False], weights=[1, 3], k=1)[0]
            # print(value)
            # item = random.choices(list(items.keys()),weights=[-i for _,_,i in items.values()],k=1)[0]
            weights = [1/(i**40 if i != 0 else sys.float_info.epsilon)
                       for _, _, i in self.items.values()]
            item = random.choices(list(self.items.keys()),
                                  weights=weights, k=1)[0]
            # item = random.choice(list(self.items.keys()))

            before = choosen.get(item)
            if (value and self.items[item][2] > before):
                choosen[item] = before+1
            else:
                choosen[item] = before

        return choosen

    def __neighbor_solution(self):
        weights = [1/(i if i != 0 else sys.float_info.epsilon)
                   for _, _, i in self.items.values()]
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

    def __knapsack_value(self):
        total_weight = 0
        for name in self.items:
            total_weight += self.items[name][0]*self.current_solution[name]
            # if solution[name]:
            #     total_weight+=items[name][0]

        if total_weight > self.W:
            return 0
        total_value = 0
        for name in self.items:
            total_value += self.items[name][1]*self.current_solution[name]
            # if solution[name]:
            #     total_value+=items[name][1]
        return total_value

    def simulated_annealing(self, T0, alpha, stopping_temperature):
        # current_solution = {name:random.choice([True, False]) for name in items}
        self.current_solution = self.__initState()

        self.current_value = self.__knapsack_value()
        T = T0

        max_tracker = float("-inf")
        max_solution = {}

        while T > stopping_temperature:
            new_solution = self.__neighbor_solution()
            new_value = self.__knapsack_value()
            diff = new_value - self.current_value
            if diff > 0 or random.random() < math.exp(diff / T):
                self.current_solution = new_solution
                self.current_value = new_value

                if (self.current_value > max_tracker):
                    max_tracker = self.current_value
                    max_solution = self.current_solution
            T *= alpha

        # print(max_tracker > self.current_value)
        if (max_tracker > self.current_value):
            self.current_value = max_tracker
            self.current_solution = max_solution

        self.current_value = max(max_tracker, self.current_value)
        return self.current_solution, self.current_value


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, required=True,
                        help='input file path')
    parser.add_argument('--T0', type=float, default=1000,
                        help='initial temperature')
    parser.add_argument('--alpha', type=float, default=0.99,
                        help='temperature decay rate')
    parser.add_argument('--stopping_temperature', type=float,
                        default=1e-3, help='stopping temperature')
    args = parser.parse_args()

    W, itemss = read_input_file(args.file)

    # solution, value = simulated_annealing(W, items,total_item, args.T0, args.alpha, args.stopping_temperature)
    # print(items)
    knapsack_simulated = KnapsackSimulated(itemss, W)
    start_time = time.time()
    solution, value = knapsack_simulated.simulated_annealing(
        args.T0, args.alpha, args.stopping_temperature)
    end_time = time.time()
    print(f'Execution time: {end_time-start_time}')
    print(f'Solution: {solution}')
    print(f'Total value: {value}')


# python knapsack_simulated.py  --file my-file.txt --T0 1000 --alpha 0.99 --stopping_temperature 1e-3
