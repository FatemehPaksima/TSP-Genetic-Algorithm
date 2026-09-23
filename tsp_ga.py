import random

def generate_population(population_size, cityNum):
    population = []
    for i in range(population_size):
        individual = [0] + random.sample(range(1, cityNum), cityNum - 1)
        population.append(individual)
    return population

def fitness(path):
    distance = 0
    for i in range(cityNum -1):
        distance += matrix[path[i]][path[i + 1]]
    distance += matrix[path[-1]][path[0]] 
    return distance

def roulette_wheel_selection(population, fitness_scores):
    totalfitness = sum(fitness_scores)
    prob = []
    for i in range(len(fitness_scores)):
        prob.append(totalfitness - fitness_scores[i] / totalfitness)
    parents = random.choices(population, weights = prob, k=2)
    return parents

def greedy_selection(population, fitness_scores):
    best_parent_index = fitness_scores.index(min(fitness_scores))
    temp = fitness_scores[best_parent_index]
    fitness_scores[best_parent_index] = float("inf")
    second_best_parent_index = fitness_scores.index(min(fitness_scores))
    fitness_scores[best_parent_index] = temp
    return [population[best_parent_index], population[second_best_parent_index]]

def single_point_crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + [gene for gene in parent2 if gene not in parent1[:crossover_point]]
    child2 = parent2[:crossover_point] + [gene for gene in parent1 if gene not in parent2[:crossover_point]]
    return child1, child2

def two_point_crossover(parent1, parent2):
    crossover_points = sorted(random.sample(range(len(parent1)), 2))
    child1 = [None] * len(parent1)
    child2 = [None] * len(parent2)

    child1[crossover_points[0]:crossover_points[1]] = parent1[crossover_points[0]:crossover_points[1]]
    child2[crossover_points[0]:crossover_points[1]] = parent2[crossover_points[0]:crossover_points[1]]

    index1, index2 = crossover_points[1], crossover_points[1]
    for i in range(len(parent2)):
        if index1 == len(parent2):
            index1 = 0
        if index2 == len(parent1):
            index2 = 0
        if parent2[i] not in child1:
            child1[index1] = parent2[i]
            index1 += 1
        if parent1[i] not in child2:
            child2[index2] = parent1[i]
            index2 += 1
    return child1, child2

def single_point_mutation(chromosome, mutation_rate = 0.3):
    if random.random() < mutation_rate:
        gene = random.choice(chromosome[1:])  # اولین ژن را حفظ می کنیم
        chromosome.remove(gene)
        insertion_point = random.randint(1, len(chromosome))
        chromosome.insert(insertion_point, gene)
    return chromosome

def two_point_mutation(chromosome, mutation_rate = 0.3):
    mutated_chromosome = chromosome.copy()
    if random.random() < mutation_rate:
        index1, index2 = random.sample(range(len(chromosome)), 2)
        mutated_chromosome[index1], mutated_chromosome[index2] = mutated_chromosome[index2], mutated_chromosome[index1]
    return mutated_chromosome

def replace_least_fit(population, fitness_scores, offspring1, offspring2):
    max_fitness_index1 = fitness_scores.index(max(fitness_scores))
    max_fitness_index2 = fitness_scores.index(max(fitness_scores[:max_fitness_index1] + fitness_scores[max_fitness_index1+1:]))
    population[max_fitness_index1] = offspring1
    population[max_fitness_index2] = offspring2
    return population

def genetic_algorithm(population_size, generations):
    population = []
    population = generate_population(population_size, cityNum)
    fitness_scores = [fitness(path) for path in population]

    for i in range(generations):
        parents = greedy_selection(population, fitness_scores)
        offspring1, offspring2 = single_point_crossover(parents[0], parents[1])
        offspring1, offspring2 = two_point_mutation(offspring1),two_point_mutation(offspring2)
        population = replace_least_fit(population, fitness_scores, offspring1, offspring2)

    best_individual = min(population, key=lambda path: fitness(path))
    return best_individual

def main():
    global cityNum, matrix
    population_size = 5
    generations = 50
    matrix = [[0, 14, 4, 11, 18],
              [14, 0, 5, 7, 7],
              [4, 5, 0, 9, 17],
              [11, 7, 9, 0, 4],
              [18, 7, 17, 4, 0]]
    
    cityNum = len(matrix)

    best_solution = genetic_algorithm(population_size, generations)
    best_value = fitness(best_solution)
    
    print("Best solution:", best_solution + [0])
    print("Best value:", best_value)

main()