import random

class Board:
    mutation_chance = 0.1

    def __init__(self, genes):
        self.genes = genes
        # self.collisions = self.count_collisions()
        self.score = 28 - self.count_collisions()
        self.fitness = 1.0 # set by Population

    def breed(self, other):
        return Board.breed_parents(self, other)

    @staticmethod
    def breed_parents(parent0, parent1):
        crossover = random.randint(0,7)
        genes = []
        for i in range(8):
            if i < crossover:
                genes.append(parent0.genes[i])
            else:
                genes.append(parent1.genes[i])
        # mutate
        if random.uniform(0, 1) < Board.mutation_chance:
            i = random.randint(0,7)
            genes[i] = random.randint(0,7)
        return Board(genes)


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
            print(f'{b.score}'.ljust(3) +
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
                x1 += x0+1
                if Board.within_queen_move(x0, y0, x1, y1):
                    if verbose:
                        print(f'({x0}, {y0}) can collide with ({x1}, {y1})')
                    collisions += 1
        return collisions

    # def __eq__(self, other):
    #     return self.genes == other.genes

    # def __ne__(self, other):
    #     return not self.genes == other.genes

    def __add__(self, other):
        return self.breed(other)
