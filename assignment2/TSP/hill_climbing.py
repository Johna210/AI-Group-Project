import utils
import random


def generateSuccessors(path):
	N = len(path)        
	
	randomSequence1 = list(range(N))
	random.shuffle(randomSequence1)
	randomSequence2 = list(range(N))
	random.shuffle(randomSequence2)
	

	for i in randomSequence1:
		for j in randomSequence2:
			if i<j:
				temp = list(path)
				temp[i],temp[j] = path[j],path[i]
				yield temp


def hill_climbing(cities, graph, generation):
    path = cities
    random.shuffle(path)

    bestTour = path
    bestValue = utils.calculate_cost(path, graph)

    for _ in range(generation):        
	
        for successor in generateSuccessors(bestTour):
            successorValue = utils.calculate_cost(successor, graph=graph)
			
            if successorValue < bestValue:
                bestTour  = successor
                bestValue = successorValue                

        if bestTour == path:            
            return (bestTour, bestValue)
        
    return (bestTour, bestValue)