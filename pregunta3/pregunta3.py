import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools



NB_QUEENS = 5
#Leeos la matriz de recorrido
recorrido = numpy.genfromtxt('/home/roy/Documentos/grafo.csv', delimiter=',', skip_header=1)

def evaluaPosicion(individual):
    size = len(individual)
    suma = 0
    for i in range(1, size):
        suma+=recorrido[individual[i-1]][individual[i]]
    suma+=recorrido[individual[i]][individual[0]]
    return suma,
    
def valoresRecorrido(individual):
    individual1=individual[0]
    size = len(individual1)
    for i in range(1, size):
        print(recorrido[individual1[i-1]][individual1[i]], end="->")
    print(recorrido[individual1[i]][individual1[0]], end="\n")
    
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)


toolbox = base.Toolbox()
toolbox.register("permutation", random.sample, range(NB_QUEENS), NB_QUEENS)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.permutation)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evaluaPosicion)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=2.0/NB_QUEENS)
toolbox.register("select", tools.selTournament, tournsize=3)

def main(seed=0):
    random.seed(seed)

    pop = toolbox.population(n=30)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("Avg", numpy.mean)
    stats.register("Std", numpy.std)
    stats.register("Min", numpy.min)
    stats.register("Max", numpy.max)

    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=10, stats=stats,
                        halloffame=hof, verbose=True)

    return pop, stats, hof

if __name__ == "__main__":
    hof = main()
    print("Los valores que toma el recorrido son: ")
    valoresRecorrido(hof[0])
    indices=hof[0][0]
    print("Cuyo valor (Minimo) es: ", sum(evaluaPosicion(indices)))
    
    