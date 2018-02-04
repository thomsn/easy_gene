import random


def evolve(population, scores, num_parents=2, mutation_rates=None):
    """
    Evolve a population based on provided scores
    :param population: a list of dictionaries. Each entry in the dict represents a parameter
    :param scores: a list of positive scores. Scale doesnt matter.
    :param num_parents: The number of parents to use when breeding the next population
    :param mutation_rate: The percent of change to apply to each individual in the population
    :return: the new population which is a list of dictionaries
    """
    start_num = len(population)
    params = list(population[0].keys())
    # selection
    selection_scores = [score * random.random() for score in scores]
    sorted_pop = sorted(zip(selection_scores, population), key=lambda scored_gene: scored_gene[0])
    population = [scored_parent[1] for scored_parent in sorted_pop[-num_parents:]]
    #crossover
    for _ in range(start_num - num_parents):
        child = {}
        for param in params:
            child[param] = population[random.randint(0,num_parents-1)][param]
        population.append(child)
    #mutation
    if mutation_rates:
        for gene in population:
            for param in params:
                if isinstance(gene[param], float):
                    gene[param] = gene[param]  + random.normalvariate(0, mutation_rates[param])
                elif isinstance(gene[param], bool):
                    if random.random() < mutation_rates[param]:
                        gene[param] = not gene[param]
                else:
                    raise RuntimeError('Can only mutate floats and booleans')

    return population
