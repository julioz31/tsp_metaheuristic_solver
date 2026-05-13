from math import dist
from itertools import combinations
import random as rd



class Genetyczny_alg:
    def __init__(self):
        self.list_of_cities = []
        self.distances = {}
        self.population_size = 100
        self.generations = 100
        self.elitism = True
        self.tournament_size = 5

    def dystans_miasta(self, cities):
        """kalkulacja dystansu pomiędzy miastami i wnisienie do słownika"""
        self.list_of_cities = cities
        self.distances = {}

        for i in range(len(cities)):
            for j in range(len(cities)):
                if i != j:
                    p1 = (cities[i][0], cities[i][1])
                    p2 = (cities[j][0], cities[j][1])

                    self.distances[(i, j)] = dist(p1, p2)

    def total_dystans(self, route):
        """kalkulacja całej śzieżki"""
        total = 0
        for i in range(len(route) - 1):
            total += self.distances[(route[i], route[i+1])]

        total += self.distances[(route[-1], route[0])]
        return total

    def cost(self, route):
        """kalkulacja efektywności trasy według kosztu
        koszt = cała trasa/cały priorytet"""
        total_dist = self.total_dystans(route)
        total_priority = sum(self.list_of_cities[i][2] for i in route)

        return total_dist / total_priority if total_priority != 0 else total_dist

    def fitness(self, route):
        """ocena trasy: im mniejszy coszt tym większy fitness"""
        ocena = self.cost(route)

        return 1 / (ocena + 1e-10)


    def populacja(self):
        """lista potencyjnych routes"""
        population = []

        for i in range(self.population_size):
            route = rd.sample(range(len(self.list_of_cities)), len(self.list_of_cities))
            population.append(route)

        return population

    def selekcja(self, population):
        grupa = rd.sample(population, self.tournament_size)
        winner = max(grupa, key=self.fitness)
        return winner


    def crossover(self):
        pass

    def mutacja(self):
        pass

    def generation(self):
        pass





