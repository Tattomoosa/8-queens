from Board import Board
import random
import sys

class Population:

    def __init__(self, size=10, mutation_chance=0.1):
        pop = []
        for i in range(size):
            pop.append(Board.random())
        self.pop = pop
        self.size = size
        Board.mutation_chance = mutation_chance
        self.generation = 0
        self.fitness_sum = 0
        self.fitness_max = 0


    def step(self):
        self.update_fitness()
        children = []
        # for i in range(self.size):
        while len(children) < self.size:
            parents = self.select_parents()
            children.append(parents[0].breed(parents[1]))
            children.append(parents[1].breed(parents[0]))
        while len(children) > self.size:
            children.pop()
        self.pop = children
        self.generation += 1


    def sort(self):
        self.pop.sort(key=lambda x : x.score)
        self.pop.reverse()


    def update_fitness(self):
        fitness_sum = 0
        for pop in self.pop:
            fitness_sum += pop.score
        for pop in self.pop:
            # on low population sizes, rarely every board can wind up with a fitness of
            # 0. seems like maybe that shouldn't happen, but since it does let's
            # stop it.
            pop.fitness = (pop.score / fitness_sum) if fitness_sum != 0 else 0
        self.fitness_sum = fitness_sum
        self.fitness_max = (28 / fitness_sum) if fitness_sum != 0 else 0



    def select_parents(self):
        parent0, parent1 = None, None
        while parent0 is None:
            rnd = random.uniform(0,self.fitness_max)
            choices = [x for x in self.pop if x.fitness >= rnd]
            if len(choices) >= 1:
                parent0 = random.choice(choices)

        while parent1 is None:
            rnd = random.uniform(0,1)
            choices = [x for x in self.pop if x.fitness >= rnd]
            if len(choices) >= 1:
                p = random.choice(choices)
                if p != parent0:
                    parent1 = p

        return (parent0, parent1)


    def print(self):
        # clear screen
        print(chr(27) + "[2J")
        print(f'GENERATION: {self.generation}')
        print(f'BEST: {self.get_best_score()}')
        print(f'AVG: {self.get_avg_score()}')


    def print_all(self):
        self.print()
        i = 0
        n = 16
        while i < len(self.pop):
            Board.printn(self.pop[i:i+n])
            i += n


    def print_best(self):
        self.print()
        print('BEST:')
        self.get_best().print()


    def get_best(self):
        best = self.pop[0]
        for pop in self.pop:
            if pop.score > best.score:
                best = pop
        return best


    def get_best_score(self):
        return self.get_best().score


    def get_avg_score(self):
        n = 0
        for pop in self.pop:
            n += pop.score
        return n / len(self.pop)


    def contains_winner(self):
        for p in self.pop:
            if p.score == 28:
                return True
        return False
