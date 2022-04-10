import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))


def main():
    fig, ax = plt.subplots()

    bar = ax.barh(y_pos, performance, xerr=error, align='center')
    ax.set_yticks(y_pos, labels=people)
    ax.invert_yaxis()
    ax.set_xlabel('Performance')
    ax.set_title('How fast do  you wan to go today?')

    ax.bar_label(bar, fmt='%.2f', padding=3)
    ax.set_xlim(right=15)
    plt.savefig('main.png')
    return


if __name__ == '__main__':
    main()
