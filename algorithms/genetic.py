from math import dist
from itertools import combinations
import random as rd
from random import random


class Genetyczny_alg:
    def __init__(self):
        self.list_of_cities = []
        self.distances = {}
        self.population_size = 100
        self.generations = 100
        self.elitism = True
        self.tournament_size = 5
        self.mutation = 0.05 #  domyślnie

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

    def koszt(self, route):
        """kalkulacja efektywności trasy według kosztu
        koszt = cała trasa/cały priorytet"""
        total_dist = self.total_dystans(route)
        total_priority = sum(self.list_of_cities[i][2] for i in route)

        return total_dist / total_priority if total_priority != 0 else total_dist

    def fitness(self, route):
        """ocena trasy: im mniejszy coszt tym większy fitness"""
        ocena = self.koszt(route)

        return (1 / ocena) if ocena>0 else 0


    def populacja(self):
        """lista potencyjnych routes"""
        population = []

        for i in range(self.population_size):
            route = rd.sample(range(len(self.list_of_cities)), len(self.list_of_cities))
            population.append(route)

        return population

    def selekcja(self, population):
        """selekcja turniejowa - szukamy zwycięcę który ma największy fitness"""
        grupa = rd.sample(population, self.tournament_size)
        winner = max(grupa, key=self.fitness)
        return winner

    def krzyzowanie(self, parent1, parent2):
        size = len(parent1)
        a,b = sorted(rd.sample(range(size), 2)) #wybieramy dwa dowolne punkty segmentu

        child = [None] * size #tworzymy dziecka
        child[a:b] = parent1[a:b] #kopiujemy część od pierwszego ojca
        remaining = [item for item in parent2 if item not in child]

        idx = 0
        for i in range(size):
            if child[i] is None:
                child[i] = remaining[idx]
                idx += 1

        return child

    def mutacja(self, route):
        if rd.random() < self.mutation:
            a = rd.randint(0, len(route)-1)
            b = rd.randint(0, len(route)-1)

            if a == b:
                return route

            city1 = route[a]
            city2 = route[b]

            route[a] = city2
            route[b] = city1

            return route



    def pokolenie(self):
        pass


