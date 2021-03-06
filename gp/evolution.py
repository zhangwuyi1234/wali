# -*-coding:utf-8-*-
import array
import random
import numpy
import barinFack as bf
import time
import pickle as p
from deap import algorithms
from deap import base
from deap import creator
from deap import tools

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", array.array, typecode='b', fitness=creator.FitnessMax)

toolbox = base.Toolbox()

def getBaseValue():
    return random.randint(0,7)

# Attribute generator
toolbox.register("attr_bool",getBaseValue)

# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 250)  #barinFack length
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalOneMax(individual):
    indList=individual.tolist()
	#bf.run(indList)
    #sum(individual) 
    return sum(individual)  ,
toolbox.register("evaluate", evalOneMax)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=10)      #tournsize   selectNum 



def main():
    random.seed(64)
    pop = toolbox.population(n=300)  #定义了300个个体的种群！
    try:
        rFile =open('pop.data','rb')
        pop=p.load(rFile)
        rFile.close
        print ("loadSuccess")
    except BaseException:
        print ("loadError")
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    
    #cxpb交叉率  mutpb变异率   ngen迭代次数
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=10000, 
                                   stats=stats, halloffame=hof, verbose=True)
    #print(len(hof[0]))
    #print(hof)
    f = open('pop.data','wb')
    p.dump(pop, f)
    f.close()

    #print pop, log, hof

if __name__ == "__main__":
    main()
