from Population import Population
from Board import Board
from time import sleep
import sys

if __name__ == '__main__':
    pop = Population(100, 0.2)
    print('Starting population:\n')
    pop.print_best()
    input()
    for i in range(1000000):
        pop.step()
        if i % 1000 == 9:
            pop.print_best()
            # pop.print_all()
        if pop.contains_winner():
            # clear screen
            print(chr(27) + "[2J")
            print('WIN!')
            break

