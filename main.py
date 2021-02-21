import time
from Population import Population

# How many steps between printing an update
PRINT_EVERY = 100
# Size of population each step
POP_SIZE = 10
# If no answer is found in this many iterations, give up
ITER_MAX = 100_000
# Chance of mutation - per child
MUT_CHANCE = 1.0

def plot_results(title, figtitle, best_results, avg_results):
    try:
        import matplotlib.pyplot as plt
        plt.title(title)
        best_plt, = plt.plot(best_results, color='red')
        avg_plt, = plt.plot(avg_results, color='blue')
        plt.legend((best_plt, avg_plt), ('Best', 'Average'))
        plt.ylim([0, 28])
        plt.xlabel('Iterations')
        plt.ylabel('Fitness')
        writepath = f'figures/{figtitle}.png'
        print(f'writing {writepath}')
        plt.savefig(writepath)
    except:
        print('matplotlib not found, no plot generated')

def main():
    best_info = []
    avg_info = []
    pop = Population(POP_SIZE, MUT_CHANCE)
    win = False
    for i in range(ITER_MAX):

        best_info.append(pop.get_best_score())
        avg_info.append(pop.get_avg_score())

        if i % PRINT_EVERY == 0:
            pop.print_best()

        if pop.contains_winner():
            # clear screen
            print(chr(27) + "[2J")
            pop.print_best()
            print('\nCONGRATULATIONS! YOU WIN!')
            win = True
            break

        pop.step()

    title = f'SUCCESS at {pop.generation}' if win else 'FAILURE'
    title += f' - Pop Size: {POP_SIZE}, Mutation Chance: {MUT_CHANCE * 100}%'
    figtitle = 'success' if win else 'failure'
    figtitle += f'_size_{POP_SIZE}_mut_chance_{MUT_CHANCE}_iter_{pop.generation}_ts_{time.time()}'
    plot_results(title, figtitle, best_info, avg_info)

if __name__ == '__main__':
    main()
