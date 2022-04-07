import matplotlib.pyplot as plt
import numpy as np

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
men_std = [2, 3, 4, 1, 2]
women_std = [3, 5, 2, 3, 3]
width = 0.45


def main():
    fig, ax = plt.subplots()

    ax.bar(labels, men_means, yerr=men_std, width=width, label='Men')
    ax.bar(labels, women_means, yerr=women_std, width=width, label='Women', bottom=men_means)
    ax.legend()

    plt.savefig('main.png')
    return


if __name__ == '__main__':
    main()
