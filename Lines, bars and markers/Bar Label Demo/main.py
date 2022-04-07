import matplotlib.pyplot as plt
import numpy as np

n = 5
men_means = (20, 35, 30, 35, -27)
women_means = (25, 32, 34, 20, -25)
men_std = (2, 3, 4, 1, 2)
women_std = (3, 5, 2, 3, 3)
x = np.arange(n)
width = 0.35


def main():
    # fig, ax = plt.subplots()  # 1,1のグラフを作るときは引数不要だと知らなかった。
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))  # 1,1のグラフを作るときは引数不要だと知らなかった。

    draw1(ax[0])
    draw2(ax[1])

    plt.tight_layout()
    plt.savefig('main.png')
    return


def draw1(ax):
    """
    Original Version
    :param ax:
    :return:
    """
    p1 = ax.bar(x, men_means, width, yerr=men_std, label='Men')
    p2 = ax.bar(x, women_means, width, yerr=women_std, label='Women', bottom=men_means)

    ax.axhline(0, color='grey', linewidth=0.8)
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(x, labels=[f'G{i}' for i in range(1, 6)])
    ax.legend()

    ax.bar_label(p1, label_type='center')
    ax.bar_label(p2, label_type='center')
    ax.bar_label(p2)  # これは何？ 一番上に表示する奴？
    return ax


def draw2(ax):
    """
    Original Version
    :param ax:
    :return:
    """
    p1 = ax.bar(x, men_means, width, yerr=men_std, label='Men')
    p2 = ax.bar(x, women_means, width, yerr=women_std, label='Women', bottom=men_means)

    ax.axhline(0, color='grey', linewidth=0.8)
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(x, labels=[f'G{i}' for i in range(1, 6)])
    ax.legend()

    ax.bar_label(p1, label_type='center')
    ax.bar_label(p2, label_type='center')
    # ax.bar_label(p2)  # label_tyep='edge'の省略形だった。
    return ax


if __name__ == '__main__':
    main()
