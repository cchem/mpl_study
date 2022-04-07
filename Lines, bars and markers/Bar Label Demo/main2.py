import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19689891)
people = ['Tom', 'Dick', 'Harry', 'Slim', 'Jim']
y_pos = list(range(len(people)))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))


def main():
    fig, ax = plt.subplots(2, 2, figsize=(8, 8))

    draw1(ax[0, 0])
    draw2(ax[0, 1])
    draw3(ax[1, 0])
    draw4(ax[1, 1])

    plt.tight_layout()
    plt.savefig('main2.png')
    return


def draw1(ax):
    hbars = ax.barh(y_pos, performance, xerr=error, align='center')
    ax.set_yticks(y_pos, labels=people)
    ax.invert_yaxis()
    ax.set_xlabel('Performance')
    ax.set_title('Original')

    ax.bar_label(hbars, fmt='%.2f')
    ax.set_xlim(right=15)


def draw2(ax):
    hbars = ax.barh(y_pos, performance, xerr=error, align='center')
    ax.set_yticks(y_pos, labels=people)
    # ax.invert_yaxis()
    # ax.set_xlabel('Performance')
    ax.set_title('Edited1')
    #
    # ax.bar_label(hbars, fmt='%.2f')
    # ax.set_xlim(right=15)


def draw3(ax):
    hbars = ax.barh(y_pos, performance, xerr=error, align='center')
    ax.set_yticks(y_pos, labels=people)
    ax.invert_yaxis()
    ax.set_xlabel('Performance')
    ax.set_title('Edited2')

    ax.bar_label(hbars, fmt='%.2f')
    # ax.set_xlim(right=15)


def draw4(ax):
    hbars = ax.barh(y_pos, performance, xerr=error, align='edge')
    ax.set_yticks(y_pos, labels=people)
    ax.invert_yaxis()
    ax.set_xlabel('Performance')
    ax.set_title('NOT ONLY "ax.bar_label"\n BUT ALSO "ax.barh(*args, align="edge")"')

    ax.bar_label(hbars, fmt='%.2f')
    ax.set_xlim(right=15)


if __name__ == '__main__':
    main()
