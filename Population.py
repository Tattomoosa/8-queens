from Board import Board
import random
import sys

PICK_PARENTS_FROM=3

class Population:

    def __init__(self, size=10, mutation_chance=0.1):
        pop = []
        for i in range(size):
            pop.append(Board.random())
        # pop.sort(key=lambda x : x.collisions)
        self.pop = pop
        self.size = size
        Board.mutation_chance = mutation_chance
        self.generation = 0

    def get_best_score(self):
        return self.get_best().score

    def step(self):
        self.update_fitness()
        parents = self.select_parents()

    def sort(self):
        self.pop.sort(key=lambda x : x.score)
        self.pop.reverse()

    def update_fitness(self):
        fitness_sum = 0
        for pop in self.pop:
            fitness_sum += pop.score
        for pop in self.pop:
            pop.fitness = pop.score / fitness_sum

    def select_parents(self, fitness):
        parent0 = None
        while parent0 is None:
            rnd = random.uniform(0,1)
            choices = [x for x in self.pop if x.fitness < ]

    def select_fitness_then_breed(self, do_print=False):
        # cull last 3
        # self.sort()
        # for i in range(0, 3):
            # self.pop.pop()

        if do_print:
            print("SURVIVORS")
            Board.printn(self.pop)
            input()

        children = []

        # while len(self.pop) < self.size:
        while len(children) < self.size:
            for parent0 in self.pop:
                parent1 = self.pop[random.randint(0, len(self.pop) - 1)]
                children.append(parent0 + parent1)

        if do_print:
            print("CHILDREN")
            Board.printn(children)
            input()

        self.pop.extend(children)
        self.sort()
        while len(self.pop) > self.size:
            self.pop.pop()

        if do_print:
            print("POPULATION")
            Board.printn(self.pop)
            input()

        self.generation += 1




    # this way is naive, an initial exploration. it gets stuck at score=24 every time
    # which is interesting but not super helpful.
    def best_of_random_method(self):
        pop = []
        while len(pop) < self.size:
            potential = Population.pickRandomIndividuals(self.pop, PICK_PARENTS_FROM)
            parent0 = Population.pickRandomBestIndividual(potential)
            parent1 = None
            while parent1 is None or parent0 == parent1:
                potential = Population.pickRandomIndividuals(self.pop, PICK_PARENTS_FROM)
                parent1 = Population.pickRandomBestIndividual(potential)
            pop.extend(parent0 + parent1)

        while len(pop) > self.size:
            pop.pop()

        self.pop = pop
        self.generation += 1

    @staticmethod
    def pickRandomBestIndividual(boards):
        best = [boards[0]]
        for board in boards[1:]:
            if board.score > best[0].score:
                best = [board]
            elif board.score == best[0].score:
                best.append(board)
        return best[random.randint(0, len(best) - 1)]

    @staticmethod
    def pickRandomIndividuals(boards, count):
        picked = []
        while len(picked) < count:
            board = boards[random.randint(0, len(boards) - 1)]
            if board not in picked:
                picked.append(board)
            picked.append(board)
        return picked

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
