from Board import Board
import random
import sys

PICK_PARENTS_FROM=5

class Population:

    def __init__(self, size=10, mutation_chance=0.1):
        pop = []
        for i in range(size):
            pop.append(Board.random())
        pop.sort(key=lambda x : x.collisions)
        self.pop = pop
        self.current_best = self.get_best()
        self.size = size
        self.mutation_chance = mutation_chance
        self.generation = 0

    def get_best(self):
        best = 1000
        for pop in self.pop:
            if pop.collisions < best:
                best = pop.collisions
        return best

    def step(self):

        pop = []
        while len(pop) < self.size:
            potential = self.pickRandomIndividuals(PICK_PARENTS_FROM)
            parent0 = Population.pickBestIndividual(potential)
            parent1 = None
            while parent1 is None or parent0 == parent1:
                potential = self.pickRandomIndividuals(PICK_PARENTS_FROM)
                parent1 = Population.pickBestIndividual(potential)
            pop.extend(parent0.breed(parent1, self.mutation_chance))

        while len(pop) > self.size:
            pop.pop()

        self.pop = pop
        self.generation += 1

    @staticmethod
    def pickBestIndividual(boards):
        best = boards[0]
        for board in boards[1:]:
            if board.collisions < best.collisions:
                best = board
        return best

    def pickRandomIndividuals(self, count):
        picked = []
        while len(picked) < count:
            board = self.pop[random.randint(0, self.size - 1)]
            if not board in picked:
                picked.append(board)
            picked.append(board)
        return picked

    def print(self):
        # clear screen
        print(chr(27) + "[2J")
        print(f'GENERATION: {self.generation}')
        print(f'BEST: {self.get_best()}')
        i = 0
        n = 16
        while i < len(self.pop):
            Board.printn(self.pop[i:i+n])
            i += n

    def contains_winner(self):
        for p in self.pop:
            if p.collisions == 0:
                return True
        return False
