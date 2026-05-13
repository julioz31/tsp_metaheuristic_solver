from math import dist
from itertools import combinations

class Genetyczny_alg:
    def __init__(self):
        self.list_of_cities = []
        self.distances = {}
        self.population_size = 100
        self.generations = 100
        self.elitism = True

    def dystans_miasta(self, cities):
        self.list_of_cities = cities
        self.distances = {}

        for i in range(len(cities)):
            for j in range(len(cities)):
                if i != j:
                    p1 = (cities[i][0], cities[i][1])
                    p2 = (cities[j][0], cities[j][1])

                    self.distances[(i, j)] = dist(p1, p2)



    def populacja(self):
        pass

    def crossover(self):
        pass

    def selekcja(self):
        pass

    def mutacja(self):
        pass

    def fitness(self):
        pass




    def cost(self):
        pass