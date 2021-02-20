import random

class Board:

    def __init__(self, genes):
        self.genes = genes
        # self.queens = []
        # for (x, y) in enumerate(genes):
            # self.add_queen(x, y)
        self.collisions = self.count_collisions()
        # self.fitness = 28 - self.count_collisions()

    def breed(self, other, mutation_chance = 0):
        return Board.breed_parents(self, other, mutation_chance)

    @staticmethod
    def breed_parents(parent0, parent1, mutation_chance = 0):
        def child(parent0, parent1, crossover, mutation_chance):
            genes = []
            for i in range(8):
                if i < crossover:
                    genes.append(parent0.genes[i])
                else:
                    genes.append(parent1.genes[i])
            # mutate
            if random.uniform(0, 1) < mutation_chance:
                i = random.randint(0,7)
                genes[i] = random.randint(0,7)
            return Board(genes)

        def mutate(self):
            print(f'mutating {self.gene_str()}')
            genes = self.genes.copy()

        crossover = random.randint(0,7)
        child0 = child(parent0, parent1, crossover, mutation_chance)
        child1 = child(parent1, parent0, crossover, mutation_chance)
        return (child0, child1)


    @staticmethod
    def random():
        genes = []
        for x in range(8):
            y = random.randint(0,7)
            genes.append(y)
        return Board(genes)


    def print(self):
        Board.printn(self)

    @staticmethod
    def printn(boards):
        if not isinstance(boards, list):
            boards = [boards]
        print()
        for y in range(8):
            for b in boards:
                for x in range(8):
                    print(f"{'♛' if b.queen_at(x, y) else '.'}", end=' ')
                print(' ', end='')
            print()
        for b in boards:
            print(f'{b.collisions}'.ljust(3) +
                  b.gene_str().rjust(12), end='  ')
        print()


    def gene_str(self):
        return f'~{"".join(map(lambda x : str(x), self.genes))}'


    def queen_at(self, x, y):
        return self.genes[x] == y


    @staticmethod
    def within_queen_move(x0, y0, x1, y1):
        diff_x = abs(x0 - x1)
        diff_y = abs(y0 - y1)
        return x0 == x1 or y0 == y1 or diff_x == diff_y


    def count_collisions(self, verbose=False):
        collisions = 0
        for (x0, y0) in enumerate(self.genes):
            for (x1, y1) in enumerate(self.genes[x0+1:]):
                if Board.within_queen_move(x0, y0, x1, y1):
                    collisions += 1
        return collisions

