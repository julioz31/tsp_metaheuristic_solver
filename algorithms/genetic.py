import math
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
        self.mutation = 0.05

    def dystans_miasta(self, cities):
        """kalkulacja dystansu pomiędzy miastami i wnisienie do słownika"""
        self.list_of_cities = cities
        self.distances = {}

        for i in range(len(cities)):
            for j in range(len(cities)):
                if i != j:
                    x1 = cities[i][0]
                    x2 = cities[j][0]
                    y1 = cities[i][1]
                    y2 = cities[j][1]

                    base_dist = math.sqrt((x1 - x2)**2 + (y1-y2)**2)  # dist(p1, p2)
                    self.distances[(i,j)] = base_dist

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
        """OX"""
        size = len(parent1)
        a,b = sorted(rd.sample(range(size), 2)) #wybieramy dwa dowolne punkty segmentu

        child = [None] * size #tworzymy dziecka
        child[a:b] = parent1[a:b] #kopiujemy część od pierwszego ojca

        parent2_ordered = parent2[b:] + parent2[:b]
        remaining = [item for item in parent2_ordered if item not in child]

        idx = 0
        for i in range(size):
            pos = (b + i) % size
            if child[pos] is None:
                child[pos] = remaining[idx]
                idx += 1

        return child

    def mutacja(self, route):
        """mutowanie trasy: zmiania wybranych miast miejscami
        inversion mutation"""
        if rd.random() < self.mutation:
            a,b = sorted(rd.sample(range(len(route)), 2))

            if a == b or (b - a) == 1:
                return route

            mutation = route[a:b]
            mutation = mutation[::-1]
            route[a:b] = mutation

        return route

    def pokolenie(self, popul):
        """obliczanie jednej iteracji / pokolenia"""
        new_popul = []
        if self.elitism:
            new_popul.append(min(popul, key=self.koszt))

        start_range = 1 if self.elitism else 0
        for j in range(start_range, self.population_size):
            parent1 = self.selekcja(popul)
            parent2 = self.selekcja(popul)
            child = self.krzyzowanie(parent1, parent2)
            child = self.mutacja(child)
            new_popul.append(child)
        return new_popul
