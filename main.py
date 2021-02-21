from Population import Population
from Board import Board

PRINT_EVERY = 1
POP_SIZE = 1000
ITER_MAX = 1000
MUT_CHANCE = 0.01

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
            print('\nCONGRATULATIONS! WIN!')
            win = True
            break

        pop.step()

    title = 'SUCCESS' if win else 'FAILURE'
    title += f' - Pop Size: {POP_SIZE}, Mutation Chance: {MUT_CHANCE * 100}%'
    figtitle = 'success' if win else 'failure'
    figtitle += f'_size_{POP_SIZE}_mut_chance_{MUT_CHANCE}_iter_{pop.generation}'
    plot_results(title, figtitle, best_info, avg_info)

if __name__ == '__main__':
    main()
