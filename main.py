from Population import Population
from Board import Board
from time import sleep

if __name__ == '__main__':
    pop = Population(96, 0.05)
    print('Starting population:\n')
    pop.print()
    input()
    for i in range(1000000):
        pop.step()
        if i % 100 == 0:
            pop.print()
        if pop.contains_winner():
            # clear screen
            print(chr(27) + "[2J")
            print('WIN!')

