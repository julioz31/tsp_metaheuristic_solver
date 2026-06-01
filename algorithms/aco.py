from math import dist


class Mrowkowy_alg:
    def __init__(self):
        self.list_of_cities = []
        self.distances = {}
        self.pheromones = {}
        #parametry do zmiany
        self.ant_count = 25
        self.iterations = 100
        self.pheromone_evaporation = 0.1
        self.alpha = 0.2
        self.beta = 0.4
        self.Q = 200

    def dystans_miasta(self, cities):
        """kalkulacja dystansu pomiędzy miastami i wnisienie do słownika"""
        self.list_of_cities = cities
        self.distances = {}

        for i in range(len(cities)):
            for j in range(len(cities)):
                if i != j:
                    p1 = (cities[i][0], cities[i][1])
                    p2 = (cities[j][0], cities[j][1])

                    base_dist = dist(p1, p2)
                    y1 = cities[i][1]
                    y2 = cities[j][1]

                    if y2 > y1:
                        self.distances[(i, j)] = base_dist * 1.3
                    else:
                        self.distances[(i, j)] = base_dist

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

    def start_city(self):
        pass

    def next_city(self):
        pass

    def pheromone_update(self):
        pass

    def krok(self):
        pass