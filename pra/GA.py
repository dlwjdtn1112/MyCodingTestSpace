import heapq
import time
import random

def create_individual(nodes):
    individual = nodes[:]
    random.shuffle(individual)
    return individual

def create_population(graph, size):
    nodes = list(graph.keys())
    return [create_individual(nodes) for _ in range(size)]

def fitness(individual, graph):
    distance = 0
    for i in range(len(individual) - 1):
        distance += graph[individual[i]].get(individual[i + 1], float('inf'))
    return distance

def select(population, fitnesses, k=3):
    selected = random.sample(list(zip(population, fitnesses)), k)
    selected = sorted(selected, key=lambda x: x[1])
    return selected[0][0]

def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted([random.randint(0, size - 1) for _ in range(2)])
    child = parent1[start:end] + [gene for gene in parent2 if gene not in parent1[start:end]]
    return child

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(individual) - 1)
            individual[i], individual[j] = individual[j], individual[i]

def genetic_algorithm(graph, population_size, generations, mutation_rate):
    population = create_population(graph, population_size)
    for generation in range(generations):
        fitnesses = [fitness(ind, graph) for ind in population]
        new_population = []
        for _ in range(population_size):
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
    best_individual = min(population, key=lambda ind: fitness(ind, graph))
    return best_individual, fitness(best_individual, graph)

# 주어진 그래프
graph = {
    'A': {'B': 8, 'C': 9, 'D': 11},
    'B': {'E': 10},
    'C': {'D': 3, 'E': 1},
    'D': {'G': 8, 'F': 8},
    'E': {'H': 2},
    'F': {'C': 12, 'H': 5},
    'G': {'F': 7},
    'H': {'G': 4}
}

# 성능 비교 및 최소 거리 계산
start_time = time.time()
best_individual, best_fitness = genetic_algorithm(graph, population_size=100, generations=500, mutation_rate=0.01)
end_time = time.time()

print("GA best individual:", best_individual)
print("GA best fitness:", best_fitness)
print("GA execution time:", end_time - start_time)
