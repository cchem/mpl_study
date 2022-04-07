import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19689891)
people = ['Tom', 'Dick', 'Harry', 'Slim', 'Jim']
y_pos = list(range(len(people)))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))


def main():
    fig, ax = plt.subplots()

    draw1(ax)
    plt.tight_layout()
    plt.savefig('main3.png')
    return


def draw1(ax):
    hbars = ax.barh(y_pos, performance, xerr=error, align='center')
    ax.set_yticks(y_pos, labels=people)
    ax.invert_yaxis()
    ax.set_xlabel('Performance')
    ax.set_title('How fast do you want to today?')

    ax.bar_label(hbars, labels=[f'±{i:.2f}' for i in error], c='b', fontsize=14, padding=8)
    ax.set_xlim(right=15)


if __name__ == '__main__':
    main()
