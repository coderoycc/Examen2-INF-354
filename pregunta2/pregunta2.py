import numpy as np
import random

recorrido = np.genfromtxt('/home/roy/Documentos/grafo.csv', delimiter=',', skip_header=1)

modelEnd = [0,1,2,3,4] 
largeIndividual = 5 

num = 30 #Cantidad de individuos
generation = 5 #Generaciones
pressure = 2 #individual>2
mutation_chance = 0.2

imin=0
imax=4
#CREMOS INDIVIDUO CON ELEMENTOS DEL 0-4 No Repetidos
def individual(min, max):
    ss = set([])
    a=0
    individuo = [] #genera individuo
    while(len(ss)<largeIndividual):
        a=len(ss) 
        elemento=random.randint(min, max)
        ss.add(elemento)
        if(len(ss)!=a):
            individuo.append(elemento)
    return individuo

def newPopulation():
    return [individual(imin,imax) for i in range(num)]

# Funcion la que se debe cambiar en funcion a f(x)
def functionType(individual):
    funcionObj = 0
    for i in range(len(individual)):
        if individual[i]==modelEnd[i]:
            funcionObj+=1
    return funcionObj

def selection_and_reproduction(population):
    chosen = []
    for i in range(len(population)-pressure):
        aspirants = [random.choice(population) for i in range(2)]
        chosen.append(max(aspirants))
    return chosen

def mutation(population):
    size = len(population)
    for i in range(size):
        if random.random() < mutation_chance: #probabilidad
            indice_int = random.randint(0, size - 2)
            if indice_int >= i:
                indice_int += 1
            population[i], population[indice_int] = population[indice_int], population[i]
    return population


# Principal
population = newPopulation()
print("\nPopulation Begin:\n%s"%(population))

for i in range(generation):    
    population = selection_and_reproduction(population)
    # print("\nSelection Population:\n%s"%(population))
    population = mutation(population)
    print("\nMutation Population:\n%s"%(population))
minimo = 600
for ele in population:
    suma=0
    for i in range(1, len(ele)):
        suma+=recorrido[ele[i-1]][ele[i]]
    suma+=recorrido[ele[i]][ele[0]]
    if (suma < minimo):
        minimo=suma
        v=ele
print(minimo, v)
